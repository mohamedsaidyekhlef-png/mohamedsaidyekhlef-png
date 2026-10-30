"""Generates every SVG on the profile in light and dark. Run: python3 scripts/make_assets.py"""
import math, random

FONT = "Schibsted Grotesk, Inter, -apple-system, Segoe UI, Helvetica, Arial, sans-serif"
THEMES = {
    "dark": dict(bg="#0F1420", panel="#151C2B", ink="#EEF1F6", muted="#93A0B4", line="#2A3448",
                 blue="#5B8CFF", green="#34C38F", amber="#F2B63A", rose="#FF6B7A", violet="#A78BFA"),
    "light": dict(bg="#F6F7FA", panel="#FFFFFF", ink="#141B2A", muted="#566175", line="#D5DBE5",
                  blue="#2F5BEA", green="#14935F", amber="#C98A06", rose="#D3263A", violet="#6D4AE0"),
}
MOTION = """<style>
.pulse{animation:p 2.6s ease-in-out infinite}.flow{stroke-dasharray:6 8;animation:f 1.6s linear infinite}
.d2{animation-delay:.9s}.d3{animation-delay:1.7s}
@keyframes p{0%,100%{opacity:1}50%{opacity:.35}}@keyframes f{to{stroke-dashoffset:-28}}
@media (prefers-reduced-motion:reduce){.pulse,.flow{animation:none}}
</style>"""

def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;")

def write(name, theme, body, w, h, label):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(label)}">'
           f'{MOTION}<rect width="{w}" height="{h}" rx="18" fill="{THEMES[theme]["bg"]}"/>{body}</svg>')
    open(f"assets/{name}-{theme}.svg", "w").write(svg)

# ── Banner ────────────────────────────────────────────────────────────────
def banner(t, c):
    random.seed(11); cx, cy = 1010, 180
    nodes = [(cx + (110 + random.randint(-12, 12)) * math.cos(-math.pi/2 + i*2*math.pi/7),
              cy + (110 + random.randint(-12, 12)) * 0.78 * math.sin(-math.pi/2 + i*2*math.pi/7)) for i in range(7)]
    outer = [(cx + (190 + random.randint(-10, 14)) * math.cos(-math.pi/2 + i*2*math.pi/10 + .3),
              cy + (190 + random.randint(-10, 14)) * 0.62 * math.sin(-math.pi/2 + i*2*math.pi/10 + .3)) for i in range(10)]
    g = []
    for k, (x, y) in enumerate(nodes):
        act = k in (1, 4, 6)
        g.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="{c["blue"] if act else c["line"]}" stroke-width="{2.4 if act else 1.2}"'
                 + (f' class="flow{" d2" if k == 4 else " d3" if k == 6 else ""}"' if act else "") + "/>")
    for j, (x, y) in enumerate(outer):
        bx, by = min(nodes, key=lambda n: (n[0]-x)**2 + (n[1]-y)**2)
        g.append(f'<line x1="{bx:.1f}" y1="{by:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="{c["line"]}" stroke-width="1.2"/>')
        g.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{c["line"]}"/>')
    colors = {1: c["blue"], 3: c["green"], 4: c["amber"], 6: c["violet"]}
    for k, (x, y) in enumerate(nodes):
        fill = colors.get(k, c["bg"])
        cls = ' class="pulse"' if k in colors else ""
        g.append(f'<circle{cls} cx="{x:.1f}" cy="{y:.1f}" r="9" fill="{fill}" stroke="{fill if k in colors else c["muted"]}" stroke-width="2"/>')
    g.append(f'<circle cx="{cx}" cy="{cy}" r="17" fill="{c["ink"]}"/><circle cx="{cx}" cy="{cy}" r="6" fill="{c["bg"]}"/>')
    body = (f'<g transform="translate(1110 180) scale(0.7) translate(-1010 -180)">{"".join(g)}</g>'
            f'<g font-family="{FONT}">'
            f'<text x="64" y="112" font-size="66" font-weight="800" letter-spacing="-1.4" fill="{c["ink"]}">Mohamed Said Yekhlef</text>'
            f'<text x="64" y="172" font-size="34" font-weight="500" fill="{c["ink"]}">AI engineer · Senior GEO expert · Finance analyst</text>'
            f'<text x="64" y="220" font-size="22" fill="{c["muted"]}">Founder · SettlementDecisions · Surplus Clock · AuthorsPack</text>'
            f'<text x="64" y="300" font-size="22" fill="{c["muted"]}">Tetouan, Morocco  ·  العربية · Français · English</text></g>')
    write("banner", t, body, 1280, 360, "Mohamed Said Yekhlef. AI engineer, senior GEO expert and finance analyst. Founder of SettlementDecisions, Surplus Clock and AuthorsPack.")

# ── Three skills ──────────────────────────────────────────────────────────
def skills(t, c):
    W, H, R = 1280, 600, 150
    A, G, F = (560, 235), (720, 235), (640, 375)
    b = []
    for (x, y), col in ((A, c["blue"]), (G, c["green"]), (F, c["amber"])):
        b.append(f'<circle cx="{x}" cy="{y}" r="{R}" fill="{col}" fill-opacity="0.12" stroke="{col}" stroke-width="2.5"/>')
    # Titles outside the circles, anchored to the canvas edges they face
    b.append(f'<text x="64" y="120" font-size="34" font-weight="800" fill="{c["blue"]}">AI engineering</text>'
             f'<text x="64" y="156" font-size="20" fill="{c["muted"]}">Agents · automation</text>'
             f'<text x="64" y="184" font-size="20" fill="{c["muted"]}">fine-tuned models</text>')
    b.append(f'<text x="1216" y="120" text-anchor="end" font-size="34" font-weight="800" fill="{c["green"]}">GEO</text>'
             f'<text x="1216" y="156" text-anchor="end" font-size="20" fill="{c["muted"]}">Found and cited</text>'
             f'<text x="1216" y="184" text-anchor="end" font-size="20" fill="{c["muted"]}">in AI answers</text>')
    b.append(f'<text x="1216" y="470" text-anchor="end" font-size="34" font-weight="800" fill="{c["amber"]}">Finance</text>'
             f'<text x="1216" y="506" text-anchor="end" font-size="20" fill="{c["muted"]}">Cash flows · valuation</text>'
             f'<text x="1216" y="534" text-anchor="end" font-size="20" fill="{c["muted"]}">risk</text>')
    # Connector ticks from titles to circles
    b.append(f'<line x1="300" y1="140" x2="440" y2="170" stroke="{c["blue"]}" stroke-width="1.5" stroke-dasharray="4 5"/>')
    b.append(f'<line x1="1050" y1="140" x2="850" y2="170" stroke="{c["green"]}" stroke-width="1.5" stroke-dasharray="4 5"/>')
    b.append(f'<line x1="1050" y1="490" x2="770" y2="440" stroke="{c["amber"]}" stroke-width="1.5" stroke-dasharray="4 5"/>')
    # Pair overlaps
    b.append(f'<text x="640" y="160" text-anchor="middle" font-size="17" font-weight="600" fill="{c["ink"]}">AI that</text>'
             f'<text x="640" y="182" text-anchor="middle" font-size="17" font-weight="600" fill="{c["ink"]}">gets cited</text>')
    b.append(f'<text x="566" y="352" text-anchor="middle" font-size="17" font-weight="600" fill="{c["ink"]}">Models that</text>'
             f'<text x="566" y="374" text-anchor="middle" font-size="17" font-weight="600" fill="{c["ink"]}">price risk</text>')
    b.append(f'<text x="714" y="352" text-anchor="middle" font-size="17" font-weight="600" fill="{c["ink"]}">Traffic that</text>'
             f'<text x="714" y="374" text-anchor="middle" font-size="17" font-weight="600" fill="{c["ink"]}">pays for itself</text>')
    b.append(f'<circle class="pulse" cx="640" cy="272" r="40" fill="{c["ink"]}"/>'
             f'<text x="640" y="278" text-anchor="middle" font-size="17" font-weight="800" fill="{c["bg"]}">Founder</text>')
    write("skills", t, f'<g font-family="{FONT}">{"".join(b)}</g>', W, H,
          "Three overlapping skills: AI engineering, GEO and finance. AI that gets cited, models that price risk, traffic that pays for itself. Where all three meet: founder.")

# ── Cards ─────────────────────────────────────────────────────────────────
def card(t, c, name, title, line1, line2, tags, domain, motif, accent):
    W, H = 1280, 300
    tag_svg, x = [], 470
    for tg in tags:
        w = 16 + len(tg) * 10.2
        tag_svg.append(f'<rect x="{x}" y="196" width="{w:.0f}" height="34" rx="17" fill="none" stroke="{c["line"]}" stroke-width="1.5"/>'
                       f'<text x="{x + w/2:.0f}" y="219" text-anchor="middle" font-size="17" fill="{c["muted"]}">{esc(tg)}</text>')
        x += w + 10
    body = (f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="none" stroke="{c["line"]}" stroke-width="2"/>'
            f'<rect x="0" y="0" width="420" height="{H}" rx="18" fill="{accent}" fill-opacity="0.08"/>{motif}'
            f'<g font-family="{FONT}"><text x="470" y="88" font-size="40" font-weight="800" letter-spacing="-.6" fill="{c["ink"]}">{esc(title)}</text>'
            f'<text x="470" y="130" font-size="22" fill="{c["ink"]}">{esc(line1)}</text>'
            f'<text x="470" y="162" font-size="22" fill="{c["muted"]}">{esc(line2)}</text>{"".join(tag_svg)}'
            f'<text x="{W-48}" y="88" text-anchor="end" font-size="18" font-weight="600" fill="{accent}">{esc(domain)} ↗</text></g>')
    write(name, t, body, W, H, f"{title}: {line1} {line2}")

def settlement_motif(c):
    # many small future payments flowing into one lump sum today
    s = []
    for i in range(9):
        x = 60 + i * 26; h = 34
        s.append(f'<rect x="{x}" y="{170 - h}" width="16" height="{h}" rx="3" fill="{c["blue"]}" fill-opacity="{0.35 + i*0.05:.2f}"/>')
    s.append(f'<path class="flow" d="M300 150 C 320 150, 320 150, 340 150" stroke="{c["blue"]}" stroke-width="3" fill="none"/>')
    s.append(f'<rect class="pulse" x="345" y="70" width="40" height="100" rx="5" fill="{c["blue"]}"/>')
    s.append(f'<line x1="50" y1="180" x2="390" y2="180" stroke="{c["line"]}" stroke-width="2"/>')
    s.append(f'<text x="60" y="210" font-family="{FONT}" font-size="15" fill="{c["muted"]}">payments over years</text>'
             f'<text x="388" y="210" text-anchor="end" font-family="{FONT}" font-size="15" fill="{c["muted"]}">value today</text>')
    return "".join(s)

def surplus_motif(c):
    cx, cy, r = 210, 140, 82
    s = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c["green"]}" stroke-width="5"/>']
    for i in range(12):
        a = i * math.pi / 6
        s.append(f'<line x1="{cx + (r-10)*math.cos(a):.1f}" y1="{cy + (r-10)*math.sin(a):.1f}" x2="{cx + (r-2)*math.cos(a):.1f}" y2="{cy + (r-2)*math.sin(a):.1f}" stroke="{c["muted"]}" stroke-width="3"/>')
    s.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-55}" stroke="{c["ink"]}" stroke-width="6" stroke-linecap="round"/>')
    s.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+40}" y2="{cy+18}" stroke="{c["green"]}" stroke-width="5" stroke-linecap="round" class="pulse"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="8" fill="{c["ink"]}"/>')
    s.append(f'<text x="{cx}" y="262" text-anchor="middle" font-family="{FONT}" font-size="15" fill="{c["muted"]}">surplus funds have a deadline</text>')
    return "".join(s)

def authors_motif(c):
    cols = [c["violet"], c["blue"], c["amber"], c["green"], c["rose"], c["violet"], c["blue"]]
    hs = [150, 120, 165, 135, 110, 155, 125]
    s, x = [], 70
    for col, h, wdt in zip(cols, hs, [34, 28, 40, 30, 26, 36, 30]):
        s.append(f'<rect x="{x}" y="{210-h}" width="{wdt}" height="{h}" rx="3" fill="{col}" fill-opacity="0.85"/>'
                 f'<rect x="{x+6}" y="{220-h}" width="{wdt-12}" height="4" rx="2" fill="{c["bg"]}" fill-opacity="0.6"/>')
        x += wdt + 6
    s.append(f'<line x1="56" y1="212" x2="{x+8}" y2="212" stroke="{c["muted"]}" stroke-width="3"/>')
    s.append(f'<text x="210" y="262" text-anchor="middle" font-family="{FONT}" font-size="15" fill="{c["muted"]}">manuscript in, book out</text>')
    return "".join(s)

def diffplay_motif(c):
    random.seed(7); s = []; x = 50
    hot = {6: c["rose"], 7: c["rose"], 15: c["amber"], 22: c["rose"], 27: c["amber"]}
    for i in range(32):
        col = hot.get(i, c["green"] if random.random() > .25 else c["rose"])
        op = 1 if i in hot else 0.35
        h = 110 if i in hot and hot[i] == c["rose"] else 90 if i in hot else 70
        s.append(f'<rect{" class=\"pulse\"" if i in hot else ""} x="{x}" y="{140 - h/2}" width="7" height="{h}" rx="2" fill="{col}" fill-opacity="{op}"/>')
        x += 10
    s.append(f'<text x="210" y="262" text-anchor="middle" font-family="{FONT}" font-size="15" fill="{c["muted"]}">every changed line, risk lit up</text>')
    return "".join(s)

for t, c in THEMES.items():
    banner(t, c); skills(t, c)
    card(t, c, "card-settlement", "SettlementDecisions", "Structured settlement payments, made clear.",
         "Options explained, funding partners matched.", ["Fine-tuned LLM", "Lead qualification", "Finance"],
         "settlementdecisions.com", settlement_motif(c), c["blue"])
    card(t, c, "card-surplus", "Surplus Clock", "Florida tax deed surplus research.",
         "For recovery firms, attorneys and lienholders.", ["Research automation", "Public records", "Legal finance"],
         "surplusclock.com", surplus_motif(c), c["green"])
    card(t, c, "card-authors", "AuthorsPack", "AI publishing production.",
         "Formatting, editing, QA and publishing-ready files.", ["Agent pipelines", "Typesetting", "Publishing"],
         "authorspack.com", authors_motif(c), c["violet"])
    card(t, c, "card-diffplay", "diffplay", "Review AI-written pull requests in minutes.",
         "Open source. Story-ordered steps, risky lines lit up.", ["TypeScript", "GitHub Action", "MIT"],
         "github.com/…/diffplay", diffplay_motif(c), c["rose"])
print("assets written")
