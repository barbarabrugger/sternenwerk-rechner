"""Render the edition's original geometric mark; requires Pillow.

No existing artwork or personal album data is used.
"""
from pathlib import Path
from PIL import Image, ImageDraw

ASSETS = Path(__file__).resolve().parents[1] / 'src' / 'Calculator' / 'Assets'
SIZES = {'AppList': (44, 44), 'MedTile': (150, 150), 'LargeTile': (310, 310),
         'WideTile': (310, 150), 'SmallTile': (71, 71), 'StoreLogo': (50, 50),
         'SplashScreen': (620, 300)}

def render(size):
    scale = 4
    w, h = (v * scale for v in size)
    image = Image.new('RGBA', (w, h))
    draw = ImageDraw.Draw(image)
    d = min(w, h) * .90
    cx, cy = w / 2, h / 2
    box = (cx - d / 2, cy - d / 2, cx + d / 2, cy + d / 2)
    draw.rounded_rectangle(box, radius=d * .23, fill='#102126')
    r = d * .31
    draw.ellipse((cx-r, cy-r, cx+r, cy+r), outline='#A68C5C', width=max(1, round(d*.018)))
    # Compass star, with two tiny satellites.
    a, b = d * .32, d * .075
    draw.polygon([(cx, cy-a), (cx+b, cy-b), (cx+a*.83, cy), (cx+b, cy+b),
                  (cx, cy+a), (cx-b, cy+b), (cx-a*.83, cy), (cx-b, cy-b)], fill='#DFB978')
    for x, y, radius, color in [(cx+d*.28, cy-d*.27, d*.036, '#F0E5D2'),
                                 (cx-d*.28, cy+d*.27, d*.022, '#93D9C4')]:
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=color)
    return image.resize(size, Image.Resampling.LANCZOS)

if __name__ == '__main__':
    for kind, size in SIZES.items():
        render(size).save(ASSETS / f'Sternenwerk{kind}.png')
    print(f'Rendered {len(SIZES)} original icon assets.')
