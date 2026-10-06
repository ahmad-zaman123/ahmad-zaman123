#!/usr/bin/env python3
"""
Render the `whoami` terminal card (840 x 880, same canvas as stats.svg so the
two sit side by side in the README at 420px each).

Each line is revealed with a left-to-right clip wipe, top to bottom, like a
terminal printing. GitHub runs SMIL inside <img> SVGs but never JS, so the
animation is pure SMIL. Edit LINES below and re-run to update the card:

    python scripts/render_whoami_svg.py [output.svg]
"""
import html
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "whoami.svg")

# ("cmd" | "out" | "gap", text). cmd lines get a green prompt.
LINES = [
    ("cmd", "whoami"),
    ("out", "Ahmad Zaman"),
    ("out", "Backend Engineer"),
    ("gap", ""),
    ("cmd", "now"),
    ("out", "Broadstone Technologies"),
    ("out", "EDR + cloud identity security"),
    ("gap", ""),
    ("cmd", "stack --core"),
    ("out", "Python · Django · DRF · Celery"),
    ("out", "Redis · PostgreSQL · pgvector"),
    ("out", "AWS · GCP · Azure"),
    ("gap", ""),
    ("cmd", "ls projects/"),
    ("out", "unfurl/  paper-mind/  blissful/"),
    ("gap", ""),
    ("cmd", "cat focus.txt"),
    ("out", "async backends, RAG, system design"),
    ("gap", ""),
    ("cmd", "contact"),
    ("out", "ahmadzamannn@gmail.com"),
]

W, H = 840, 880
PAD = 28
TITLEBAR_H = 30
FS = 28
LH = 36
CHAR_W = FS * 0.6
PROMPT = "ahmad@github:~$ "

BG, BG2 = "#0d1117", "#111722"
FRAME = "#30363d"
MUTED = "#7d8590"
INK = "#e6edf3"
GREEN = "#39d353"

TOP = TITLEBAR_H + 52
CHAR_TIME = 0.014         # seconds per typed character
PAUSE = 0.08              # beat after each line


def esc(s):
    return html.escape(s, quote=False)


parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
    f'font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
    f'<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
    f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/></linearGradient></defs>',
    f'<rect width="{W}" height="{H}" rx="12" fill="url(#bg)"/>',
    f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{FRAME}"/>',
    f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>',
]
for i, dot in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
    parts.append(f'<circle cx="{PAD - 8 + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{dot}"/>')
parts.append(f'<text x="{W/2}" y="{TITLEBAR_H/2 + 4}" fill="{MUTED}" font-size="12" '
             f'text-anchor="middle">ahmad@github: ~$ ./whoami.sh</text>')

t = 0.3
last_y = TOP
for i, (kind, text) in enumerate(LINES):
    y = TOP + i * LH
    last_y = y
    if kind == "gap":
        continue
    prompt = PROMPT if kind == "cmd" else "  "
    full = prompt + text
    dur = len(full) * CHAR_TIME
    x_end = PAD + len(full) * CHAR_W
    row_top = y - FS
    body = ""
    if kind == "cmd":
        body += f'<tspan fill="{GREEN}">{esc(PROMPT)}</tspan><tspan fill="{INK}">{esc(text)}</tspan>'
    else:
        body += f'<tspan fill="{INK if i == 1 else MUTED}">{esc("  " + text)}</tspan>'
    parts.append(
        f'<clipPath id="l{i}"><rect x="{PAD}" y="{row_top}" height="{LH + 4}" width="0">'
        f'<animate attributeName="width" from="0" to="{W - PAD*2}" begin="{t:.2f}s" dur="{dur:.2f}s" '
        f'fill="freeze"/></rect></clipPath>'
    )
    parts.append(
        f'<g clip-path="url(#l{i})"><text xml:space="preserve" x="{PAD}" y="{y}" font-size="{FS}" '
        f'font-weight="{700 if i == 1 else 400}">{body}</text></g>'
    )
    # block cursor riding the wipe edge
    parts.append(
        f'<rect y="{row_top + 4}" width="{CHAR_W:.1f}" height="{FS - 2}" fill="{INK}" opacity="0">'
        f'<animate attributeName="x" from="{PAD}" to="{x_end:.1f}" begin="{t:.2f}s" dur="{dur:.2f}s" fill="freeze"/>'
        f'<set attributeName="opacity" to="0.85" begin="{t:.2f}s"/>'
        f'<set attributeName="opacity" to="0" begin="{t + dur:.2f}s"/></rect>'
    )
    t += dur + PAUSE

# final prompt with a steady blinking cursor
y = last_y + LH * 2
parts.append(
    f'<text x="{PAD}" y="{y}" font-size="{FS}" fill="{GREEN}" opacity="0">{esc(PROMPT)}'
    f'<set attributeName="opacity" to="1" begin="{t:.2f}s"/></text>'
)
cx = PAD + len(PROMPT) * CHAR_W
parts.append(
    f'<rect x="{cx:.1f}" y="{y - FS + 4}" width="{CHAR_W:.1f}" height="{FS - 2}" fill="{INK}" opacity="0">'
    f'<animate attributeName="opacity" values="0.85;0.85;0;0" keyTimes="0;0.5;0.51;1" dur="1s" '
    f'begin="{t:.2f}s" repeatCount="indefinite"/></rect>'
)

parts.append('</svg>')
svg = "".join(parts)
with open(OUT, "w") as f:
    f.write(svg)
print(f"wrote {OUT}: {W} x {H}, {len(svg)//1024} KB, types for ~{t:.1f}s")
