#!/usr/bin/env python3
"""
generate_assets.py — Master asset generator.

Runs every generator and writes the resulting SVGs to assets/svg/sections/.
Use this when you want to refresh all generated assets at once.

Usage:
    python scripts/python/generate_assets.py
"""
import io
import os
import subprocess
import sys
from pathlib import Path

# Force UTF-8 output on Windows for the child processes.
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
SECTIONS = ROOT / "assets" / "svg" / "sections"

GENERATORS = [
    "generate_status.py",
    "generate_heatmap.py",
    "generate_skill_tree.py",
]

def run(gen):
    path = ROOT / "scripts" / "python" / gen
    out = SECTIONS / gen.replace("generate_", "").replace(".py", ".svg")
    print(f"  → {gen}")
    result = subprocess.run(
        [sys.executable, str(path)],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    if result.returncode != 0:
        print(f"    ✗ failed: {result.stderr}")
        return False
    out.write_text(result.stdout, encoding="utf-8")
    print(f"    ✓ {out.relative_to(ROOT)}")
    return True

def main():
    SECTIONS.mkdir(parents=True, exist_ok=True)
    print("Generating assets into", SECTIONS.relative_to(ROOT))
    ok = 0
    for g in GENERATORS:
        if run(g):
            ok += 1
    print(f"\n{ok}/{len(GENERATORS)} generators succeeded")

if __name__ == "__main__":
    main()
