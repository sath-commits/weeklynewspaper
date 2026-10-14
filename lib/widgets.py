"""Programmatic puzzle/game graphics: chess boards, sudoku, origami steps.

These are generated in code (not images) so they print crisp and are
guaranteed correct: chess positions come from replaying real moves with
python-chess, and every sudoku is checked for a single unique solution.
"""
import random

import chess
import chess.svg

from .art import O, SW, _svg

# ---------------------------------------------------------------- chess

BOARD_COLORS = {
    "square light": "#FFF1C1", "square dark": "#F15BB5",
    "margin": "#2B2140", "coord": "#FFFFFF",
    "square light lastmove": "#FFE066", "square dark lastmove": "#FFB703",
}


def replay(moves_san, upto=None):
    """Replay SAN moves (list of strings, alternating W/B) and return the board.

    Raises ValueError on any illegal move, so a typo in the content file
    fails the build instead of printing a wrong diagram.
    """
    board = chess.Board()
    for i, san in enumerate(moves_san[: upto if upto is not None else len(moves_san)]):
        try:
            board.push_san(san)
        except ValueError as e:
            raise ValueError(f"Illegal move #{i+1} '{san}': {e}") from None
    return board


def board_svg(board, size=300, arrows=(), flipped=False):
    last = board.peek() if board.move_stack else None
    svg = chess.svg.board(board, size=size, colors=BOARD_COLORS, coordinates=True,
                          lastmove=last, arrows=list(arrows), flipped=flipped)
    return svg.replace("<svg ", '<svg class="chessboard" ', 1)


# ---------------------------------------------------------------- sudoku

def _candidates(g, r, c):
    used = set(g[r]) | {g[i][c] for i in range(9)}
    br, bc = 3 * (r // 3), 3 * (c // 3)
    used |= {g[i][j] for i in range(br, br + 3) for j in range(bc, bc + 3)}
    return [n for n in range(1, 10) if n not in used]


def count_solutions(grid, limit=2):
    g = [row[:] for row in grid]
    count = 0

    def solve():
        nonlocal count
        best, best_c = None, None
        for r in range(9):
            for c in range(9):
                if g[r][c] == 0:
                    cand = _candidates(g, r, c)
                    if not cand:
                        return
                    if best is None or len(cand) < len(best_c):
                        best, best_c = (r, c), cand
        if best is None:
            count += 1
            return
        r, c = best
        for n in best_c:
            g[r][c] = n
            solve()
            if count >= limit:
                g[r][c] = 0
                return
        g[r][c] = 0

    solve()
    return count


def solve_sudoku(grid):
    g = [row[:] for row in grid]

    def go():
        for r in range(9):
            for c in range(9):
                if g[r][c] == 0:
                    for n in _candidates(g, r, c):
                        g[r][c] = n
                        if go():
                            return True
                    g[r][c] = 0
                    return False
        return True

    if not go():
        raise ValueError("Sudoku has no solution")
    return g


def make_sudoku(seed, givens=34):
    """Make a puzzle with exactly one solution and about `givens` clues.

    34 clues with a unique solution is a comfortable easy-medium level.
    Removal is done in symmetric pairs, which looks nicer on the page.
    """
    rng = random.Random(seed)
    full = [[0] * 9 for _ in range(9)]

    def fill():
        for r in range(9):
            for c in range(9):
                if full[r][c] == 0:
                    cand = _candidates(full, r, c)
                    rng.shuffle(cand)
                    for n in cand:
                        full[r][c] = n
                        if fill():
                            return True
                    full[r][c] = 0
                    return False
        return True

    fill()
    puzzle = [row[:] for row in full]
    cells = [(r, c) for r in range(9) for c in range(9) if (r, c) <= (8 - r, 8 - c)]
    rng.shuffle(cells)
    filled = 81
    for r, c in cells:
        if filled <= givens:
            break
        pair = {(r, c), (8 - r, 8 - c)}
        saved = {p: puzzle[p[0]][p[1]] for p in pair}
        for pr, pc in pair:
            puzzle[pr][pc] = 0
        if count_solutions(puzzle) != 1:
            for (pr, pc), v in saved.items():
                puzzle[pr][pc] = v
        else:
            filled -= len(pair)
    # Final guarantees, checked independently of the generator logic.
    assert count_solutions(puzzle) == 1, "puzzle is not unique"
    assert solve_sudoku(puzzle) == full, "solver disagrees with generator"
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]:
                assert puzzle[r][c] == full[r][c]
    return puzzle, full


def sudoku_svg(grid, cell=34, solution_of=None, accent="#E63946"):
    """Draw a grid. If solution_of (the puzzle) is given, original clues are dark and
    filled-in answers are coloured, so the answer key is easy to read."""
    n = 9 * cell
    pad = 4
    parts = [f'<rect x="{pad}" y="{pad}" width="{n}" height="{n}" fill="#fff"/>']
    for br in range(3):
        for bc in range(3):
            if (br + bc) % 2 == 0:
                parts.append(f'<rect x="{pad+bc*3*cell}" y="{pad+br*3*cell}" width="{3*cell}" height="{3*cell}" fill="#F1FCE3"/>')
    for i in range(10):
        w = 3.2 if i % 3 == 0 else 1.1
        p = pad + i * cell
        parts.append(f'<line x1="{pad}" y1="{p}" x2="{pad+n}" y2="{p}" stroke="{O}" stroke-width="{w}"/>')
        parts.append(f'<line x1="{p}" y1="{pad}" x2="{p}" y2="{pad+n}" stroke="{O}" stroke-width="{w}"/>')
    for r in range(9):
        for c in range(9):
            v = grid[r][c]
            if not v:
                continue
            is_clue = solution_of is None or solution_of[r][c] != 0
            col = O if is_clue else accent
            parts.append(f'<text x="{pad+c*cell+cell/2}" y="{pad+r*cell+cell*0.72}" text-anchor="middle" '
                         f'font-family="Fredoka" font-weight="700" font-size="{cell*0.62:.1f}" fill="{col}">{v}</text>')
    return _svg(f"0 0 {n+2*pad} {n+2*pad}", "".join(parts), "sudoku")


# ---------------------------------------------------------------- origami fox

FOX = "#FF8C42"
FOXB = "#FFE8D6"


def _arrow(d):
    return (f'<path d="{d}" fill="none" stroke="#E63946" stroke-width="2.6" marker-end="url(#ah)"/>')


_DEFS = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto">'
         '<path d="M0 0 L10 5 L0 10Z" fill="#E63946"/></marker></defs>')
_FOLD = 'stroke="#2B2140" stroke-width="1.8" stroke-dasharray="5 4" fill="none"'


def origami_steps():
    """Eight diagrams for a simple origami fox face. Geometry is real:
    a square folded into a triangle T(10,25)-(90,25)-(50,65); folding each top
    corner to the bottom point uses the crease from (50,25) to (30,45)/(70,45)."""
    s = []
    # 1 square, colored side down, fold diagonal
    s.append(f'<rect x="20" y="20" width="60" height="60" fill="{FOXB}" stroke="{O}" stroke-width="{SW}" transform="rotate(45 50 50)"/>'
             f'<line x1="8" y1="50" x2="92" y2="50" {_FOLD}/>' + _arrow("M50 14 Q74 30 52 60"))
    # 2 triangle
    s.append(f'<path d="M10 30 H90 L50 70Z" fill="{FOX}" stroke="{O}" stroke-width="{SW}"/>'
             f'<line x1="50" y1="24" x2="50" y2="76" {_FOLD}/>' + _arrow("M24 22 Q50 6 76 22"))
    # 3 center crease shown, fold left corner down
    s.append(f'<path d="M10 25 H90 L50 65Z" fill="{FOX}" stroke="{O}" stroke-width="{SW}"/>'
             f'<line x1="50" y1="25" x2="50" y2="65" stroke="{O}" stroke-width="1" opacity=".5"/>'
             f'<line x1="50" y1="25" x2="30" y2="45" {_FOLD}/>' + _arrow("M14 30 Q20 66 46 66"))
    # 4 left done, fold right corner
    s.append(f'<path d="M50 25 H90 L50 65 L30 45Z" fill="{FOX}" stroke="{O}" stroke-width="{SW}"/>'
             f'<path d="M50 25 L30 45 L50 65Z" fill="#F77F00" stroke="{O}" stroke-width="2"/>'
             f'<line x1="50" y1="25" x2="70" y2="45" {_FOLD}/>' + _arrow("M86 30 Q80 66 54 66"))
    # 5 diamond
    s.append(f'<path d="M50 25 L70 45 L50 65 L30 45Z" fill="#F77F00" stroke="{O}" stroke-width="{SW}"/>'
             f'<line x1="50" y1="25" x2="50" y2="65" stroke="{O}" stroke-width="2"/>'
             f'<line x1="36" y1="58" x2="44" y2="40" {_FOLD}/><line x1="64" y1="58" x2="56" y2="40" {_FOLD}/>'
             + _arrow("M44 62 Q30 50 30 22") + _arrow("M56 62 Q70 50 70 22"))
    # 6 ears up
    s.append(f'<path d="M50 25 L70 45 L50 65 L30 45Z" fill="#F77F00" stroke="{O}" stroke-width="{SW}"/>'
             f'<path d="M44 40 L22 14 L38 48Z" fill="{FOX}" stroke="{O}" stroke-width="2.5"/>'
             f'<path d="M56 40 L78 14 L62 48Z" fill="{FOX}" stroke="{O}" stroke-width="2.5"/>')
    # 7 turn over, fold top down
    s.append(f'<path d="M44 40 L22 14 L38 48Z M56 40 L78 14 L62 48Z" fill="{FOXB}" stroke="{O}" stroke-width="2.5"/>'
             f'<path d="M50 25 L70 45 L50 65 L30 45Z" fill="{FOX}" stroke="{O}" stroke-width="{SW}"/>'
             f'<line x1="38" y1="35" x2="62" y2="35" {_FOLD}/>' + _arrow("M50 14 Q60 22 50 32")
             + '<text x="84" y="84" font-family="Bangers" font-size="13" fill="#E63946" text-anchor="end">FLIP!</text>')
    # 8 finished face
    s.append(f'<path d="M44 40 L22 14 L38 48Z M56 40 L78 14 L62 48Z" fill="{FOX}" stroke="{O}" stroke-width="2.5"/>'
             f'<path d="M40 35 H60 L70 45 L50 65 L30 45Z" fill="#F77F00" stroke="{O}" stroke-width="{SW}"/>'
             f'<circle cx="42" cy="44" r="3" fill="{O}"/><circle cx="58" cy="44" r="3" fill="{O}"/>'
             f'<circle cx="50" cy="61" r="3.4" fill="{O}"/><path d="M36 50 l-8 -2 M36 53 l-8 2 M64 50 l8 -2 M64 53 l8 2" stroke="{O}" stroke-width="1.4"/>')
    return [_svg("0 0 100 90", _DEFS + x, "ostep") for x in s]


# ---------------------------------------------------------------- QR codes

QR_MODULE_PX = 1.6   # ~0.42 mm per module printed; verified by decoding the rendered PDF


def qr_svg(url, min_px=50):
    """Crisp vector QR code. Size grows with URL length so modules never get too
    small to scan. Returns (svg, size_px)."""
    import qrcode
    from urllib.parse import urlsplit, urlunsplit
    parts = urlsplit(url)
    url = urlunsplit((parts.scheme, parts.netloc, parts.path, parts.query, ""))  # drop #fragments
    # Smallest code first; if a reference decoder can't read even a perfect copy,
    # step up the error-correction level so the printed code is robust.
    import cv2, numpy as np
    for level in (qrcode.constants.ERROR_CORRECT_L, qrcode.constants.ERROR_CORRECT_M, qrcode.constants.ERROR_CORRECT_Q):
        q = qrcode.QRCode(error_correction=level, border=2)
        q.add_data(url)
        q.make(fit=True)
        m = q.get_matrix()
        ref = cv2.resize(((1 - np.array(m, dtype=np.uint8)) * 255), None, fx=8, fy=8, interpolation=cv2.INTER_NEAREST)
        ref = cv2.copyMakeBorder(ref, 32, 32, 32, 32, cv2.BORDER_CONSTANT, value=255)
        if cv2.QRCodeDetector().detectAndDecode(ref)[0] == url:
            break
    n = len(m)
    rects = "".join(f'<rect x="{x}" y="{y}" width="1.02" height="1.02"/>'
                    for y, row in enumerate(m) for x, v in enumerate(row) if v)
    size = max(min_px, round(n * QR_MODULE_PX))
    svg = (f'<svg class="qr" viewBox="0 0 {n} {n}" width="{size}" height="{size}" shape-rendering="crispEdges" '
           f'xmlns="http://www.w3.org/2000/svg"><rect width="{n}" height="{n}" fill="#fff"/>'
           f'<g fill="#000">{rects}</g></svg>')
    return svg, size, url


# ---------------------------------------------------------------- v3 activity widgets

def board_from_fen(fen):
    return chess.Board(fen)


def mate_in_one_moves(board):
    """All moves that give immediate checkmate. Used to prove a puzzle has one answer."""
    sols = []
    for mv in list(board.legal_moves):
        board.push(mv)
        if board.is_checkmate():
            sols.append(mv)
        board.pop()
    return sols


def maze_svg(w, h, seed, cell=22, start_label="START", end_label="FINISH"):
    """Perfect maze (exactly one path between any two cells) via randomized DFS,
    so it is always solvable. Returns svg."""
    rng = random.Random(seed)
    walls = {(x, y): {"N", "S", "E", "W"} for x in range(w) for y in range(h)}
    seen = {(0, 0)}
    stack = [(0, 0)]
    d = {"N": (0, -1, "S"), "S": (0, 1, "N"), "E": (1, 0, "W"), "W": (-1, 0, "E")}
    while stack:
        x, y = stack[-1]
        opts = [(k, x + dx, y + dy, opp) for k, (dx, dy, opp) in d.items()
                if 0 <= x + dx < w and 0 <= y + dy < h and (x + dx, y + dy) not in seen]
        if not opts:
            stack.pop()
            continue
        k, nx, ny, opp = rng.choice(opts)
        walls[(x, y)].discard(k)
        walls[(nx, ny)].discard(opp)
        seen.add((nx, ny))
        stack.append((nx, ny))
    assert len(seen) == w * h
    walls[(0, 0)].discard("W")
    walls[(w - 1, h - 1)].discard("E")
    p = 6
    lines = []
    for (x, y), ws in walls.items():
        X, Y = p + x * cell, p + y * cell
        if "N" in ws: lines.append(f"M{X} {Y}h{cell}")
        if "W" in ws: lines.append(f"M{X} {Y}v{cell}")
        if y == h - 1 and "S" in ws: lines.append(f"M{X} {Y+cell}h{cell}")
        if x == w - 1 and "E" in ws: lines.append(f"M{X+cell} {Y}v{cell}")
    W, H = w * cell + 2 * p, h * cell + 2 * p
    body = (f'<rect width="{W}" height="{H}" fill="#fff"/>'
            f'<path d="{" ".join(lines)}" stroke="{O}" stroke-width="2.6" stroke-linecap="square" fill="none"/>'
            f'<circle cx="{p+cell/2}" cy="{p+cell/2}" r="{cell*0.28}" fill="#06D6A0"/>'
            f'<circle cx="{p+(w-0.5)*cell}" cy="{p+(h-0.5)*cell}" r="{cell*0.28}" fill="#E63946"/>')
    return _svg(f"0 0 {W} {H}", body, "maze")


def word_search(words, size, seed):
    """Place words in 4 directions, fill the rest. Verifies every word can be found."""
    rng = random.Random(seed)
    dirs = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for _ in range(500):
        g = [[None] * size for _ in range(size)]
        ok = True
        for wd in sorted(words, key=len, reverse=True):
            placed = False
            for _ in range(400):
                dx, dy = rng.choice(dirs)
                x, y = rng.randrange(size), rng.randrange(size)
                ex, ey = x + dx * (len(wd) - 1), y + dy * (len(wd) - 1)
                if not (0 <= ex < size and 0 <= ey < size):
                    continue
                if all(g[y + dy * i][x + dx * i] in (None, c) for i, c in enumerate(wd)):
                    for i, c in enumerate(wd):
                        g[y + dy * i][x + dx * i] = c
                    placed = True
                    break
            if not placed:
                ok = False
                break
        if ok:
            break
    else:
        raise ValueError("could not place all words")
    letters = "ABCDEFGHIKLMNOPRSTUVWY"
    for y in range(size):
        for x in range(size):
            if g[y][x] is None:
                g[y][x] = rng.choice(letters)
    # independent check: every word appears in some direction
    def found(wd):
        for y in range(size):
            for x in range(size):
                for dx, dy in [(1,0),(0,1),(1,1),(1,-1),(-1,0),(0,-1),(-1,-1),(-1,1)]:
                    if all(0 <= x+dx*i < size and 0 <= y+dy*i < size and g[y+dy*i][x+dx*i] == c for i, c in enumerate(wd)):
                        return True
        return False
    assert all(found(w) for w in words)
    return g


def word_search_svg(grid, cell=24):
    n = len(grid)
    p = 4
    t = "".join(f'<text x="{p+x*cell+cell/2}" y="{p+y*cell+cell*0.72}" text-anchor="middle" font-family="Fredoka" '
                f'font-weight="700" font-size="{cell*0.62:.1f}" fill="{O}">{grid[y][x]}</text>'
                for y in range(n) for x in range(n))
    W = n * cell + 2 * p
    return _svg(f"0 0 {W} {W}", f'<rect width="{W}" height="{W}" rx="8" fill="#fff"/>{t}', "wsearch")


def origami_cup_steps():
    """Classic paper cup. Square folded to a triangle T(10,78)-(90,78) apex (50,38)."""
    F = FOX
    s = []
    s.append(f'<rect x="22" y="18" width="56" height="56" fill="{FOXB}" stroke="{O}" stroke-width="{SW}" transform="rotate(45 50 46)"/>'
             f'<line x1="10" y1="46" x2="90" y2="46" {_FOLD}/>' + _arrow("M50 84 Q74 70 52 34"))
    s.append(f'<path d="M10 78 H90 L50 38Z" fill="#4CC9F0" stroke="{O}" stroke-width="{SW}"/>'
             '<text x="50" y="88" font-family="Bangers" font-size="8" text-anchor="middle" fill="#2B2140">FOLD AT THE BOTTOM</text>')
    s.append(f'<path d="M10 78 H90 L50 38Z" fill="#4CC9F0" stroke="{O}" stroke-width="{SW}"/>'
             f'<line x1="22" y1="66" x2="64" y2="78" {_FOLD}/>' + _arrow("M12 74 Q30 40 76 60"))
    s.append(f'<path d="M30 58 L50 38 L90 78 H34Z" fill="#4CC9F0" stroke="{O}" stroke-width="{SW}"/>'
             f'<path d="M30 58 L76 58 L34 78Z" fill="#118AB2" stroke="{O}" stroke-width="2"/>'
             + _arrow("M88 74 Q70 40 24 60"))
    s.append(f'<path d="M30 58 L50 38 L70 58 L66 78 H34Z" fill="#4CC9F0" stroke="{O}" stroke-width="{SW}"/>'
             f'<path d="M30 58 L70 58 L66 78 L34 78Z" fill="#118AB2" stroke="{O}" stroke-width="2"/>'
             f'<line x1="30" y1="58" x2="70" y2="58" {_FOLD}/>' + _arrow("M50 36 Q62 48 50 66"))
    s.append(f'<path d="M30 58 L70 58 L66 78 H34Z" fill="#118AB2" stroke="{O}" stroke-width="{SW}"/>'
             f'<path d="M30 58 L70 58 L50 74Z" fill="#4CC9F0" stroke="{O}" stroke-width="2"/>'
             '<text x="50" y="40" font-family="Bangers" font-size="9" text-anchor="middle" fill="#E63946">FLIP IT OVER!</text>')
    s.append(f'<path d="M28 40 Q50 32 72 40 L64 80 H36Z" fill="#118AB2" stroke="{O}" stroke-width="{SW}"/>'
             f'<ellipse cx="50" cy="40" rx="22" ry="5" fill="#fff" stroke="{O}" stroke-width="2"/>'
             f'<path d="M44 26 q4 -6 0 -12 M56 26 q4 -6 0 -12" fill="none" stroke="#ADB5BD" stroke-width="2"/>')
    return [_svg("0 0 100 90", _DEFS + x, "ostep") for x in s]
