#!/usr/bin/env python3
"""Build one issue of the newspaper into a print-ready PDF.

Usage:
    python3 build.py issues/2026-10-19.py            # -> out/<slug>.pdf + PNG previews
    python3 build.py issues/2026-10-12.py --no-png   # skip previews

Each week: copy the last issue file, change the words, pick illustrations
(lib/art.py ILLUSTRATIONS) and press build. Layout, mascots, chess, sudoku
and QA are all handled here.

How a page is described (see the issue file):
    {"section": "WORLD", "bg": "#4CC9F0", "title": "...",
     "grid": ['"a a b"', '"c d b"', ...],  # CSS grid-template-areas rows
     "rows": "1fr 1fr auto",               # optional grid-template-rows
     "blocks": [ {"type": "story", "area": "a", ...}, ... ]}

QA that runs on every build (fails loudly):
  * any block whose content overflows its box (clipped text/images)
  * any block that pokes outside the page
  * text coverage per page (rule: about 40% max of page area)
  * chess moves are replayed and validated; sudoku uniqueness is asserted
"""
import argparse
import html
import importlib.util
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from lib import art, widgets  # noqa: E402

PAGE_W, PAGE_H = 816, 1056     # US Letter at 96 px/in
TEXT_LIMIT = 0.70   # v2: dense pages by request; layout QA still guards overflow

E = html.escape


def rich(s):
    """Escape text but allow **bold** and *italic* markers."""
    import re
    s = E(s)
    for t in ("b", "i", "br"):   # allow a few trusted inline tags
        s = s.replace(f"&lt;{t}&gt;", f"<{t}>").replace(f"&lt;/{t}&gt;", f"</{t}>")
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    return s


# ---------------------------------------------------------------- block renderers

def burst(text, color="#FFD23F", pos="tr", size=86, rot=-12):
    places = {"tr": "top:-26px;right:-18px", "tl": "top:-26px;left:-18px",
              "br": "bottom:-22px;right:-18px", "bl": "bottom:-22px;left:-18px"}
    star = art._star(50, 50, 48, color, points=12, inner=0.78)
    fs = 26 if len(text) <= 5 else (20 if len(text) <= 8 else 15)
    return (f'<div class="burst" style="{places[pos]};width:{size}px;height:{size}px;transform:rotate({rot}deg)">'
            f'<svg viewBox="0 0 100 100">{star}</svg><span style="font-size:{fs}px">{E(text)}</span></div>')


QR_URLS = []   # every QR printed in this build, checked by decoding the rendered pages


def qr_block(url, label="Read more"):
    svg, px, clean = widgets.qr_svg(url)
    QR_URLS.append(clean)
    return f'<div class="qrbox" style="width:{px+8}px">{svg}<div class="qrl">{E(label)}</div></div>'


def b_story(b):
    illo = art.illo(b["illo"]) if b.get("illo") else ""
    kicker = f'<span class="kicker" style="background:{b.get("kc","#2B2140")}">{E(b["kicker"])}</span>' if b.get("kicker") else ""
    tag = f'<span class="tag">{E(b["tag"])}</span>' if b.get("tag") else ""
    ic = f'<span class="hicon">{art.icon(b["icon"])}</span>' if b.get("icon") else ""
    qr = qr_block(b["qr"]) if b.get("qr") else ""
    fs = f' style="font-size:{b["fs"]}px"' if b.get("fs") else ""
    cols = f' style="column-count:{b["cols"]};column-gap:14px"' if b.get("cols") else ""
    body = "".join(f"<p{fs}>{rich(p)}</p>" for p in b.get("text", []))
    layout = b.get("layout", "top")
    illo_html = f'<div class="illo framed" style="background:{art.illo_bg(illo)}">{illo}</div>' if illo else ""
    words = (f'<div class="words">{kicker}{tag}<h2 style="font-size:{b.get("hs",22)}px">{ic}{rich(b["head"])}</h2>'
             f'<div class="body"{cols}>{qr}{body}</div></div>')
    inner = illo_html + words if layout in ("top", "left") else words + illo_html
    return f'<div class="card story {layout}" style="background:{b.get("bg","#FFFDF5")}">{inner}</div>'


def b_briefs(b):
    items = []
    for it in b["items"]:
        ic = f'<span class="bicon">{art.icon(it[0])}</span>' if it[0] else ""
        items.append(f'<li>{ic}<span><b>{rich(it[1])}</b> {rich(it[2])}</span></li>')
    cols = b.get("cols", 1)
    return (f'<div class="card briefs" style="background:{b.get("bg","#FFFDF5")}"><h3>{E(b["head"])}</h3>'
            f'<ul style="font-size:{b.get("fs",12)}px;column-count:{cols}">{"".join(items)}</ul></div>')


def b_headlines(b):
    items = "".join(f'<li><span class="bicon">{art.icon(ic)}</span><span>{rich(t)}</span><span class="pg2">p.{pg}</span></li>'
                    for ic, t, pg in b["items"])
    return (f'<div class="card headlines" style="background:{b.get("bg","#FFFDF5")}"><h3>{E(b["head"])}</h3>'
            f'<ul style="font-size:{b.get("fs",13)}px">{items}</ul></div>')


def b_quiz(b):
    qs = []
    for i, q in enumerate(b["questions"], 1):
        opts = ""
        if len(q) > 1 and q[1]:
            opts = '<span class="opts">' + " ".join(f"<span>({chr(97+j)}) {rich(o)}</span>" for j, o in enumerate(q[1])) + "</span>"
        qs.append(f'<li><span class="qn">{i}</span><span>{rich(q[0])} {opts}</span></li>')
    return (f'<div class="card quiz" style="background:{b.get("bg","#FFFDF5")}"><h3>{E(b["head"])}</h3>'
            f'<p class="lead">{rich(b.get("lead",""))}</p>'
            f'<ol style="font-size:{b.get("fs",12.5)}px;column-count:{b.get("cols",2)}">{"".join(qs)}</ol></div>')


def b_answers(b):
    ans = " · ".join(f"<b>{i}</b> {rich(a)}" for i, a in enumerate(b["answers"], 1))
    return (f'<div class="card answers" style="background:{b.get("bg","#fff")}"><div class="flip">'
            f'<h3>{E(b.get("head","Answers"))}</h3><p style="font-size:{b.get("fs",11)}px">{ans}</p></div></div>')


def b_mascot(b):
    name, fn = art.MASCOTS[b["who"]]
    side = b.get("side", "left")
    return (f'<div class="mascotbox {side}"><div class="mfig">{fn()}<div class="mname">{E(name)}</div></div>'
            f'<div class="bubble {side}" style="font-size:{b.get("fs",15)}px">{rich(b["say"])}</div></div>')


def b_facts(b):
    items = "".join(f"<li>{rich(x)}</li>" for x in b["items"])
    tag = "ol" if b.get("numbered") else "ul"
    illo = ""
    if b.get("illo"):
        svg = art.illo(b["illo"])
        illo = f'<div class="illo framed {"" if b.get("illo_top") else "mini"}" style="background:{art.illo_bg(svg)}">{svg}</div>'
    col = " col" if b.get("illo_top") else ""
    return (f'<div class="card facts{col}" style="background:{b.get("bg","#FFF3B0")}">{illo}<div class="words">'
            f'<h3>{E(b["head"])}</h3><{tag} style="font-size:{b.get("fs",14)}px">{items}</{tag}></div></div>')


def b_banner(b):
    return f'<div class="banner" style="background:{b.get("bg","#2B2140")};color:{b.get("color","#fff")}">{rich(b["text"])}</div>'


def b_medals(b):
    cells = "".join(f'<div class="medalcell"><div class="illo">{art.illo(k)}</div><div class="mlabel">{rich(t)}</div></div>'
                    for k, t in b["items"])
    text = "".join(f"<p>{rich(p)}</p>" for p in b.get("text", []))
    hs = f' style="font-size:{b["hs"]}px"' if b.get("hs") else ""
    return (f'<div class="card medals" style="background:{b.get("bg","#FFFDF5")}"><h3{hs}>{E(b["head"])}</h3>'
            f'<div class="words">{text}</div><div class="medalrow">{cells}</div>'
            + (f'<div class="pullquote">{rich(b["quote"])}</div>' if b.get("quote") else "") + '</div>')


def b_raw(b):
    return f'<div class="card raw" style="background:{b.get("bg","#FFFDF5")}">{b["html"]}</div>'


def b_masthead(b):
    # Shrink the title for longer paper names so it always fits on one line.
    n = len(b["title"])
    fs = b.get("title_fs") or (104 if n <= 15 else max(56, int(104 * 15 / n)))
    return f'''<div class="masthead">
      <div class="mh-title" style="font-size:{fs}px">{E(b["title"])}</div>
      <div class="mh-tag">{E(b["tagline"])}</div>
      <div class="mh-date">{E(b["dateline"])}</div></div>'''


def b_contents(b):
    rows = "".join(f'<li><span class="pg" style="background:{c}">{n}</span>{E(t)}</li>' for n, t, c in b["items"])
    return f'<div class="card contents" style="background:{b.get("bg","#fff")}"><h3>Inside this issue</h3><ul>{rows}</ul></div>'


def b_chess(b):
    board = widgets.board_from_fen(b["fen"]) if b.get("fen") else widgets.replay(b["moves"], b.get("upto"))
    if b.get("mate_in_one"):   # prove the printed answer is the ONLY mate in one
        sols = [board.san(m) for m in widgets.mate_in_one_moves(board)]
        if sols != [b["mate_in_one"]]:
            raise ValueError(f"Chess puzzle answer check failed: mates found {sols}")
    if b.get("mate_line"):     # replay the printed solution and require checkmate at the end
        tb = board.copy()
        for san in b["mate_line"]:
            tb.push_san(san)
        if not tb.is_checkmate():
            raise ValueError("Chess puzzle solution does not end in checkmate")
    arrows = []
    for a in b.get("arrows", []):
        import chess
        arrows.append(chess.svg.Arrow(chess.parse_square(a[0]), chess.parse_square(a[1]), color=a[2] if len(a) > 2 else "#06D6A0cc"))
    if b.get("expect_mate") and not board.is_checkmate():
        raise ValueError("Chess diagram was expected to be checkmate but is not")
    svg = widgets.board_svg(board, arrows=arrows)
    return (f'<div class="card chessbox" style="background:{b.get("bg","#FFFDF5")}"><h3>{rich(b["head"])}</h3>'
            f'<div class="illo">{svg}</div><div class="cap">{rich(b.get("cap",""))}</div></div>')


def b_movelist(b):
    moves, notes = b["moves"], b["notes"]
    rows = []
    for i in range(0, len(moves), 2):
        n = i // 2 + 1
        w = moves[i]
        bl = moves[i + 1] if i + 1 < len(moves) else ""
        note = notes.get(n, "")
        rows.append(f'<tr><td class="mn">{n}.</td><td class="mv">{E(w)}</td><td class="mv">{E(bl)}</td>'
                    f'<td class="note">{rich(note)}</td></tr>')
    return (f'<div class="card movelist" style="background:{b.get("bg","#FFFDF5")}"><h3>{rich(b["head"])}</h3>'
            f'<table style="font-size:{b.get("fs",12.5)}px">{"".join(rows)}</table></div>')


def b_sudoku(b):
    puzzle, sol = widgets.make_sudoku(b["seed"], b.get("givens", 34))
    clues = sum(1 for r in puzzle for v in r if v)
    b["_meta"] = {"clues": clues}
    return (f'<div class="card sudokubox" style="background:{b.get("bg","#FFFDF5")}">'
            f'<h3>{E(b["head"])}</h3><div class="illo">{widgets.sudoku_svg(puzzle)}</div>'
            f'<div class="cap">{rich(b["cap"])}</div></div>',
            f'<div class="card answerkey"><h3>Sudoku answer (no peeking!)</h3>'
            f'<div class="illo">{widgets.sudoku_svg(sol, cell=16, solution_of=puzzle)}</div></div>')


def b_sudoku_key(b):
    """Answer grid for a sudoku printed on another page. Same seed + givens = same puzzle."""
    puzzle, sol = widgets.make_sudoku(b["seed"], b.get("givens", 34))
    return (f'<div class="card answerkey" style="background:{b.get("bg","#FFFFFF")}"><h3>{E(b.get("head","Sudoku answer"))}</h3>'
            f'<div class="illo">{widgets.sudoku_svg(sol, cell=16, solution_of=puzzle)}</div>'
            f'<div class="cap">Red numbers are the ones you filled in.</div></div>')


def b_origami(b):
    steps = widgets.origami_cup_steps() if b.get("model") == "cup" else widgets.origami_steps()
    cells = "".join(f'<div class="ocell"><div class="onum">{i+1}</div>{svg}<div class="otext">{rich(t)}</div></div>'
                    for i, (svg, t) in enumerate(zip(steps, b["steps"])))
    return (f'<div class="card origami" style="background:{b.get("bg","#FFFDF5")}"><h3>{E(b["head"])}</h3>'
            f'<div class="ogrid">{cells}</div></div>')


def b_leaves(b):
    cells = "".join(f'<div class="lcell"><div class="lbox"></div>{art.leaf(k, c)}<div class="ltext"><b>{E(n)}</b><br>{rich(t)}</div></div>'
                    for k, c, n, t in b["items"])
    return (f'<div class="card leaves" style="background:{b.get("bg","#FFFDF5")}"><h3>{E(b["head"])}</h3>'
            f'<p class="lead">{rich(b["lead"])}</p><div class="lgrid">{cells}</div></div>')


def b_countdown(b):
    cells = "".join(f'<div class="cd" style="background:{c}"><div class="cdd">{E(d)}</div><div class="cdn">{E(n)}</div>'
                    f'<div class="cdt">{rich(t)}</div>'
                    + (f'<div class="illo">{art.illo(ic)}</div>' if ic else "") + '</div>'
                    for d, n, t, c, *rest in b["items"] for ic in [rest[0] if rest else None])
    return (f'<div class="card countdown" style="background:{b.get("bg","#FFFDF5")}"><h3>{E(b["head"])}</h3>'
            f'<div class="cdrow">{cells}</div></div>')


def b_maze(b):
    return (f'<div class="card mazebox" style="background:{b.get("bg","#FFFDF5")}"><h3>{E(b["head"])}</h3>'
            f'<p class="lead">{rich(b.get("lead",""))}</p><div class="illo">{widgets.maze_svg(b["w"], b["h"], b["seed"])}</div></div>')


def b_wordsearch(b):
    g = widgets.word_search(b["words"], b["size"], b["seed"])
    words = " · ".join(b["words"])
    return (f'<div class="card wsbox" style="background:{b.get("bg","#FFFDF5")}"><h3>{E(b["head"])}</h3>'
            f'<div class="illo">{widgets.word_search_svg(g)}</div><p class="wlist">{words}</p></div>')


RENDER = {
    "sudoku_key": b_sudoku_key,
    "maze": b_maze, "wordsearch": b_wordsearch,
    "briefs": b_briefs, "headlines": b_headlines, "quiz": b_quiz, "answers": b_answers,
    "story": b_story, "mascot": b_mascot, "facts": b_facts, "banner": b_banner, "medals": b_medals,
    "raw": b_raw, "masthead": b_masthead, "contents": b_contents, "chess": b_chess,
    "movelist": b_movelist, "origami": b_origami, "leaves": b_leaves, "countdown": b_countdown,
}


# ---------------------------------------------------------------- page assembly

def render_page(i, p, issue):
    blocks_html = []
    for b in p["blocks"]:
        if b["type"] == "sudoku":
            puzzle_html, key_html = b_sudoku(b)
            blocks_html.append(f'<div class="cell" style="grid-area:{b["area"]}">{puzzle_html}</div>')
            if b.get("key_area"):
                blocks_html.append(f'<div class="cell" style="grid-area:{b["key_area"]}">{key_html}</div>')
            continue
        inner = RENDER[b["type"]](b)
        if b.get("burst"):
            bb = b["burst"]
            inner += burst(*bb) if isinstance(bb, (list, tuple)) else burst(bb)
        rot = b.get("rot", 0)
        style = f'grid-area:{b["area"]};' + (f"transform:rotate({rot}deg);" if rot else "")
        blocks_html.append(f'<div class="cell" style="{style}">{inner}</div>')
    header = ""
    if p.get("section"):
        header = (f'<div class="sechead"><div class="secname" style="color:{p.get("secc","#fff")}">{E(p["section"])}</div>'
                  f'<div class="sectitle">{rich(p.get("title",""))}</div>'
                  f'<div class="pgnum">{i}</div></div>')
    grid = " ".join(p["grid"])
    rows = p.get("rows", "")
    cols = p.get("cols", "")
    gstyle = f"grid-template-areas:{grid};" + (f"grid-template-rows:{rows};" if rows else "") + (f"grid-template-columns:{cols};" if cols else "")
    footer = f'<div class="footer">{E(issue["name"])} · {E(issue["week"])} · page {i} of {len(issue["pages"])}</div>'
    return (f'<section class="page" data-page="{i}" style="--bg:{p["bg"]}">'
            f'<div class="doodle"></div>{header}<div class="grid" style="{E(gstyle)}">{"".join(blocks_html)}</div>{footer}</section>')


def build_html(issue):
    css = (ROOT / "lib" / "style.css").read_text()
    pages = "".join(render_page(i + 1, p, issue) for i, p in enumerate(issue["pages"]))
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{E(issue['name'])}</title>
<style>{css}</style></head><body>{pages}</body></html>"""


FIT_JS = r"""
() => document.querySelectorAll('.illo.framed svg.art').forEach(s => {
  const vb = s.viewBox.baseVal, r = s.parentElement.getBoundingClientRect();
  const k = (r.width / r.height) / (vb.width / vb.height);
  s.setAttribute('preserveAspectRatio', (k > 0.82 && k < 1.22) ? 'xMidYMid slice' : 'xMidYMid meet');
})
"""

QA_JS = r"""
() => {
  const out = [];
  document.querySelectorAll('section.page').forEach(pg => {
    const pr = pg.getBoundingClientRect();
    const n = pg.dataset.page;
    const probs = [];
    pg.querySelectorAll('.card, .mascotbox, .banner, .masthead').forEach(el => {
      if (el.scrollHeight > el.clientHeight + 2 || el.scrollWidth > el.clientWidth + 2)
        probs.push('OVERFLOW ' + el.className + ' "' + el.innerText.slice(0,40).replace(/\n/g,' ') + '" (+' +
                   (el.scrollHeight - el.clientHeight) + 'px)');
      const r = el.getBoundingClientRect();
      if (r.left < pr.left - 1 || r.right > pr.right + 1 || r.top < pr.top - 1 || r.bottom > pr.bottom + 1)
        probs.push('OUTSIDE PAGE ' + el.className);
    });
    pg.querySelectorAll('.words, .bubble, .ltext, .otext, .cdt').forEach(el => {
      if (getComputedStyle(el).overflow === 'visible') return;   // grows to fit, can't clip
      if (el.scrollHeight > el.clientHeight + 2) probs.push('TEXT CLIPPED "' + el.innerText.slice(0,40).replace(/\n/g,' ') + '"');
    });
    // text coverage: union-ish estimate via line boxes of text nodes
    let area = 0;
    const walker = document.createTreeWalker(pg, NodeFilter.SHOW_TEXT);
    const range = document.createRange();
    while (walker.nextNode()) {
      const t = walker.currentNode;
      if (!t.textContent.trim()) continue;
      if (t.parentElement.closest('svg')) continue;
      range.selectNodeContents(t);
      for (const r of range.getClientRects()) area += r.width * r.height;
    }
    out.push({page: +n, text_pct: Math.round(1000 * area / (pr.width * pr.height)) / 10, problems: probs});
  });
  return out;
}
"""


def render(issue, outdir, pngs=True):
    from playwright.sync_api import sync_playwright
    outdir.mkdir(parents=True, exist_ok=True)
    stem = issue["slug"]
    html_path = outdir / f"{stem}.html"
    html_doc = build_html(issue).replace("url(fonts/", f"url({(ROOT / 'fonts').as_uri()}/")
    html_path.write_text(html_doc)
    pdf_path = outdir / f"{stem}.pdf"
    with sync_playwright() as p:
        br = p.chromium.launch()
        page = br.new_page(viewport={"width": PAGE_W, "height": PAGE_H})
        page.goto(html_path.as_uri())
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(300)
        loaded = page.evaluate("[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family)")
        page.evaluate(FIT_JS)
        report = page.evaluate(QA_JS)
        global QR_BOXES
        QR_BOXES = page.evaluate("""() => [...document.querySelectorAll('svg.qr')].map(q => {
            const pg = q.closest('section.page'); const pr = pg.getBoundingClientRect(); const r = q.getBoundingClientRect();
            return {page: +pg.dataset.page, x: r.left - pr.left, y: r.top - pr.top, w: r.width, h: r.height};
        })""")
        page.pdf(path=str(pdf_path), width="8.5in", height="11in", print_background=True,
                 margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}, prefer_css_page_size=True)
        br.close()
    if pngs:
        subprocess.run(["pdftoppm", "-png", "-r", "80", str(pdf_path), str(outdir / f"{stem}-p")], check=True)
    return pdf_path, report, sorted(set(loaded))


QR_BOXES = []


def check_qr_codes(pdf_path, expected):
    """Rasterise the PDF at 300 dpi (roughly what a phone camera resolves at reading
    distance), cut out each printed QR code and decode it on its own.
    Returns a list of (expected_url, decoded_or_None) failures."""
    import tempfile, cv2
    fails = []
    scale = 300 / 96
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["pdftoppm", "-png", "-r", "300", str(pdf_path), f"{td}/p"], check=True)
        pages = {}
        det = cv2.QRCodeDetector()
        for url, box in zip(expected, QR_BOXES):
            n = box["page"]
            if n not in pages:
                import glob
                f = sorted(glob.glob(f"{td}/p-*.png"))[n - 1]
                pages[n] = cv2.imread(f)
            img = pages[n]
            data = ""
            for pad, zoom in ((14, 1), (30, 1), (14, 2), (30, 1.5)):   # a few camera-like framings
                x0, y0 = int(box["x"] * scale) - pad, int(box["y"] * scale) - pad
                x1, y1 = int((box["x"] + box["w"]) * scale) + pad, int((box["y"] + box["h"]) * scale) + pad
                crop = img[max(0, y0):y1, max(0, x0):x1]
                if zoom != 1:
                    crop = cv2.resize(crop, None, fx=zoom, fy=zoom, interpolation=cv2.INTER_LINEAR)
                data, *_ = det.detectAndDecode(crop)
                if data:
                    break
            if data != url:
                fails.append((url, data or None))
    return fails


def load_issue(path):
    spec = importlib.util.spec_from_file_location("issue", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.ISSUE


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("issue")
    ap.add_argument("--out", default=str(ROOT / "out"))
    ap.add_argument("--no-png", action="store_true")
    a = ap.parse_args()
    issue = load_issue(a.issue)
    pdf, report, fonts = render(issue, pathlib.Path(a.out), not a.no_png)
    print("PDF:", pdf)
    print("Fonts loaded:", ", ".join(fonts))
    bad = False
    for r in report:
        flag = " <-- over text budget" if r["text_pct"] > TEXT_LIMIT * 100 else ""
        print(f"p{r['page']:>2}: text {r['text_pct']:>5}%{flag}")
        for pr in r["problems"]:
            print("      ", pr)
            bad = True
        bad |= bool(flag)
    # page count check
    n = int(subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout.split("Pages:")[1].split()[0])
    print("Pages in PDF:", n)
    if QR_URLS:
        fails = check_qr_codes(pdf, QR_URLS)
        print(f"QR codes: {len(QR_URLS) - len(fails)}/{len(QR_URLS)} decode correctly from the rendered PDF")
        for url, got in fails:
            print("   !! QR problem:", url, "->", got)
        bad |= bool(fails)
    if n != len(issue["pages"]):
        print(f"!! expected {len(issue['pages'])} pages")
        bad = True
    print("QA:", "PROBLEMS FOUND" if bad else "all clear")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
