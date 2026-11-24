#!/usr/bin/env python3
"""Render the 24 November 2026 world-news poster (1024x1024 PNG).

All text is drawn with real fonts via Pillow. No image model is used.
Deterministic: fixed fonts, fixed layout, no timestamps, no randomness.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (20, 33, 61)
RED = (180, 35, 24)
GOLD = (176, 141, 58)
TEAL = (31, 93, 102)
LIGHT = (233, 227, 210)
MIDGREY = (90, 96, 110)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_I = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    lines = []
    for para in text.split("\n"):
        lines.extend(textwrap.wrap(para, width=width,
                                   break_long_words=False) or [""])
    # re-wrap by pixel width for accuracy
    out = []
    for line in lines:
        words = line.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= width or not cur:
                cur = trial
            else:
                out.append(cur)
                cur = w
        if cur:
            out.append(cur)
    return out


def draw_wrapped(draw, xy, text, fnt, width, fill, spacing=4):
    x, y = xy
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y


def kicker(draw, x, y, label, color=RED):
    f = font(SANS_B, 20)
    draw.text((x, y), label.upper(), font=f, fill=color)
    return y + 28


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- frame ---
    d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=4)
    d.rectangle([22, 22, W - 23, H - 23], outline=GOLD, width=2)

    # --- masthead ---
    y = 44
    d.text((W // 2, y), "THE WORLD IN ONE DAY", font=font(SERIF_B, 58),
           fill=INK, anchor="ma")
    y += 72
    d.text((W // 2, y), "World news  •  One image  •  One day",
           font=font(SANS_I, 22), fill=MIDGREY, anchor="ma")
    y += 40
    # date band
    d.rectangle([48, y, W - 48, y + 58], fill=RED)
    d.text((W // 2, y + 29), "TUESDAY 24 NOVEMBER 2026",
           font=font(SANS_B, 34), fill=(255, 255, 255), anchor="mm")
    y += 58 + 18

    # --- lead story: chess ---
    lead_top = y
    # mini chessboard on the right
    bx, by, bs = 800, lead_top + 8, 176
    sq = bs // 8
    for r in range(8):
        for c in range(8):
            col = PAPER if (r + c) % 2 == 0 else INK
            d.rectangle([bx + c * sq, by + r * sq,
                         bx + (c + 1) * sq, by + (r + 1) * sq], fill=col)
    d.rectangle([bx, by, bx + bs, by + bs], outline=INK, width=3)
    # two kings facing off: bold discs with K on the board
    d.ellipse([bx + 3 * sq + 2, by + 1 * sq + 2, bx + 4 * sq - 2, by + 2 * sq - 2],
              fill=GOLD, outline=INK, width=2)
    d.text((bx + 3 * sq + sq // 2, by + sq + sq // 2), "K",
           font=font(SANS_B, 20), fill=INK, anchor="mm")
    d.ellipse([bx + 4 * sq + 2, by + 6 * sq + 2, bx + 5 * sq - 2, by + 7 * sq - 2],
              fill=(255, 255, 255), outline=INK, width=2)
    d.text((bx + 4 * sq + sq // 2, by + 6 * sq + sq // 2), "K",
           font=font(SANS_B, 20), fill=INK, anchor="mm")
    d.text((bx + bs // 2, by + bs + 8), "GENEVA  •  GAME 1",
           font=font(SANS_B, 16), fill=MIDGREY, anchor="ma")

    lx = 48
    y = kicker(d, lx, lead_top, "Lead  •  Chess  •  Geneva", RED)
    y = draw_wrapped(d, (lx, y),
                     "Youngest title match\never opens in Geneva",
                     font(SERIF_B, 52), 720, INK, spacing=2)
    y += 6
    y = draw_wrapped(d, (lx, y),
                     "Defending champion Gukesh Dommaraju, 20, of India "
                     "faces challenger Javokhir Sindarov, 20, of "
                     "Uzbekistan in Game 1 of a 14-game match for a "
                     "$2.5 million prize fund.",
                     font(SANS, 25), 720, INK, spacing=5)
    y += 10
    d.line([48, y, W - 48, y], fill=INK, width=3)
    y += 16

    # --- supporting stories: 2 columns x 3 rows ---
    stories = [
        ("Football  •  Law", "CAS to rule today on\nSenegal's AFCON appeal",
         "Senegal appeal for their stripped title back after CAF gave "
         "Morocco a 3-0 win when Senegal walked off in January's final, "
         "won 1-0 by Senegal.", TEAL),
        ("Markets  •  Japan", "Japan factory growth\nquickens; services cool",
         "Manufacturing PMI 53.7 in November, up from 53.3; services "
         "50.5; composite 51.5, a six-month low.", TEAL),
        ("Sky  •  Tonight", "Beaver Supermoon\npeaks today",
         "November's full Moon reaches its full phase at 9:53 a.m. "
         "EST — the first of four supermoons.", GOLD),
        ("Space  •  California", "SpaceX to launch\nclassified USSF-266 today",
         "Falcon 9 lifts off from Vandenberg at 7:55 a.m. PT; "
         "booster B1081 flies a record-tying 29th time.", GOLD),
        ("Culture  •  India", "557th birth anniversary\nof Guru Nanak",
         "Sikhs mark Guru Nanak Jayanti today, with prayers at the "
         "Golden Temple in Amritsar.", RED),
        ("Politics  •  Portugal", "Portugal votes on\n2027 budget today",
         "Parliament holds its final vote as unions demonstrate "
         "outside in Lisbon.", RED),
    ]
    col_w = (W - 96 - 32) // 2
    row_h = 162
    for i, (kick, head, deck, accent) in enumerate(stories):
        cx = 48 + (i % 2) * (col_w + 32)
        cy = y + (i // 2) * row_h
        d.rectangle([cx, cy + 6, cx + 8, cy + 118], fill=accent)
        tx = cx + 22
        yy = kicker(d, tx, cy, kick, accent)
        yy = draw_wrapped(d, (tx, yy), head, font(SERIF_B, 30),
                          col_w - 22, INK, spacing=1)
        draw_wrapped(d, (tx, yy + 2), deck, font(SANS, 19),
                     col_w - 22, (52, 58, 74), spacing=3)

    # --- footer ---
    fy = H - 62
    d.line([48, fy, W - 48, fy], fill=INK, width=2)
    d.text((W // 2, fy + 12),
           "All stories reported on Tuesday 24 November 2026",
           font=font(SANS_I, 20), fill=MIDGREY, anchor="ma")

    img.save("entry.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
