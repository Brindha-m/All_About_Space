"""Check that SVG text labels stay inside the canvas and do not overlap."""

from pathlib import Path
import sys
import xml.etree.ElementTree as ET

from PIL import ImageFont


ROOT = Path(__file__).resolve().parents[1]
SVG_DIR = ROOT / "assets" / "key-concepts"
FONT_PATH = Path("C:/Windows/Fonts/segoepr.ttf")
SVG_TEXT = "{http://www.w3.org/2000/svg}text"


def inherited_anchor(node, parents):
    while node is not None:
        anchor = node.get("text-anchor")
        if anchor:
            return anchor
        node = parents.get(node)
    return "start"


def text_boxes(svg_path):
    root = ET.parse(svg_path).getroot()
    width = float(root.get("width", "1200"))
    height = float(root.get("height", "630"))
    parents = {child: parent for parent in root.iter() for child in parent}
    boxes = []

    for node in root.iter(SVG_TEXT):
        text = "".join(node.itertext())
        font_size = int(float(node.get("font-size", "30")))
        font = ImageFont.truetype(str(FONT_PATH), font_size)
        left, top, right, bottom = font.getbbox(text)
        text_width = right - left
        text_height = bottom - top
        x = float(node.get("x", "0"))
        y = float(node.get("y", "0"))
        anchor = inherited_anchor(node, parents)

        if anchor == "middle":
            x -= text_width / 2
        elif anchor == "end":
            x -= text_width

        boxes.append((x, y - text_height, text_width, text_height, text))

    return width, height, boxes


def intersects(first, second):
    ax, ay, aw, ah, _ = first
    bx, by, bw, bh, _ = second
    return (
        ax < bx + bw
        and ax + aw > bx
        and ay < by + bh
        and ay + ah > by
    )


def main():
    if not FONT_PATH.exists():
        raise SystemExit(f"Required font was not found: {FONT_PATH}")

    issues = []
    files = sorted(SVG_DIR.glob("*.svg"))

    for svg_path in files:
        width, height, boxes = text_boxes(svg_path)
        for index, box in enumerate(boxes):
            x, y, box_width, box_height, text = box
            if x < 0 or y < 0 or x + box_width > width or y + box_height > height:
                issues.append(f"{svg_path.name}: out of bounds: {text!r}")

            for other in boxes[index + 1 :]:
                if intersects(box, other):
                    issues.append(
                        f"{svg_path.name}: overlap: {text!r} / {other[4]!r}"
                    )

    if issues:
        print("\n".join(issues))
        return 1

    print(f"Checked {len(files)} SVG files: no text overlaps or clipped labels.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
