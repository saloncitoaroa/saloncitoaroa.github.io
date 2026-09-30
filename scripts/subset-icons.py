"""Regenera assets/fonts/material-symbols-outlined.woff2 con solo los iconos
que usan las páginas .html de la raíz (unos 10 KB en vez de 4 MB).

Requisitos (una vez):
    npm install --no-save material-symbols
    pip install fonttools brotli uharfbuzz

Uso:
    python3 scripts/subset-icons.py
"""
import re
import tempfile
from pathlib import Path

import uharfbuzz as hb
from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "node_modules/material-symbols/material-symbols-outlined.woff2"
OUT = ROOT / "assets/fonts/material-symbols-outlined.woff2"
CHARS = "abcdefghijklmnopqrstuvwxyz0123456789_"

icons = set()
for page in ROOT.glob("*.html"):
    html = page.read_text(encoding="utf-8")
    icons.update(re.findall(r'class="[^"]*material-symbols-outlined[^"]*"[^>]*>\s*([a-z0-9_]+)\s*<', html))
print(f"{len(icons)} iconos: {' '.join(sorted(icons))}")

with tempfile.TemporaryDirectory() as tmp:
    full = Path(tmp) / "full.ttf"
    font = TTFont(SRC, lazy=False)
    font.flavor = None
    font.save(full)
    order = font.getGlyphOrder()

    # Cada nombre de icono es una ligadura; se busca el glifo que produce,
    # con y sin relleno (FILL 0 y 1).
    hb_font = hb.Font(hb.Face(hb.Blob.from_file_path(str(full))))
    glyphs = set()
    for name in icons:
        for fill in (0, 1):
            hb_font.set_variations({"FILL": fill})
            buf = hb.Buffer()
            buf.add_str(name)
            buf.guess_segment_properties()
            hb.shape(hb_font, buf, {})
            shaped = [order[info.codepoint] for info in buf.glyph_infos]
            if len(shaped) != 1:
                raise SystemExit(f"'{name}' no es un icono de Material Symbols")
            glyphs.update(shaped)

    # Se fijan grosor, grado y tamaño óptico; solo se conserva el eje FILL.
    inst = Path(tmp) / "inst.ttf"
    instancer.instantiateVariableFont(TTFont(full, lazy=False), {"GRAD": 0, "opsz": 24, "wght": 400}).save(inst)

    font = TTFont(inst, lazy=False)
    cmap = font.getBestCmap()
    keep = [".notdef"] + [cmap[ord(c)] for c in CHARS if ord(c) in cmap] + sorted(glyphs)
    opts = subset.Options()
    opts.layout_closure = False
    opts.layout_features = ["*"]
    opts.notdef_outline = True
    opts.name_IDs = ["*"]
    opts.flavor = "woff2"
    subsetter = subset.Subsetter(opts)
    subsetter.populate(glyphs=keep, unicodes=[ord(c) for c in CHARS])
    subsetter.subset(font)
    font.flavor = "woff2"
    font.save(OUT)

print(f"{OUT.relative_to(ROOT)}: {OUT.stat().st_size / 1024:.1f} KB")
