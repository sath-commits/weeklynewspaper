"""Vector cartoon art for the weekly newspaper (mascots, illustrations, icons).

Everything here is hand-built SVG so it stays razor sharp in print and
shares one style: chunky dark outlines, flat bright fills, white glints,
rosy cheeks. Each function returns an <svg> string. Reuse freely week to week;
add new illustrations to ILLUSTRATIONS at the bottom.
"""

O = "#2B2140"          # outline ink
SW = 3                 # outline width
CHEEK = "#FF8FAB"


def _svg(vb, body, cls="art"):
    return (f'<svg class="{cls}" viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" '
            f'preserveAspectRatio="xMidYMid meet" stroke-linejoin="round" stroke-linecap="round">{body}</svg>')


def _eye(x, y, r=6):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{O}"/>'
            f'<circle cx="{x+r*0.35}" cy="{y-r*0.35}" r="{r*0.35}" fill="#fff"/>')


def _cheeks(x1, x2, y, r=5):
    return (f'<ellipse cx="{x1}" cy="{y}" rx="{r}" ry="{r*0.6}" fill="{CHEEK}" opacity=".8"/>'
            f'<ellipse cx="{x2}" cy="{y}" rx="{r}" ry="{r*0.6}" fill="{CHEEK}" opacity=".8"/>')


def _star(cx, cy, r, fill="#FFD23F", points=5, inner=0.45, stroke=True):
    import math
    pts = []
    for i in range(points * 2):
        rr = r if i % 2 == 0 else r * inner
        a = math.pi * i / points - math.pi / 2
        pts.append(f"{cx + rr*math.cos(a):.1f},{cy + rr*math.sin(a):.1f}")
    s = f' stroke="{O}" stroke-width="2"' if stroke else ""
    return f'<polygon points="{" ".join(pts)}" fill="{fill}"{s}/>'


# ---------------------------------------------------------------- mascots

def fox():
    """Scoop the fox reporter, with press hat."""
    b = f'''
    <path d="M92 118 Q128 100 112 70 Q106 92 86 104Z" fill="#FF8C42" stroke="{O}" stroke-width="{SW}"/>
    <path d="M112 70 Q120 82 113 92 Q108 82 104 80Z" fill="#fff" stroke="{O}" stroke-width="2"/>
    <ellipse cx="60" cy="112" rx="30" ry="22" fill="#FF8C42" stroke="{O}" stroke-width="{SW}"/>
    <ellipse cx="60" cy="116" rx="16" ry="14" fill="#FFF4E6"/>
    <rect x="70" y="100" width="22" height="26" rx="3" fill="#fff" stroke="{O}" stroke-width="2" transform="rotate(12 81 113)"/>
    <path d="M75 106 h12 M75 111 h12 M75 116 h8" stroke="#9AA" stroke-width="1.6" transform="rotate(12 81 113)"/>
    <path d="M24 44 L14 8 L46 30Z" fill="#FF8C42" stroke="{O}" stroke-width="{SW}"/>
    <path d="M96 44 L106 8 L74 30Z" fill="#FF8C42" stroke="{O}" stroke-width="{SW}"/>
    <path d="M22 38 L18 18 L36 31Z M98 38 L102 18 L84 31Z" fill="{O}"/>
    <path d="M14 52 Q60 22 106 52 Q100 86 60 100 Q20 86 14 52Z" fill="#FF8C42" stroke="{O}" stroke-width="{SW}"/>
    <path d="M17 58 Q36 70 60 99 Q30 90 17 58Z M103 58 Q84 70 60 99 Q90 90 103 58Z" fill="#FFF4E6"/>
    {_eye(44, 60, 6.5)}{_eye(76, 60, 6.5)}
    {_cheeks(34, 86, 74)}
    <ellipse cx="60" cy="88" rx="6" ry="4.5" fill="{O}"/>
    <path d="M53 94 Q60 99 67 94" fill="none" stroke="{O}" stroke-width="2"/>
    <ellipse cx="60" cy="38" rx="42" ry="8" fill="#5A3E2B" stroke="{O}" stroke-width="{SW}"/>
    <path d="M34 37 Q32 12 60 10 Q88 12 86 37Z" fill="#7A5638" stroke="{O}" stroke-width="{SW}"/>
    <rect x="34" y="27" width="52" height="7" fill="#2B2140"/>
    <rect x="62" y="16" width="24" height="12" rx="1.5" fill="#fff" stroke="{O}" stroke-width="1.6" transform="rotate(-8 74 22)"/>
    <text x="74" y="25" font-family="Bangers" font-size="8.5" fill="#E63946" text-anchor="middle" transform="rotate(-8 74 22)">PRESS</text>
    '''
    return _svg("0 0 130 140", b, "mascot")


def robot():
    """Bolt the teal robot."""
    b = f'''
    <line x1="60" y1="20" x2="60" y2="6" stroke="{O}" stroke-width="{SW}"/>
    <circle cx="60" cy="6" r="6" fill="#FFD23F" stroke="{O}" stroke-width="2.5"/>
    <rect x="20" y="18" width="80" height="58" rx="18" fill="#2EC4B6" stroke="{O}" stroke-width="{SW}"/>
    <rect x="12" y="38" width="10" height="20" rx="4" fill="#FFD23F" stroke="{O}" stroke-width="2.5"/>
    <rect x="98" y="38" width="10" height="20" rx="4" fill="#FFD23F" stroke="{O}" stroke-width="2.5"/>
    <rect x="30" y="28" width="60" height="38" rx="12" fill="#1B2A41" stroke="{O}" stroke-width="2"/>
    <ellipse cx="46" cy="45" rx="7" ry="8" fill="#7CF5E8"/><ellipse cx="74" cy="45" rx="7" ry="8" fill="#7CF5E8"/>
    <circle cx="48" cy="42" r="2.4" fill="#fff"/><circle cx="76" cy="42" r="2.4" fill="#fff"/>
    <path d="M50 57 Q60 63 70 57" fill="none" stroke="#7CF5E8" stroke-width="3"/>
    <ellipse cx="38" cy="58" rx="4" ry="2.4" fill="{CHEEK}"/><ellipse cx="82" cy="58" rx="4" ry="2.4" fill="{CHEEK}"/>
    <rect x="50" y="76" width="20" height="8" fill="#9AA5B1" stroke="{O}" stroke-width="2"/>
    <rect x="28" y="84" width="64" height="44" rx="12" fill="#2EC4B6" stroke="{O}" stroke-width="{SW}"/>
    <circle cx="60" cy="104" r="10" fill="#FFD23F" stroke="{O}" stroke-width="2.5"/>
    <path d="M58 97 L54 105 H61 L57 112" fill="none" stroke="{O}" stroke-width="2.2"/>
    <path d="M28 96 Q12 100 10 116" fill="none" stroke="{O}" stroke-width="{SW+2}"/>
    <path d="M92 96 Q110 88 112 74" fill="none" stroke="{O}" stroke-width="{SW+2}"/>
    <circle cx="10" cy="118" r="6" fill="#FFD23F" stroke="{O}" stroke-width="2.5"/>
    <circle cx="112" cy="72" r="6" fill="#FFD23F" stroke="{O}" stroke-width="2.5"/>
    '''
    return _svg("0 0 122 134", b, "mascot")


def owl():
    """Professor Hoot the owl, with spectacles."""
    b = f'''
    <path d="M22 30 L30 6 L44 24Z M98 30 L90 6 L76 24Z" fill="#7B4FB8" stroke="{O}" stroke-width="{SW}"/>
    <path d="M18 60 Q16 22 60 18 Q104 22 102 60 Q106 118 60 126 Q14 118 18 60Z" fill="#9B5DE5" stroke="{O}" stroke-width="{SW}"/>
    <path d="M36 80 Q60 66 84 80 Q88 112 60 118 Q32 112 36 80Z" fill="#E9D8FD"/>
    <path d="M44 88 q4 4 8 0 M56 88 q4 4 8 0 M68 88 q4 4 8 0 M50 98 q4 4 8 0 M62 98 q4 4 8 0" fill="none" stroke="#B794F4" stroke-width="2"/>
    <path d="M18 66 Q4 88 16 108 Q26 96 30 80Z M102 66 Q116 88 104 108 Q94 96 90 80Z" fill="#7B4FB8" stroke="{O}" stroke-width="{SW}"/>
    <circle cx="42" cy="52" r="17" fill="#fff" stroke="{O}" stroke-width="2"/>
    <circle cx="78" cy="52" r="17" fill="#fff" stroke="{O}" stroke-width="2"/>
    {_eye(44, 53, 7.5)}{_eye(76, 53, 7.5)}
    <circle cx="42" cy="52" r="19" fill="none" stroke="#E63946" stroke-width="3.5"/>
    <circle cx="78" cy="52" r="19" fill="none" stroke="#E63946" stroke-width="3.5"/>
    <path d="M56 50 Q60 46 64 50" fill="none" stroke="#E63946" stroke-width="3.5"/>
    <path d="M54 66 L66 66 L60 76Z" fill="#FFB703" stroke="{O}" stroke-width="2"/>
    <path d="M44 124 l-4 8 M50 125 l0 8 M70 125 l0 8 M76 124 l4 8" stroke="#FFB703" stroke-width="4"/>
    '''
    return _svg("0 0 120 136", b, "mascot")


def peacock():
    """Mayil the peacock (mayil = peacock in Tamil)."""
    feathers = ""
    import math
    for i in range(9):
        a = math.radians(-160 + i * 17.5)
        x, y = 60 + 52 * math.cos(a), 78 + 52 * math.sin(a)
        feathers += (f'<line x1="60" y1="78" x2="{x:.1f}" y2="{y:.1f}" stroke="#2A9D8F" stroke-width="3"/>'
                     f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="10" ry="12" fill="#06D6A0" stroke="{O}" stroke-width="2" transform="rotate({math.degrees(a)+90:.0f} {x:.1f} {y:.1f})"/>'
                     f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="#118AB2"/><circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="#FFD23F"/>')
    b = f'''
    {feathers}
    <path d="M44 132 Q34 96 48 80 Q58 72 70 80 Q86 98 74 132Z" fill="#118AB2" stroke="{O}" stroke-width="{SW}"/>
    <path d="M52 84 Q48 60 56 46 Q66 40 70 52 Q72 66 66 84Z" fill="#118AB2" stroke="{O}" stroke-width="{SW}"/>
    <circle cx="62" cy="44" r="14" fill="#118AB2" stroke="{O}" stroke-width="{SW}"/>
    <path d="M58 30 l-4 -12 M62 30 l0 -13 M66 30 l4 -12" stroke="{O}" stroke-width="2"/>
    <circle cx="54" cy="18" r="3.4" fill="#06D6A0" stroke="{O}" stroke-width="1.5"/><circle cx="62" cy="16" r="3.4" fill="#06D6A0" stroke="{O}" stroke-width="1.5"/><circle cx="70" cy="18" r="3.4" fill="#06D6A0" stroke="{O}" stroke-width="1.5"/>
    <path d="M60 40 q4 -3 9 0 q-4 5 -9 0Z" fill="#fff"/>
    {_eye(65, 41, 4.2)}
    <path d="M74 44 L84 47 L74 51Z" fill="#FFB703" stroke="{O}" stroke-width="2"/>
    <ellipse cx="66" cy="52" rx="3.5" ry="2" fill="{CHEEK}"/>
    <path d="M52 132 l-2 6 M66 132 l2 6" stroke="#FFB703" stroke-width="4"/>
    '''
    return _svg("0 0 120 140", b, "mascot")


MASCOTS = {
    "fox": ("Scoop", fox), "robot": ("Bolt", robot),
    "owl": ("Prof. Hoot", owl), "peacock": ("Mayil", peacock),
}


# ---------------------------------------------------------------- illustrations

def rocket_iss():
    stars = "".join(_star(x, y, r, "#FFF3B0", stroke=False) for x, y, r in
                    [(20, 20, 4), (180, 26, 5), (150, 70, 3), (40, 80, 3), (110, 14, 3), (190, 100, 4)])
    b = f'''
    <rect width="200" height="140" fill="#14213D"/>{stars}
    <path d="M-10 150 Q100 98 210 150Z" fill="#4CC9F0" stroke="{O}" stroke-width="{SW}"/>
    <path d="M40 140 Q60 118 90 126 Q110 112 140 128" fill="none" stroke="#06D6A0" stroke-width="6"/>
    <rect x="98" y="46" width="70" height="6" fill="#ADB5BD" stroke="{O}" stroke-width="2"/>
    <rect x="100" y="22" width="16" height="22" fill="#F4A261" stroke="{O}" stroke-width="2"/>
    <rect x="100" y="54" width="16" height="22" fill="#F4A261" stroke="{O}" stroke-width="2"/>
    <rect x="150" y="22" width="16" height="22" fill="#F4A261" stroke="{O}" stroke-width="2"/>
    <rect x="150" y="54" width="16" height="22" fill="#F4A261" stroke="{O}" stroke-width="2"/>
    <rect x="124" y="40" width="22" height="18" rx="4" fill="#E9ECEF" stroke="{O}" stroke-width="2"/>
    <rect x="118" y="44" width="8" height="10" rx="2" fill="#E9ECEF" stroke="{O}" stroke-width="2"/>
    <path d="M66 49 L106 49" stroke="#FFD23F" stroke-width="2.5" stroke-dasharray="4 4"/>
    <g transform="rotate(90 50 49)">
      <path d="M38 64 L40 40 Q50 22 60 40 L62 64Z" fill="#F8F9FA" stroke="{O}" stroke-width="{SW}"/>
      <rect x="40" y="62" width="20" height="10" fill="#343A40" stroke="{O}" stroke-width="2"/>
      <circle cx="50" cy="46" r="4.5" fill="#4CC9F0" stroke="{O}" stroke-width="2"/>
    </g>
    <text x="14" y="128" font-family="Bangers" font-size="16" fill="#fff" stroke="{O}" stroke-width="0.6">DOCKED!</text>
    '''
    return _svg("0 0 200 140", b)


def trophy_lab():
    b = f'''
    <rect width="200" height="140" fill="#FFF1C1"/>
    {_star(30, 28, 12)}{_star(172, 36, 9, "#FF8FAB")}{_star(160, 112, 7, "#4CC9F0")}
    <path d="M70 30 H130 V58 Q130 88 100 92 Q70 88 70 58Z" fill="#FFD23F" stroke="{O}" stroke-width="{SW}"/>
    <path d="M70 40 Q50 40 52 58 Q56 72 72 70 M130 40 Q150 40 148 58 Q144 72 128 70" fill="none" stroke="{O}" stroke-width="{SW}"/>
    <rect x="92" y="92" width="16" height="16" fill="#FFB703" stroke="{O}" stroke-width="{SW}"/>
    <rect x="76" y="108" width="48" height="16" rx="3" fill="#8D5524" stroke="{O}" stroke-width="{SW}"/>
    <path d="M84 40 Q86 66 100 74" fill="none" stroke="#fff" stroke-width="4" opacity=".7"/>
    <path d="M28 120 L36 82 V66 H48 V82 L56 120Z" fill="#06D6A0" stroke="{O}" stroke-width="{SW}"/>
    <circle cx="40" cy="104" r="3" fill="#fff"/><circle cx="46" cy="96" r="2" fill="#fff"/>
    <path d="M160 124 V100" stroke="#2A9D8F" stroke-width="4"/>
    <path d="M160 104 Q146 94 148 82 Q160 86 160 104 Q174 92 172 80 Q160 84 160 104" fill="#8AC926" stroke="{O}" stroke-width="2"/>
    <text x="100" y="66" font-family="Bangers" font-size="16" text-anchor="middle" fill="{O}">#1</text>
    '''
    return _svg("0 0 200 140", b)


def medal(ribbon="#E63946", label="", bg=None):
    b = (f'<rect width="140" height="140" fill="{bg}"/>' if bg else "") + f'''
    <path d="M44 10 L64 64 L76 58 L58 10Z" fill="{ribbon}" stroke="{O}" stroke-width="{SW}"/>
    <path d="M96 10 L76 64 L64 58 L82 10Z" fill="{ribbon}" stroke="{O}" stroke-width="{SW}" opacity=".85"/>
    <circle cx="70" cy="88" r="38" fill="#FFD23F" stroke="{O}" stroke-width="{SW}"/>
    <circle cx="70" cy="88" r="28" fill="#FFB703" stroke="{O}" stroke-width="2"/>
    <path d="M50 96 Q46 80 54 70 M90 96 Q94 80 86 70" fill="none" stroke="#8D6E00" stroke-width="3"/>
    <text x="70" y="98" font-family="Bangers" font-size="{24 if len(label) < 3 else 15}" text-anchor="middle" fill="{O}">{label}</text>
    <path d="M52 70 Q60 60 74 60" fill="none" stroke="#fff" stroke-width="4" opacity=".8"/>
    '''
    return _svg("0 0 140 140", b)


def brain_switch():
    b = f'''
    <rect width="200" height="140" fill="#1D1145"/>
    <path d="M20 20 L70 46 L70 74 L20 100Z" fill="#4CC9F0" opacity=".35"/>
    <rect x="4" y="36" width="22" height="48" rx="6" fill="#ADB5BD" stroke="{O}" stroke-width="{SW}"/>
    <circle cx="15" cy="60" r="6" fill="#4CC9F0" stroke="{O}" stroke-width="2"/>
    <path d="M72 70 Q66 40 92 34 Q100 18 122 24 Q142 14 156 30 Q178 34 176 58 Q186 78 168 92 Q164 112 140 108 Q124 120 106 108 Q82 114 80 94 Q64 88 72 70Z" fill="#FF8FAB" stroke="{O}" stroke-width="{SW}"/>
    <path d="M96 44 Q108 52 100 64 M126 34 Q122 52 136 58 M150 48 Q160 62 150 74 M108 86 Q122 78 132 92 M88 74 Q96 80 92 90" fill="none" stroke="#C9184A" stroke-width="2.5"/>
    <rect x="114" y="54" width="28" height="40" rx="5" fill="#fff" stroke="{O}" stroke-width="{SW}"/>
    <rect x="122" y="60" width="12" height="16" rx="3" fill="#FFD23F" stroke="{O}" stroke-width="2"/>
    <text x="128" y="90" font-family="Bangers" font-size="9" text-anchor="middle" fill="{O}">ON</text>
    {_star(178, 18, 7)}{_star(96, 122, 5, "#4CC9F0")}
    <path d="M80 60 l-6 -4 M78 70 l-8 0" stroke="#FFD23F" stroke-width="3"/>
    '''
    return _svg("0 0 200 140", b)


def ice_neutrino():
    strings = ""
    for x in (60, 92, 124, 156):
        strings += f'<line x1="{x}" y1="56" x2="{x}" y2="134" stroke="#2B2140" stroke-width="1.5"/>'
        for y in range(66, 132, 14):
            glow = "#FFD23F" if (x + y) % 3 == 0 else "#FFF"
            strings += f'<circle cx="{x}" cy="{y}" r="4" fill="{glow}" stroke="{O}" stroke-width="1.3"/>'
    b = f'''
    <rect width="200" height="140" fill="#0B132B"/>
    {_star(18, 14, 3, "#FFF3B0", stroke=False)}{_star(120, 10, 3, "#FFF3B0", stroke=False)}{_star(190, 30, 4, "#FFF3B0", stroke=False)}
    <rect x="0" y="52" width="200" height="88" fill="#BDE0FE" stroke="{O}" stroke-width="{SW}"/>
    <path d="M0 52 L30 44 L60 52 L100 42 L140 52 L170 46 L200 52" fill="#fff" stroke="{O}" stroke-width="2"/>
    {strings}
    <rect x="150" y="30" width="34" height="16" fill="#ADB5BD" stroke="{O}" stroke-width="2"/>
    <rect x="156" y="20" width="22" height="10" fill="#6C757D" stroke="{O}" stroke-width="2"/>
    <path d="M8 6 Q50 36 84 98" fill="none" stroke="#B5179E" stroke-width="5" stroke-dasharray="2 7" opacity=".9"/>
    <circle cx="86" cy="100" r="11" fill="#E0AAFF" stroke="{O}" stroke-width="2.5" opacity=".95"/>
    {_eye(82, 98, 2.4)}{_eye(90, 98, 2.4)}
    <path d="M82 104 Q86 107 90 104" fill="none" stroke="{O}" stroke-width="1.6"/>
    <circle cx="86" cy="100" r="20" fill="none" stroke="#E0AAFF" stroke-width="2" opacity=".6"/>
    '''
    return _svg("0 0 200 140", b)


def mirror_hands():
    hand = (f'<path d="M30 120 L30 70 Q30 62 37 62 Q44 62 44 70 L44 46 Q44 38 51 38 Q58 38 58 46 L58 40 Q58 32 65 32 '
            f'Q72 32 72 40 L72 48 Q72 40 79 40 Q86 40 86 48 L86 92 Q86 120 60 124Z" '
            f'fill="#FFD6A5" stroke="{O}" stroke-width="{SW}"/>'
            f'<path d="M30 84 Q16 70 10 74 Q4 80 16 92 L30 106" fill="#FFD6A5" stroke="{O}" stroke-width="{SW}"/>')
    b = f'''
    <rect width="200" height="140" fill="#E0C3FC"/>
    <g>{hand}</g>
    <g transform="translate(200 0) scale(-1 1)">{hand}</g>
    <rect x="96" y="6" width="8" height="128" rx="3" fill="#BDE0FE" stroke="{O}" stroke-width="2"/>
    <path d="M98 14 L102 30" stroke="#fff" stroke-width="2"/>
    <circle cx="58" cy="76" r="5" fill="#E63946" stroke="{O}" stroke-width="1.5"/>
    <circle cx="142" cy="76" r="5" fill="#E63946" stroke="{O}" stroke-width="1.5"/>
    <text x="54" y="18" font-family="Bangers" font-size="15" fill="{O}" text-anchor="middle">LEFT</text>
    <text x="146" y="18" font-family="Bangers" font-size="15" fill="{O}" text-anchor="middle">RIGHT</text>
    '''
    return _svg("0 0 200 140", b)


def books():
    b = f'''
    <rect width="140" height="140" fill="#FFE5EC"/>
    <rect x="22" y="40" width="22" height="80" fill="#4CC9F0" stroke="{O}" stroke-width="{SW}"/>
    <rect x="44" y="30" width="22" height="90" fill="#FFD23F" stroke="{O}" stroke-width="{SW}"/>
    <rect x="70" y="44" width="22" height="76" fill="#E63946" stroke="{O}" stroke-width="{SW}" transform="rotate(10 81 120)"/>
    <path d="M100 118 L120 30 Q126 22 128 32 L108 120Z" fill="#fff" stroke="{O}" stroke-width="2.5"/>
    <path d="M12 120 H130" stroke="{O}" stroke-width="{SW}"/>
    <text x="55" y="80" font-family="Bangers" font-size="13" fill="{O}" text-anchor="middle" transform="rotate(-90 55 80)">POEMS</text>
    '''
    return _svg("0 0 140 140", b)


def mystery_box():
    b = f'''
    <rect width="200" height="140" fill="#D8F3DC"/>
    <rect x="50" y="56" width="90" height="66" fill="#9B5DE5" stroke="{O}" stroke-width="{SW}"/>
    <rect x="44" y="44" width="102" height="18" fill="#B388EB" stroke="{O}" stroke-width="{SW}"/>
    <rect x="88" y="44" width="14" height="78" fill="#FFD23F" stroke="{O}" stroke-width="2"/>
    <path d="M95 44 Q76 18 70 34 Q72 44 95 44 Q114 18 120 34 Q118 44 95 44" fill="#FFD23F" stroke="{O}" stroke-width="2.5"/>
    <text x="30" y="46" font-family="Bangers" font-size="34" fill="#E63946" stroke="{O}" stroke-width="1">?</text>
    <text x="156" y="40" font-family="Bangers" font-size="26" fill="#118AB2" stroke="{O}" stroke-width="1">?</text>
    <circle cx="160" cy="96" r="20" fill="#E0FBFC" fill-opacity=".6" stroke="{O}" stroke-width="{SW+1}"/>
    <path d="M174 110 L192 128" stroke="#8D5524" stroke-width="8"/>
    <path d="M174 110 L192 128" stroke="{O}" stroke-width="1"/>
    <g transform="rotate(-14 96 92)"><rect x="56" y="80" width="80" height="22" rx="3" fill="none" stroke="#E63946" stroke-width="3"/>
    <text x="96" y="97" font-family="Bangers" font-size="16" text-anchor="middle" fill="#E63946">RUMOR</text></g>
    '''
    return _svg("0 0 200 140", b)


def ai_chat():
    b = f'''
    <rect width="200" height="140" fill="#CAF0F8"/>
    <rect x="12" y="14" width="110" height="40" rx="14" fill="#fff" stroke="{O}" stroke-width="{SW}"/>
    <path d="M30 54 L24 68 L44 54" fill="#fff" stroke="{O}" stroke-width="{SW}"/>
    <path d="M26 30 H100 M26 40 H80" stroke="#ADB5BD" stroke-width="4"/>
    <rect x="76" y="70" width="112" height="42" rx="14" fill="#2EC4B6" stroke="{O}" stroke-width="{SW}"/>
    <path d="M168 112 L176 126 L152 112" fill="#2EC4B6" stroke="{O}" stroke-width="{SW}"/>
    <path d="M90 86 H170 M90 96 H150" stroke="#fff" stroke-width="4"/>
    <rect x="18" y="80" width="40" height="40" rx="6" fill="#343A40" stroke="{O}" stroke-width="{SW}"/>
    <path d="M24 80 v-6 M34 80 v-6 M44 80 v-6 M52 80 v-6 M24 126 v-6 M34 126 v-6 M44 126 v-6 M52 126 v-6" stroke="{O}" stroke-width="2.5"/>
    <text x="38" y="106" font-family="Bangers" font-size="15" fill="#7CF5E8" text-anchor="middle">AI</text>
    {_star(150, 30, 10)}{_star(176, 52, 6, "#FF8FAB")}
    '''
    return _svg("0 0 200 140", b)


def sea_cucumber():
    b = f'''
    <rect width="200" height="140" fill="#03045E"/>
    <path d="M150 0 L196 0 L120 140 L40 140Z" fill="#90E0EF" opacity=".18"/>
    <circle cx="30" cy="30" r="2" fill="#90E0EF"/><circle cx="60" cy="16" r="1.6" fill="#90E0EF"/><circle cx="176" cy="96" r="2" fill="#90E0EF"/>
    <path d="M0 126 Q50 112 100 124 Q150 116 200 128 V140 H0Z" fill="#6C584C" stroke="{O}" stroke-width="2"/>
    <path d="M40 112 Q34 80 70 74 Q110 64 150 80 Q170 92 160 112 Q100 124 40 112Z" fill="#FFB3C6" fill-opacity=".92" stroke="{O}" stroke-width="{SW}"/>
    <path d="M58 76 Q44 40 60 26 Q64 46 74 72Z M84 70 Q80 32 98 22 Q98 46 96 68Z" fill="#FF8FAB" stroke="{O}" stroke-width="{SW}"/>
    <path d="M50 112 v8 M70 116 v8 M92 118 v8 M114 118 v8 M136 116 v8 M152 112 v8" stroke="{O}" stroke-width="3"/>
    {_eye(136, 92, 4)}{_eye(150, 92, 4)}
    <path d="M136 102 Q143 107 150 102" fill="none" stroke="{O}" stroke-width="2"/>
    <ellipse cx="128" cy="100" rx="4" ry="2.4" fill="#FF4D6D"/>
    <path d="M70 92 Q90 86 110 92" fill="none" stroke="#fff" stroke-width="3" opacity=".7"/>
    <text x="10" y="22" font-family="Bangers" font-size="14" fill="#CAF0F8">2,577 m DOWN</text>
    '''
    return _svg("0 0 200 140", b)


def croc_sphinx():
    b = f'''
    <rect width="200" height="140" fill="#FFE8A3"/>
    <circle cx="170" cy="24" r="14" fill="#FFB703" stroke="{O}" stroke-width="2"/>
    <path d="M100 96 L136 30 L172 96Z" fill="#E9C46A" stroke="{O}" stroke-width="{SW}"/>
    <path d="M136 30 L172 96 L150 96Z" fill="#D4A373"/>
    <path d="M110 96 L110 72 Q110 50 92 48 Q74 50 74 70 L74 96Z" fill="#E9C46A" stroke="{O}" stroke-width="{SW}"/>
    <path d="M70 56 L74 92 L66 92Z M114 56 L110 92 L118 92Z" fill="#E9C46A" stroke="{O}" stroke-width="2"/>
    <path d="M84 64 l6 0 M96 64 l6 0" stroke="{O}" stroke-width="3"/>
    <path d="M90 74 h6" stroke="{O}" stroke-width="2" stroke-dasharray="2 2"/>
    <text x="58" y="56" font-family="Bangers" font-size="12" fill="#E63946" text-anchor="end">NO NOSE!</text>
    <path d="M60 58 L84 70" stroke="#E63946" stroke-width="2"/>
    <rect x="0" y="96" width="200" height="44" fill="#DDA15E" stroke="{O}" stroke-width="2"/>
    <path d="M14 122 Q14 108 30 106 L76 104 L76 120 Q50 128 14 122Z" fill="#F8F9FA" stroke="{O}" stroke-width="{SW}"/>
    <path d="M76 104 L118 108 L118 118 L76 120" fill="#F8F9FA" stroke="{O}" stroke-width="{SW}"/>
    <path d="M118 108 L130 112 L118 118" fill="none" stroke="#E63946" stroke-width="2" stroke-dasharray="3 3"/>
    <circle cx="34" cy="113" r="5" fill="#2B2140"/>
    <path d="M80 118 l4 -4 l4 4 l4 -4 l4 4 l4 -4 l4 4 l4 -4 l4 4" fill="none" stroke="{O}" stroke-width="1.6"/>
    <text x="134" y="132" font-family="Bangers" font-size="12" fill="#E63946">NO SNOUT TIP!</text>
    '''
    return _svg("0 0 200 140", b)


def gharial(bg="#90E0EF"):
    b = f'''
    <rect width="200" height="140" fill="{bg}"/>
    <path d="M0 70 Q50 60 100 70 T200 70 V140 H0Z" fill="#48CAE4" stroke="{O}" stroke-width="2"/>
    <path d="M10 90 Q40 84 60 92 M120 110 Q150 104 180 112" fill="none" stroke="#fff" stroke-width="3" opacity=".7"/>
    <path d="M30 78 Q60 58 110 64 L176 70 Q190 72 188 78 Q186 84 176 82 L110 84 Q70 92 30 86Z" fill="#6A994E" stroke="{O}" stroke-width="{SW}"/>
    <circle cx="182" cy="72" r="7" fill="#6A994E" stroke="{O}" stroke-width="2.5"/>
    <path d="M60 66 l4 -6 l4 6 l4 -6 l4 6 l4 -6 l4 6" fill="#A7C957" stroke="{O}" stroke-width="2"/>
    <circle cx="104" cy="64" r="8" fill="#A7C957" stroke="{O}" stroke-width="2.5"/>
    {_eye(105, 63, 3.5)}
    <path d="M118 80 l4 -3 l4 3 l4 -3 l4 3 l4 -3 l4 3 l4 -3 l4 3 l4 -3 l4 3 l4 -3" fill="none" stroke="#fff" stroke-width="2"/>
    <path d="M30 82 Q10 80 4 70" fill="none" stroke="{O}" stroke-width="{SW}"/>
    <path d="M30 120 Q42 112 58 118 L74 120 Q78 124 72 126 L58 126 Q42 130 30 120Z" fill="#A7C957" stroke="{O}" stroke-width="2"/>
    <circle cx="56" cy="118" r="2" fill="{O}"/>
    <path d="M120 128 Q130 122 142 126 L154 128 Q156 132 150 132 L142 132 Q130 134 120 128Z" fill="#A7C957" stroke="{O}" stroke-width="2"/>
    <circle cx="140" cy="126" r="1.8" fill="{O}"/>
    '''
    return _svg("0 0 200 140", b)


def diya():
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="#fff"/>'
                   for x in range(20, 200, 18) for y in (120, 132))
    b = f'''
    <rect width="200" height="140" fill="#3C096C"/>
    {dots}
    <path d="M100 20 Q118 46 100 62 Q82 46 100 20Z" fill="#FFD23F" stroke="{O}" stroke-width="2.5"/>
    <path d="M100 34 Q108 48 100 56 Q92 48 100 34Z" fill="#FF8C42"/>
    <circle cx="100" cy="42" r="30" fill="#FFD23F" opacity=".18"/>
    <path d="M52 66 Q100 58 148 66 Q140 106 100 108 Q60 106 52 66Z" fill="#E76F51" stroke="{O}" stroke-width="{SW}"/>
    <path d="M52 66 Q100 76 148 66" fill="none" stroke="{O}" stroke-width="2"/>
    <path d="M66 84 q8 6 16 0 q8 6 16 0 q8 6 16 0 q8 6 16 0" fill="none" stroke="#FFD23F" stroke-width="3"/>
    <circle cx="100" cy="96" r="4" fill="#FFD23F"/>
    {_star(30, 30, 8, "#FFD23F")}{_star(170, 36, 10, "#FF8FAB")}{_star(160, 90, 5, "#4CC9F0")}
    '''
    return _svg("0 0 200 140", b)


def kolu():
    dolls = ""
    cols = ["#E63946", "#FFD23F", "#4CC9F0", "#06D6A0", "#9B5DE5", "#FF8C42"]
    for row, (y, xs) in enumerate([(50, [84, 116]), (78, [62, 92, 122, 152]), (106, [40, 70, 100, 130, 160])]):
        for i, x in enumerate(xs):
            c = cols[(i + row) % len(cols)]
            dolls += (f'<path d="M{x-8} {y} L{x} {y-16} L{x+8} {y}Z" fill="{c}" stroke="{O}" stroke-width="1.8"/>'
                      f'<circle cx="{x}" cy="{y-20}" r="5" fill="#FFD6A5" stroke="{O}" stroke-width="1.8"/>')
    b = f'''
    <rect width="200" height="140" fill="#FFCCD5"/>
    <rect x="60" y="50" width="80" height="10" fill="#E63946" stroke="{O}" stroke-width="2"/>
    <rect x="40" y="78" width="130" height="10" fill="#FFB703" stroke="{O}" stroke-width="2"/>
    <rect x="18" y="106" width="170" height="10" fill="#06D6A0" stroke="{O}" stroke-width="2"/>
    <path d="M60 60 V140 M140 60 V78 M40 88 V140 M170 88 V106 M18 116 V140 M188 116 V140" stroke="{O}" stroke-width="2"/>
    {dolls}
    '''
    return _svg("0 0 200 140", b)


def f1_night():
    lights = "".join(f'<rect x="{x}" y="{y}" width="4" height="4" fill="#FFD23F"/>'
                     for x, y in [(18, 40), (26, 52), (18, 64), (60, 30), (68, 46), (150, 36), (158, 50), (166, 64), (110, 46)])
    b = f'''
    <rect width="200" height="140" fill="#22223B"/>
    <rect x="10" y="30" width="26" height="60" fill="#4A4E69" stroke="{O}" stroke-width="2"/>
    <rect x="54" y="20" width="22" height="70" fill="#4A4E69" stroke="{O}" stroke-width="2"/>
    <rect x="102" y="40" width="20" height="50" fill="#4A4E69" stroke="{O}" stroke-width="2"/>
    <rect x="142" y="26" width="30" height="64" fill="#4A4E69" stroke="{O}" stroke-width="2"/>
    <path d="M136 26 H178" stroke="{O}" stroke-width="5"/>
    {lights}
    <rect x="0" y="0" width="200" height="90" fill="#ADB5BD" opacity=".35"/>
    <path d="M0 60 Q40 50 80 62 T160 58 T220 60" fill="none" stroke="#DEE2E6" stroke-width="7" opacity=".5"/>
    <rect x="0" y="90" width="200" height="50" fill="#495057"/>
    <path d="M0 114 H200" stroke="#fff" stroke-width="3" stroke-dasharray="14 10"/>
    <path d="M40 112 L56 100 H96 L112 94 H150 L158 104 L172 106 L172 116 H40Z" fill="#E63946" stroke="{O}" stroke-width="{SW}"/>
    <rect x="160" y="96" width="16" height="6" fill="#E63946" stroke="{O}" stroke-width="2"/>
    <path d="M28 98 H52 V104 H28Z" fill="#E63946" stroke="{O}" stroke-width="2"/>
    <circle cx="70" cy="118" r="11" fill="{O}"/><circle cx="70" cy="118" r="4" fill="#ADB5BD"/>
    <circle cx="148" cy="118" r="11" fill="{O}"/><circle cx="148" cy="118" r="4" fill="#ADB5BD"/>
    <circle cx="118" cy="98" r="5" fill="#FFD23F" stroke="{O}" stroke-width="1.6"/>
    <path d="M0 104 H24 M6 112 H26" stroke="#fff" stroke-width="2.5" opacity=".7"/>
    '''
    return _svg("0 0 200 140", b)


def lrt_train():
    b = f'''
    <rect width="200" height="140" fill="#BDE0FE"/>
    <circle cx="30" cy="26" r="12" fill="#FFD23F" stroke="{O}" stroke-width="2"/>
    <path d="M110 30 q10 -10 20 0 q10 -6 16 4 h-36Z" fill="#fff" stroke="{O}" stroke-width="2"/>
    <rect x="0" y="94" width="200" height="12" fill="#ADB5BD" stroke="{O}" stroke-width="{SW}"/>
    <rect x="40" y="106" width="14" height="34" fill="#CED4DA" stroke="{O}" stroke-width="2"/>
    <rect x="146" y="106" width="14" height="34" fill="#CED4DA" stroke="{O}" stroke-width="2"/>
    <path d="M26 92 V56 Q26 46 38 46 H150 Q172 46 176 70 L178 92Z" fill="#F8F9FA" stroke="{O}" stroke-width="{SW}"/>
    <rect x="26" y="76" width="152" height="8" fill="#06D6A0"/>
    <rect x="36" y="54" width="22" height="16" rx="3" fill="#4CC9F0" stroke="{O}" stroke-width="2"/>
    <rect x="64" y="54" width="22" height="16" rx="3" fill="#4CC9F0" stroke="{O}" stroke-width="2"/>
    <rect x="92" y="54" width="22" height="16" rx="3" fill="#4CC9F0" stroke="{O}" stroke-width="2"/>
    <rect x="120" y="54" width="22" height="16" rx="3" fill="#4CC9F0" stroke="{O}" stroke-width="2"/>
    <path d="M150 54 H160 Q170 56 172 70 H150Z" fill="#4CC9F0" stroke="{O}" stroke-width="2"/>
    <circle cx="170" cy="82" r="3" fill="#FFD23F" stroke="{O}" stroke-width="1.4"/>
    <path d="M184 60 h10 M186 70 h12 M184 80 h10" stroke="{O}" stroke-width="2.5"/>
    <g transform="rotate(10 100 26)"><rect x="56" y="12" width="88" height="24" rx="4" fill="#E63946" stroke="{O}" stroke-width="2.5"/>
    <text x="100" y="30" font-family="Bangers" font-size="15" text-anchor="middle" fill="#fff">14 DAYS EARLY!</text></g>
    '''
    return _svg("0 0 200 140", b)


def hockey():
    b = f'''
    <rect width="200" height="140" fill="#E0FBFC"/>
    <path d="M0 96 Q100 84 200 96 V140 H0Z" fill="#fff" stroke="{O}" stroke-width="2"/>
    <path d="M20 112 L60 110 M130 120 L180 116" stroke="#BDE0FE" stroke-width="3"/>
    <path d="M30 20 L92 104 Q98 112 110 110 L128 108" fill="none" stroke="{O}" stroke-width="10"/>
    <path d="M30 20 L92 104 Q98 112 110 110 L128 108" fill="none" stroke="#C68B59" stroke-width="5"/>
    <path d="M170 20 L108 104 Q102 112 90 110 L72 108" fill="none" stroke="{O}" stroke-width="10"/>
    <path d="M170 20 L108 104 Q102 112 90 110 L72 108" fill="none" stroke="#99D98C" stroke-width="5"/>
    <ellipse cx="100" cy="126" rx="18" ry="6" fill="{O}"/><rect x="82" y="118" width="36" height="8" fill="{O}"/>
    <ellipse cx="100" cy="118" rx="18" ry="6" fill="#495057" stroke="{O}" stroke-width="2"/>
    <rect x="66" y="8" width="68" height="34" rx="6" fill="#14213D" stroke="{O}" stroke-width="{SW}"/>
    <text x="100" y="34" font-family="Bangers" font-size="22" fill="#FFD23F" text-anchor="middle">6 - 1</text>
    <path d="M56 60 l-8 -6 M54 70 l-10 0 M144 60 l8 -6 M146 70 l10 0" stroke="#E63946" stroke-width="3"/>
    '''
    return _svg("0 0 200 140", b)


# --- leaves (for the leaf mission)

def leaf(kind, color):
    paths = {
        "maple": "M50 92 L50 74 L22 82 L28 70 L8 56 L22 52 L16 34 L34 42 L38 24 L50 40 L62 24 L66 42 L84 34 L78 52 L92 56 L72 70 L78 82 L50 74",
        "sweetgum": "M50 92 L50 70 L14 76 L36 58 L18 30 L44 46 L50 10 L56 46 L82 30 L64 58 L86 76 L50 70",
        "ginkgo": "M50 94 L50 64 L10 30 Q28 12 46 18 L50 32 L54 18 Q72 12 90 30 L50 64",
        "oak": "M50 94 L50 80 Q36 84 34 74 Q22 74 26 62 Q14 58 22 48 Q12 40 24 34 Q20 22 34 24 Q36 10 50 14 Q64 10 66 24 Q80 22 76 34 Q88 40 78 48 Q86 58 74 62 Q78 74 66 74 Q64 84 50 80",
        "birch": "M50 94 L50 78 Q20 72 24 42 Q32 18 50 8 Q68 18 76 42 Q80 72 50 78",
        "vinemaple": "M50 94 L50 72 Q24 76 18 60 Q8 50 16 40 Q14 26 28 24 Q34 10 50 14 Q66 10 72 24 Q86 26 84 40 Q92 50 82 60 Q76 76 50 72",
    }
    veins = '<path d="M50 74 L50 30 M50 60 L30 46 M50 60 L70 46" fill="none" stroke="#fff" stroke-width="2" opacity=".6"/>'
    b = f'<path d="{paths[kind]}" fill="{color}" stroke="{O}" stroke-width="{SW}"/>{veins}'
    return _svg("0 0 100 100", b, "leafart")


def opera_box():
    b = f'''
    <rect width="200" height="140" fill="#590D22"/>
    <path d="M0 0 H200 V18 Q150 30 100 18 Q50 30 0 18Z" fill="#C9184A" stroke="{O}" stroke-width="2"/>
    <path d="M0 0 Q30 70 10 140 H0Z M200 0 Q170 70 190 140 H200Z" fill="#C9184A" stroke="{O}" stroke-width="2"/>
    <path d="M40 140 V96 Q100 76 160 96 V140" fill="#FFB703" stroke="{O}" stroke-width="{SW}"/>
    <path d="M50 100 Q100 84 150 100" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="3 5"/>
    <text x="100" y="60" font-family="Bangers" font-size="22" fill="#FFD23F" text-anchor="middle">PARIS, 1858</text>
    <text x="100" y="128" font-size="34" text-anchor="middle" fill="{O}">&#9813;&#9818;&#9822;</text>
    '''
    return _svg("0 0 200 140", b)


def globe():
    b = f'''
    <rect width="140" height="140" fill="#CAF0F8"/>
    <circle cx="70" cy="70" r="52" fill="#4CC9F0" stroke="{O}" stroke-width="{SW}"/>
    <path d="M36 44 Q50 30 64 40 Q70 56 56 62 Q48 76 38 66 Q28 56 36 44Z M80 30 Q100 32 108 50 Q96 56 88 50 Q78 44 80 30Z M74 76 Q92 70 100 86 Q96 108 80 112 Q72 96 74 76Z"
      fill="#8AC926" stroke="{O}" stroke-width="2.5"/>
    <path d="M40 40 Q50 32 60 36" fill="none" stroke="#fff" stroke-width="3" opacity=".7"/>
    {_star(118, 20, 9)}
    '''
    return _svg("0 0 140 140", b)


def skyline_sg():
    b = f'''
    <rect width="200" height="140" fill="#FFCAD4"/>
    <circle cx="160" cy="34" r="18" fill="#FFB703" stroke="{O}" stroke-width="2"/>
    <rect x="0" y="0" width="200" height="140" fill="#CED4DA" opacity=".35"/>
    <rect x="20" y="64" width="18" height="46" fill="#6D597A" stroke="{O}" stroke-width="2"/>
    <rect x="44" y="50" width="20" height="60" fill="#B56576" stroke="{O}" stroke-width="2"/>
    <rect x="96" y="58" width="12" height="52" fill="#E56B6F" stroke="{O}" stroke-width="2"/>
    <rect x="116" y="58" width="12" height="52" fill="#E56B6F" stroke="{O}" stroke-width="2"/>
    <rect x="136" y="58" width="12" height="52" fill="#E56B6F" stroke="{O}" stroke-width="2"/>
    <path d="M90 58 H154 Q158 50 150 50 H96 Q88 50 90 58Z" fill="#355070" stroke="{O}" stroke-width="2"/>
    <rect x="164" y="74" width="22" height="36" fill="#6D597A" stroke="{O}" stroke-width="2"/>
    <rect x="0" y="110" width="200" height="30" fill="#4CC9F0" stroke="{O}" stroke-width="2"/>
    <path d="M10 124 Q30 118 50 124 M120 128 Q140 122 160 128" stroke="#fff" stroke-width="2.5" fill="none"/>
    '''
    return _svg("0 0 200 140", b)


def magnifier_fact():
    b = f'''<rect width="120" height="120" fill="#FFF3B0"/>
    <circle cx="52" cy="52" r="30" fill="#E0FBFC" stroke="{O}" stroke-width="{SW+1}"/>
    <path d="M74 74 L104 104" stroke="#8D5524" stroke-width="12"/>
    <text x="52" y="64" font-family="Bangers" font-size="34" text-anchor="middle" fill="#E63946">!</text>'''
    return _svg("0 0 120 120", b)


def dandiya():
    b = f'''
    <rect width="140" height="140" fill="#FFCCD5"/>
    <path d="M30 120 L104 26" stroke="{O}" stroke-width="10"/><path d="M30 120 L104 26" stroke="#E63946" stroke-width="5" stroke-dasharray="8 6"/>
    <path d="M110 120 L36 26" stroke="{O}" stroke-width="10"/><path d="M110 120 L36 26" stroke="#FFD23F" stroke-width="5" stroke-dasharray="8 6"/>
    <path d="M100 30 q12 -4 16 8 M40 30 q-12 -4 -16 8" fill="none" stroke="#06D6A0" stroke-width="4"/>
    {_star(70, 64, 12, "#fff")}{_star(22, 70, 6, "#9B5DE5")}{_star(120, 74, 6, "#4CC9F0")}
    '''
    return _svg("0 0 140 140", b)


def bow_arrow():
    b = f'''
    <rect width="140" height="140" fill="#FFF1C1"/>
    <path d="M44 14 Q110 70 44 126" fill="none" stroke="{O}" stroke-width="9"/>
    <path d="M44 14 Q110 70 44 126" fill="none" stroke="#8D5524" stroke-width="5"/>
    <path d="M44 14 L44 126" stroke="{O}" stroke-width="2"/>
    <path d="M30 70 L124 70" stroke="{O}" stroke-width="4"/>
    <path d="M124 70 L110 62 L110 78Z" fill="#E63946" stroke="{O}" stroke-width="2"/>
    <path d="M30 70 l-8 -8 M30 70 l-8 8 M38 70 l-8 -8 M38 70 l-8 8" stroke="#06D6A0" stroke-width="3"/>
    {_star(110, 26, 8)}
    '''
    return _svg("0 0 140 140", b)


def autumn_tree():
    import random
    rng = random.Random(7)
    dots = "".join(f'<circle cx="{rng.randint(40,160)}" cy="{rng.randint(20,80)}" r="{rng.randint(9,16)}" fill="{rng.choice(["#FFB703","#E63946","#FF8C42","#F4D35E","#9B2226"])}" stroke="{O}" stroke-width="2"/>' for _ in range(22))
    falling = "".join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="3" fill="{c}" stroke="{O}" stroke-width="1.4" transform="rotate({r} {x} {y})"/>'
                      for x, y, c, r in [(30, 100, "#E63946", 30), (170, 96, "#FFB703", -20), (150, 124, "#FF8C42", 50), (56, 126, "#F4D35E", -40)])
    b = f'''
    <rect width="200" height="140" fill="#CAF0F8"/>
    <rect x="0" y="122" width="200" height="18" fill="#8AC926" stroke="{O}" stroke-width="2"/>
    <path d="M92 124 L96 70 L80 52 M96 80 L114 58 M104 124 L102 70" stroke="{O}" stroke-width="3" fill="#8D5524"/>
    <path d="M90 124 L94 70 L106 70 L108 124Z" fill="#8D5524" stroke="{O}" stroke-width="{SW}"/>
    {dots}{falling}
    '''
    return _svg("0 0 200 140", b)


ILLUSTRATIONS = {
    "dandiya": dandiya, "bow_arrow": bow_arrow, "autumn_tree": autumn_tree,
    "rocket_iss": rocket_iss, "trophy_lab": trophy_lab, "brain_switch": brain_switch,
    "ice_neutrino": ice_neutrino, "mirror_hands": mirror_hands, "books": books,
    "mystery_box": mystery_box, "ai_chat": ai_chat, "sea_cucumber": sea_cucumber,
    "croc_sphinx": croc_sphinx, "gharial": gharial, "diya": diya, "kolu": kolu,
    "f1_night": f1_night, "lrt_train": lrt_train, "hockey": hockey,
    "opera_box": opera_box, "globe": globe, "skyline_sg": skyline_sg,
    "magnifier": magnifier_fact,
    "medal_med": lambda: medal("#E63946", "MED"), "medal_phy": lambda: medal("#118AB2", "PHY"),
    "medal_chem": lambda: medal("#06D6A0", "CHEM"), "medal_lit": lambda: medal("#9B5DE5", "LIT"),
    "medal": lambda: medal("#E63946", ""),
}


def illo(key):
    return ILLUSTRATIONS[key]()


def illo_bg(svg):
    """Background colour of a scene (its first full-size rect), used to fill
    any spare space around the picture so there are never white bars."""
    import re
    m = re.search(r'<rect width="\d+" height="\d+" fill="([^"]+)"', svg)
    return m.group(1) if m else "transparent"


# ================================================================ v2: icons + news illustrations
# Small round icons sit next to headlines and in brief lists, so every story
# has a picture even when space is tight. 40x40 viewBox, same ink style.

def _icon(bg, glyph):
    return _svg("0 0 40 40", f'<circle cx="20" cy="20" r="18" fill="{bg}" stroke="{O}" stroke-width="2.4"/>{glyph}', "icon")


_W = 'fill="#fff" stroke="#2B2140" stroke-width="1.8"'
ICONS = {
    "globe": ("#4CC9F0", f'<circle cx="20" cy="20" r="10" {_W}/><path d="M10 20h20M20 10q-6 10 0 20q6-10 0-20" fill="none" stroke="{O}" stroke-width="1.6"/>'),
    "oil": ("#2B2140", '<path d="M20 9 Q28 20 28 25 a8 8 0 0 1 -16 0 Q12 20 20 9Z" fill="#FFD23F" stroke="#fff" stroke-width="1.6"/>'),
    "ballot": ("#9B5DE5", f'<rect x="11" y="18" width="18" height="13" rx="2" {_W}/><path d="M15 18 L17 9 H25 L23 18" {_W}/><path d="M16 23h8" stroke="{O}" stroke-width="2"/>'),
    "virus": ("#06D6A0", f'<circle cx="20" cy="20" r="6.5" {_W}/>' + "".join(f'<path d="M{20+9*c:.1f} {20+9*s:.1f} L{20+6.5*c:.1f} {20+6.5*s:.1f}" stroke="{O}" stroke-width="2"/><circle cx="{20+10*c:.1f}" cy="{20+10*s:.1f}" r="1.8" fill="#fff" stroke="{O}" stroke-width="1.2"/>' for c, s in [(1,0),(-1,0),(0,1),(0,-1),(.7,.7),(-.7,.7),(.7,-.7),(-.7,-.7)])),
    "gavel": ("#C68B59", f'<rect x="12" y="11" width="14" height="7" rx="2" transform="rotate(-35 19 14)" {_W}/><path d="M21 18 L29 29" stroke="{O}" stroke-width="3.2"/><rect x="9" y="28" width="14" height="3" rx="1" {_W}/>'),
    "leaf": ("#8AC926", f'<path d="M11 29 Q10 12 29 11 Q30 28 11 29Z" {_W}/><path d="M12 28 L25 15" stroke="{O}" stroke-width="1.6"/>'),
    "ice": ("#BDE0FE", f'<path d="M20 9v22M10.5 14.5l19 11M29.5 14.5l-19 11" stroke="{O}" stroke-width="2.4"/><circle cx="20" cy="20" r="3" {_W}/>'),
    "rocket": ("#14213D", f'<path d="M20 8 Q27 14 26 24 H14 Q13 14 20 8Z" {_W}/><circle cx="20" cy="17" r="2.6" fill="#4CC9F0" stroke="{O}" stroke-width="1.2"/><path d="M16 25 L20 32 L24 25Z" fill="#FF8C42"/>'),
    "planet": ("#3A0CA3", f'<circle cx="20" cy="20" r="7" fill="#FFB703" stroke="#fff" stroke-width="1.6"/><ellipse cx="20" cy="20" rx="13" ry="4" fill="none" stroke="#fff" stroke-width="1.8" transform="rotate(-20 20 20)"/>'),
    "microscope": ("#E9D8FD", f'<path d="M17 9 L24 20" stroke="{O}" stroke-width="4"/><path d="M12 30 H28 M20 30 Q28 28 26 20" fill="none" stroke="{O}" stroke-width="2.4"/>'),
    "coin": ("#FFD23F", f'<circle cx="20" cy="20" r="9" fill="#FFB703" stroke="{O}" stroke-width="2"/><text x="20" y="24.5" font-family="Bangers" font-size="13" text-anchor="middle" fill="{O}">$</text>'),
    "rupee": ("#FF8C42", f'<circle cx="20" cy="20" r="9" fill="#FFD23F" stroke="{O}" stroke-width="2"/><path d="M15.5 14.5h9M15.5 18h9M17 14.5 q7 0 4 6 h-4 l6 6" fill="none" stroke="{O}" stroke-width="1.8"/>'),
    "chart": ("#06D6A0", f'<path d="M11 28 L17 20 L22 24 L29 12" fill="none" stroke="#fff" stroke-width="3"/><path d="M29 12 l-5 1 M29 12 l0 5" stroke="#fff" stroke-width="3"/>'),
    "chartdown": ("#EF476F", f'<path d="M11 12 L17 20 L22 16 L29 28" fill="none" stroke="#fff" stroke-width="3"/><path d="M29 28 l-5 -1 M29 28 l0 -5" stroke="#fff" stroke-width="3"/>'),
    "chip": ("#343A40", f'<rect x="13" y="13" width="14" height="14" rx="2" fill="#2EC4B6" stroke="#fff" stroke-width="1.6"/><path d="M16 13v-4M20 13v-4M24 13v-4M16 31v-4M20 31v-4M24 31v-4M13 16h-4M13 20h-4M13 24h-4M31 16h-4M31 20h-4M31 24h-4" stroke="#fff" stroke-width="1.6"/>'),
    "lock": ("#E63946", f'<rect x="12" y="19" width="16" height="12" rx="2" {_W}/><path d="M15 19 v-4 a5 5 0 0 1 10 0 v4" fill="none" stroke="#fff" stroke-width="2.4"/>'),
    "car": ("#4CC9F0", f'<path d="M9 25 L12 18 H27 L31 25 V28 H9Z" {_W}/><circle cx="14" cy="28.5" r="2.6" fill="{O}"/><circle cx="26" cy="28.5" r="2.6" fill="{O}"/>'),
    "cricket": ("#8AC926", f'<rect x="17" y="8" width="5" height="20" rx="2" transform="rotate(30 20 18)" fill="#F4D35E" stroke="{O}" stroke-width="1.6"/><circle cx="27" cy="27" r="3.6" fill="#E63946" stroke="{O}" stroke-width="1.4"/>'),
    "chess": ("#FF9F1C", f'<path d="M14 31 H26 L24 27 H16Z M17 27 L18 17 H22 L23 27 M16 17 h8 M20 9 v6 M17 12 h6" fill="#fff" stroke="{O}" stroke-width="1.8"/>'),
    "storm": ("#577590", f'<path d="M20 10 a10 10 0 1 0 8 4" fill="none" stroke="#fff" stroke-width="2.6"/><path d="M20 30 a10 10 0 1 0 -8 -4" fill="none" stroke="#fff" stroke-width="2.6"/><circle cx="20" cy="20" r="2.4" fill="#fff"/>'),
    "whale": ("#118AB2", f'<path d="M8 22 Q12 13 23 15 Q31 16 32 21 L35 17 L35 27 L31 24 Q27 29 17 28 Q9 27 8 22Z" fill="#2B2140" stroke="#fff" stroke-width="1.4"/><ellipse cx="17" cy="24" rx="4" ry="2" fill="#fff"/>'),
    "ship": ("#48CAE4", f'<path d="M8 24 H32 L28 30 H12Z" {_W}/><rect x="14" y="16" width="10" height="8" {_W}/><path d="M17 16 V11" stroke="{O}" stroke-width="2"/>'),
    "train": ("#06D6A0", f'<rect x="12" y="10" width="16" height="17" rx="3" {_W}/><rect x="14.5" y="13" width="11" height="6" rx="1" fill="#4CC9F0"/><path d="M14 31 l3 -4 M26 31 l-3 -4" stroke="#fff" stroke-width="2"/>'),
    "haze": ("#ADB5BD", f'<path d="M9 16 h18 M12 21 h20 M8 26 h18" stroke="#fff" stroke-width="3"/><circle cx="28" cy="13" r="4" fill="#FFB703" opacity=".7"/>'),
    "flood": ("#3A86FF", f'<path d="M8 20 q4 -4 8 0 t8 0 t8 0 M8 27 q4 -4 8 0 t8 0 t8 0" fill="none" stroke="#fff" stroke-width="2.6"/><path d="M14 14 l6 -5 l6 5" fill="none" stroke="#fff" stroke-width="2.2"/>'),
    "satellite": ("#14213D", f'<rect x="17" y="17" width="6" height="6" fill="#ADB5BD" stroke="#fff" stroke-width="1.2"/><rect x="7" y="17.5" width="9" height="5" fill="#4CC9F0" stroke="#fff" stroke-width="1.2"/><rect x="24" y="17.5" width="9" height="5" fill="#4CC9F0" stroke="#fff" stroke-width="1.2"/>'),
    "medal": ("#FFD23F", f'<path d="M15 9 L19 19 M25 9 L21 19" stroke="#E63946" stroke-width="3"/><circle cx="20" cy="24" r="7" fill="#FFB703" stroke="{O}" stroke-width="2"/>'),
    "flag": ("#EF476F", f'<path d="M13 31 V9" stroke="{O}" stroke-width="2.4"/><path d="M13 10 H28 L24 15 L28 20 H13" {_W}/>'),
    "hospital": ("#fff", f'<path d="M17 11h6v6h6v6h-6v6h-6v-6h-6v-6h6z" fill="#E63946" stroke="{O}" stroke-width="1.6"/>'),
    "fire": ("#FF8C42", f'<path d="M20 9 Q28 18 26 24 a6 6 0 0 1 -12 0 Q13 19 18 15 Q18 20 21 21 Q22 15 20 9Z" fill="#FFD23F" stroke="{O}" stroke-width="1.6"/>'),
    "book": ("#9B5DE5", f'<path d="M10 12 Q15 10 20 13 Q25 10 30 12 V28 Q25 26 20 29 Q15 26 10 28Z" {_W}/><path d="M20 13 V29" stroke="{O}" stroke-width="1.6"/>'),
    "bone": ("#F4D35E", f'<path d="M13 15 l14 10" stroke="#fff" stroke-width="5"/><circle cx="12" cy="13" r="3" fill="#fff"/><circle cx="15" cy="11" r="3" fill="#fff"/><circle cx="28" cy="27" r="3" fill="#fff"/><circle cx="25" cy="29" r="3" fill="#fff"/>'),
    "bear": ("#8D5524", f'<circle cx="13" cy="13" r="4" fill="#C68B59" stroke="#fff" stroke-width="1.4"/><circle cx="27" cy="13" r="4" fill="#C68B59" stroke="#fff" stroke-width="1.4"/><circle cx="20" cy="21" r="9" fill="#C68B59" stroke="#fff" stroke-width="1.6"/><circle cx="17" cy="19" r="1.4" fill="{O}"/><circle cx="23" cy="19" r="1.4" fill="{O}"/><ellipse cx="20" cy="24" rx="3" ry="2" fill="{O}"/>'),
    "tortoise": ("#8AC926", f'<path d="M9 26 Q11 14 20 14 Q29 14 31 26Z" fill="#6A994E" stroke="{O}" stroke-width="1.8"/><circle cx="32" cy="23" r="3" fill="#A7C957" stroke="{O}" stroke-width="1.4"/><path d="M14 20 h12 M20 14 v12" stroke="{O}" stroke-width="1.2"/>'),
    "hockey": ("#E0FBFC", f'<path d="M13 9 L21 27 H28" fill="none" stroke="{O}" stroke-width="3"/><ellipse cx="14" cy="28" rx="4" ry="2" fill="{O}"/>'),
    "football": ("#43AA8B", f'<ellipse cx="20" cy="20" rx="11" ry="7" transform="rotate(-30 20 20)" fill="#8D5524" stroke="#fff" stroke-width="1.6"/><path d="M16 23 L24 17 M18 19 l2 2 M20 18 l2 2" stroke="#fff" stroke-width="1.4"/>'),
    "tennis": ("#C0F03B", f'<circle cx="20" cy="20" r="9" fill="#E9FF70" stroke="{O}" stroke-width="1.8"/><path d="M12 15 Q20 20 12 26 M28 15 Q20 20 28 26" fill="none" stroke="#fff" stroke-width="1.8"/>'),
    "racecar": ("#E63946", f'<path d="M8 25 L13 20 H24 L28 18 H32 V25Z" {_W}/><circle cx="14" cy="26" r="3" fill="{O}"/><circle cx="28" cy="26" r="3" fill="{O}"/>'),
    "baseball": ("#fff", f'<circle cx="20" cy="20" r="9" fill="#fff" stroke="{O}" stroke-width="1.8"/><path d="M14 13 Q18 20 14 27 M26 13 Q22 20 26 27" fill="none" stroke="#E63946" stroke-width="1.6"/>'),
    "temple": ("#FFB703", f'<path d="M12 30 H28 M13 30 V18 M27 30 V18 M20 9 L30 17 H10Z M17 30 V18 M23 30 V18" fill="#fff" stroke="{O}" stroke-width="1.8"/>'),
    "people": ("#FF8FAB", f'<circle cx="15" cy="15" r="3.4" {_W}/><circle cx="25" cy="15" r="3.4" {_W}/><path d="M9 29 q6 -10 12 0 M19 29 q6 -10 12 0" {_W}/>'),
    "school": ("#FFD23F", f'<path d="M9 18 L20 11 L31 18 L20 25Z" {_W}/><path d="M14 21 V27 Q20 31 26 27 V21" fill="none" stroke="{O}" stroke-width="1.8"/>'),
    "bolt": ("#FFD23F", f'<path d="M22 8 L13 22 H19 L17 32 L27 17 H21Z" fill="#fff" stroke="{O}" stroke-width="1.6"/>'),
    "sun": ("#FF8C42", '<circle cx="20" cy="20" r="6" fill="#FFD23F" stroke="#fff" stroke-width="1.6"/>' + "".join(f'<path d="M{20+9*c:.1f} {20+9*s:.1f} L{20+12*c:.1f} {20+12*s:.1f}" stroke="#fff" stroke-width="2"/>' for c, s in [(1,0),(-1,0),(0,1),(0,-1),(.7,.7),(-.7,.7),(.7,-.7),(-.7,-.7)])),
    "peace": ("#4CC9F0", f'<path d="M12 22 Q14 13 22 14 Q30 15 29 20 L33 18 L29 23 Q25 28 17 26 Z" {_W}/><path d="M28 21 Q32 26 30 29" fill="none" stroke="#8AC926" stroke-width="2"/>'),
}


def icon(key):
    bg, g = ICONS[key]
    return _icon(bg, g)


def hormuz_map():
    b = f'''
    <rect width="200" height="140" fill="#90E0EF"/>
    <path d="M0 0 H200 V52 Q170 46 150 58 Q128 70 112 62 Q96 54 82 58 Q60 64 40 48 Q20 36 0 40Z" fill="#E9C46A" stroke="{O}" stroke-width="{SW}"/>
    <path d="M200 140 V90 Q176 82 150 96 Q132 104 120 84 Q110 70 98 76 Q86 84 70 92 Q40 106 0 98 V140Z" fill="#F4A261" stroke="{O}" stroke-width="{SW}"/>
    <text x="40" y="24" font-family="Bangers" font-size="18" fill="{O}">IRAN</text>
    <text x="146" y="128" font-family="Bangers" font-size="15" fill="{O}">OMAN</text>
    <text x="26" y="86" font-family="Bangers" font-size="11" fill="#03045E">PERSIAN GULF</text>
    <path d="M104 64 L104 76" stroke="#E63946" stroke-width="3" stroke-dasharray="3 3"/>
    <text x="96" y="58" font-family="Bangers" font-size="11" fill="#E63946" transform="rotate(-8 96 58)">STRAIT OF HORMUZ</text>
    <g transform="translate(60 72)"><path d="M0 0 H24 L20 6 H4Z" fill="#E63946" stroke="{O}" stroke-width="2"/><rect x="5" y="-5" width="7" height="5" fill="#fff" stroke="{O}" stroke-width="1.5"/></g>
    <g transform="translate(140 72)"><path d="M0 0 H24 L20 6 H4Z" fill="#118AB2" stroke="{O}" stroke-width="2"/><rect x="12" y="-5" width="7" height="5" fill="#fff" stroke="{O}" stroke-width="1.5"/></g>
    <text x="18" y="122" font-family="Bangers" font-size="11" fill="{O}">1/5 OF THE WORLD'S OIL</text>
    '''
    return _svg("0 0 200 140", b)


def haze_city():
    b = skyline_sg().split(">", 1)[1].rsplit("</svg>", 1)[0]
    b += f'''<rect width="200" height="140" fill="#9AA0A6" opacity=".45"/>
    <path d="M0 40 Q50 30 100 44 T200 38 M0 70 Q60 58 120 72 T220 66 M0 98 Q40 90 90 100 T200 94" fill="none" stroke="#DEE2E6" stroke-width="9" opacity=".75"/>
    <rect x="132" y="8" width="62" height="30" rx="6" fill="#E63946" stroke="{O}" stroke-width="2.5"/>
    <text x="163" y="22" font-family="Bangers" font-size="11" fill="#fff" text-anchor="middle">PSI</text>
    <text x="163" y="34" font-family="Bangers" font-size="13" fill="#fff" text-anchor="middle">159</text>'''
    return _svg("0 0 200 140", b)


def ballot_box(bg="#E9D8FD", label="VOTE"):
    b = f'''
    <rect width="200" height="140" fill="{bg}"/>
    <rect x="60" y="56" width="80" height="62" rx="6" fill="#fff" stroke="{O}" stroke-width="{SW}"/>
    <rect x="84" y="56" width="32" height="5" fill="{O}"/>
    <path d="M86 58 L92 18 H120 L114 58" fill="#FFF3B0" stroke="{O}" stroke-width="{SW}"/>
    <path d="M96 30 l6 6 l12 -12" fill="none" stroke="#06A77D" stroke-width="4"/>
    <text x="100" y="98" font-family="Bangers" font-size="22" text-anchor="middle" fill="#E63946">{label}</text>
    {_star(34, 34, 10, "#FFD23F")}{_star(170, 40, 8, "#4CC9F0")}{_star(160, 112, 6, "#FF8FAB")}
    '''
    return _svg("0 0 200 140", b)


def hurricane():
    b = f'''
    <rect width="200" height="140" fill="#14213D"/>
    <path d="M0 110 Q60 96 110 112 Q150 124 200 108 V140 H0Z" fill="#06D6A0" stroke="{O}" stroke-width="2"/>
    <g transform="translate(110 58)">
      <path d="M0 -40 A40 40 0 0 1 40 0" fill="none" stroke="#fff" stroke-width="9" opacity=".9"/>
      <path d="M0 40 A40 40 0 0 1 -40 0" fill="none" stroke="#fff" stroke-width="9" opacity=".9"/>
      <path d="M-26 -26 A26 26 0 0 1 26 -10" fill="none" stroke="#BDE0FE" stroke-width="7"/>
      <path d="M26 26 A26 26 0 0 1 -26 10" fill="none" stroke="#BDE0FE" stroke-width="7"/>
      <circle r="7" fill="#14213D" stroke="#fff" stroke-width="2"/>
    </g>
    <text x="12" y="130" font-family="Bangers" font-size="14" fill="#14213D">GULF COAST</text>
    <text x="12" y="24" font-family="Bangers" font-size="16" fill="#FFD23F">ISAIAS</text>
    '''
    return _svg("0 0 200 140", b)


def orca():
    b = f'''
    <rect width="200" height="140" fill="#90E0EF"/>
    <path d="M0 50 Q50 42 100 50 T200 50 V140 H0Z" fill="#0077B6" stroke="{O}" stroke-width="2"/>
    <path d="M30 92 Q46 64 96 66 Q140 66 160 84 L184 70 L178 96 L190 112 L160 102 Q130 120 80 116 Q40 114 30 92Z" fill="#14213D" stroke="{O}" stroke-width="{SW}"/>
    <path d="M92 66 L104 34 L112 66Z" fill="#14213D" stroke="{O}" stroke-width="{SW}"/>
    <ellipse cx="62" cy="80" rx="9" ry="5" fill="#fff"/>
    <path d="M44 100 Q80 112 120 104 Q90 116 52 106Z" fill="#fff"/>
    <path d="M60 30 q8 -8 16 0 q8 -8 16 0" fill="none" stroke="#fff" stroke-width="2.5"/>
    <text x="112" y="30" font-family="Bangers" font-size="15" fill="{O}">ONLY 76 LEFT</text>
    '''
    return _svg("0 0 200 140", b)


def oil_gauge():
    b = f'''
    <rect width="200" height="140" fill="#FFF1C1"/>
    <rect x="22" y="30" width="56" height="86" rx="10" fill="#2B2140" stroke="{O}" stroke-width="{SW}"/>
    <path d="M22 54 H78 M22 92 H78" stroke="#FFD23F" stroke-width="4"/>
    <text x="50" y="80" font-family="Bangers" font-size="16" fill="#FFD23F" text-anchor="middle">OIL</text>
    <path d="M96 116 L120 86 L140 96 L176 36" fill="none" stroke="#E63946" stroke-width="6"/>
    <path d="M176 36 l-14 2 M176 36 l-2 14" stroke="#E63946" stroke-width="6"/>
    <text x="130" y="30" font-family="Bangers" font-size="20" fill="{O}">$105</text>
    <text x="96" y="132" font-family="Bangers" font-size="13" fill="{O}">BEFORE WAR: $72</text>
    '''
    return _svg("0 0 200 140", b)


def cricket_bat():
    b = f'''
    <rect width="200" height="140" fill="#D8F3DC"/>
    <ellipse cx="100" cy="132" rx="110" ry="30" fill="#8AC926" stroke="{O}" stroke-width="2"/>
    <g transform="rotate(-30 100 70)"><rect x="90" y="22" width="22" height="80" rx="6" fill="#F4D35E" stroke="{O}" stroke-width="{SW}"/>
    <rect x="96" y="-6" width="10" height="30" rx="3" fill="#E63946" stroke="{O}" stroke-width="{SW}"/></g>
    <circle cx="150" cy="44" r="12" fill="#E63946" stroke="{O}" stroke-width="{SW}"/><path d="M140 40 Q150 48 160 40" fill="none" stroke="#fff" stroke-width="2"/>
    <text x="16" y="34" font-family="Bangers" font-size="26" fill="#E63946" stroke="{O}" stroke-width=".8">102*</text>
    <path d="M150 70 v40 M160 70 v40 M140 70 v40 M136 70 h28" stroke="{O}" stroke-width="3"/>
    '''
    return _svg("0 0 200 140", b)


def moon_view():
    stars = "".join(_star(x, y, r, "#FFF3B0", stroke=False) for x, y, r in [(20, 20, 3), (180, 30, 4), (60, 120, 3), (170, 110, 3), (110, 14, 2.5)])
    b = f'''
    <rect width="200" height="140" fill="#0B132B"/>{stars}
    <circle cx="100" cy="74" r="44" fill="#ADB5BD" stroke="{O}" stroke-width="{SW}"/>
    <circle cx="84" cy="60" r="8" fill="#868E96"/><circle cx="116" cy="88" r="11" fill="#868E96"/><circle cx="108" cy="54" r="5" fill="#6C9BD2" opacity=".7"/>
    <circle cx="70" cy="90" r="3" fill="#FFD23F"/><circle cx="126" cy="64" r="2.5" fill="#FFD23F"/><circle cx="96" cy="100" r="2.5" fill="#FFD23F"/>
    <text x="10" y="134" font-family="Bangers" font-size="12" fill="#FFD23F">5 TINY FLASHES = METEORITE HITS</text>
    '''
    return _svg("0 0 200 140", b)


ILLUSTRATIONS.update({
    "hormuz_map": hormuz_map, "haze_city": haze_city, "ballot_box": ballot_box,
    "ballot_brazil": lambda: ballot_box("#B7E4C7", "BRAZIL"), "ballot_us": lambda: ballot_box("#CAF0F8", "NOV 3"),
    "hurricane": hurricane, "orca": orca, "oil_gauge": oil_gauge, "cricket_bat": cricket_bat,
    "moon_view": moon_view,
})
