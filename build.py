#!/usr/bin/env python3
"""Build the standalone HTML presentation used by GitHub Pages."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "src" / "deck.html"
DIST = ROOT / "dist"


def build() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    head, rest = source.split('<div id="viewport">', 1)
    standalone = (
        '<!doctype html>\n<html lang="en">\n<head>\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        + head
        + '</head>\n<body>\n<div id="viewport">'
        + rest
        + '\n</body>\n</html>\n'
    )

    DIST.mkdir(exist_ok=True)
    (DIST / "analytics-in-food-delivery.html").write_text(standalone, encoding="utf-8")
    (ROOT / "index.html").write_text(standalone, encoding="utf-8")


if __name__ == "__main__":
    build()
    print(ROOT / "index.html")
