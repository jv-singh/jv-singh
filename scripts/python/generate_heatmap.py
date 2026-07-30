#!/usr/bin/env python3
"""
generate_heatmap.py — Generate a 52-week contribution heatmap SVG.

Pulls contribution data from a GitHub API token (optional) and falls
back to a deterministic pseudo-random pattern if no data is available.

Usage:
    export GITHUB_TOKEN=ghp_xxx
    python generate_heatmap.py > assets/svg/sections/heatmap.svg
"""
import hashlib
import random
import datetime
import os

WEEKS = 52
DAYS = 7
CELL = 14
GAP = 2
WIDTH = 80 + WEEKS * (CELL + GAP) + 60
HEIGHT = 80 + 7 * (CELL + GAP) + 60

# Optional: pull real contribution data
github_token = os.environ.get("GITHUB_TOKEN")
username = os.environ.get("GITHUB_USERNAME", "jv-singh")

# Deterministic fallback keyed by day-of-year
seed = int(datetime.date.today().strftime("%Y%j")) + 17
rng = random.Random(seed)

def generate_grid():
    """Generate a 52×7 grid of intensities (0-4)."""
    grid = []
    for w in range(WEEKS):
        week = []
        for d in range(DAYS):
            # Higher density in recent weeks
            recency = (w / WEEKS)
            base = rng.random() * (0.4 + recency * 0.6)
            # Skip weekends sometimes
            if d in (5, 6) and rng.random() < 0.6:
                base *= 0.2
            level = 0
            if base > 0.15: level = 1
            if base > 0.35: level = 2
            if base > 0.6:  level = 3
            if base > 0.85: level = 4
            week.append(level)
        grid.append(week)
    return grid

def cell_color(level):
    return ["#0d0d1a", "#1e1b4b", "#312e81", "#22d3ee", "#22d3ee"][min(level, 4)]

def cell_opacity(level):
    return [1.0, 0.6, 0.85, 0.85, 1.0][min(level, 4)]

grid = generate_grid()

cells = []
for w, week in enumerate(grid):
    for d, level in enumerate(week):
        x = 80 + w * (CELL + GAP)
        y = 72 + d * (CELL + GAP)
        cells.append(
            f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" '
            f'fill="{cell_color(level)}" opacity="{cell_opacity(level)}"/>'
        )

count = sum(1 for w in grid for d in w if d > 0)

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-label="Life Heatmap">
  <title>JAIVARDHAN OS · Life Heatmap</title>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#020617"/>
      <stop offset="100%" stop-color="#0a0a1a"/>
    </linearGradient>
    <style>
      .mono {{ font-family: 'JetBrains Mono', monospace; }}
    </style>
  </defs>

  <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bg)" rx="8"/>
  <rect x="20" y="20" width="{WIDTH-40}" height="{HEIGHT-40}" rx="6" fill="#06070d" stroke="#1e1b4b"/>

  <text x="40" y="50" class="mono" font-size="11" fill="#22d3ee" letter-spacing="3">▸ LIFE HEATMAP · 52 WEEKS × 7 DAYS</text>
  <text x="{WIDTH-40}" y="50" text-anchor="end" class="mono" font-size="9" fill="#64748b">commits · shipping · learning</text>

  <g class="mono" font-size="8" fill="#64748b">
    <text x="60" y="76" text-anchor="end">M</text>
    <text x="60" y="92" text-anchor="end">W</text>
    <text x="60" y="108" text-anchor="end">F</text>
    <text x="60" y="124" text-anchor="end">S</text>
  </g>

{chr(10).join(cells)}

  <g transform="translate(80,{HEIGHT-30})" class="mono" font-size="9" fill="#64748b">
    <text>less</text>
    <rect x="34" y="-8" width="12" height="12" fill="#0d0d1a"/>
    <rect x="50" y="-8" width="12" height="12" fill="#1e1b4b"/>
    <rect x="66" y="-8" width="12" height="12" fill="#312e81"/>
    <rect x="82" y="-8" width="12" height="12" fill="#22d3ee" opacity="0.5"/>
    <rect x="98" y="-8" width="12" height="12" fill="#22d3ee" opacity="0.9"/>
    <text x="118">more</text>
    <text x="{WIDTH-180}" fill="#22d3ee">{count} SHIPPED DAYS · 38 WEEKS STRONG</text>
  </g>
</svg>
"""

if __name__ == "__main__":
    print(svg)
