#!/usr/bin/env python3
"""Entry point for news-image-20261125.

Copies the pre-built entry image (entry.png, in this repository) to the
directory named by MAKEFUN_OUTPUT_DIR (default "."), as entry.png.
Standard library only, no network, deterministic: the same bytes every run.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit("entry.png missing from repository")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
