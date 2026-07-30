#!/usr/bin/env python3
"""
generate_status.py — Live OS status generator

Renders a fresh "process status" panel SVG with the current timestamp
and a deterministic-looking-but-shifting pattern. Can be wired into a
GitHub Action that regenerates the asset each commit.

Usage:
    python generate_status.py > assets/svg/sections/status.svg
"""
from datetime import datetime, timezone
import math
import random

# Seed by date so the same day produces the same output (cache-friendly).
random.seed(int(datetime.now(timezone.utc).strftime("%Y%m%d")))

WIDTH, HEIGHT = 1200, 240
BAR_COUNT = 22  # "processes"

# Color palette (consistent with the rest of JAIVARDHAN OS)
PALETTE = [
    "#22d3ee",  # cyan
    "#a78bfa",  # violet
    "#ec4899",  # pink
    "#10b981",  # emerald
    "#f59e0b",  # amber
    "#06b6d4",  # sky
    "#fb7185",  # rose
]

# Generate "processes" — deterministic but varied
processes = []
for i in range(BAR_COUNT):
    processes.append({
        "name": f"agent.{random.choice(['core', 'rag', 'eval', 'plan', 'tool', 'critic', 'memory', 'audit', 'ship', 'trace'])}",
        "pid": random.randint(1000, 9999),
        "cpu": random.randint(8, 92),
        "mem": random.randint(12, 86),
        "color": random.choice(PALETTE),
        "status": random.choice(["RUN", "RUN", "RUN", "QUE", "OK"]),
    })

now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
last_modified = datetime.now(timezone.utc).isoformat()

rows = []
for i, p in enumerate(processes):
    y = 56 + i * 8
    rows.append(f"""    <g transform="translate(40,{y})">
      <text x="0" y="0" font-family="JetBrains Mono, monospace" font-size="9" fill="#94a3b8">{p['name']}</text>
      <text x="140" y="0" font-family="JetBrains Mono, monospace" font-size="9" fill="#64748b">{p['pid']}</text>
      <text x="200" y="0" font-family="JetBrains Mono, monospace" font-size="9" fill="#64748b">{p['status']}</text>
      <rect x="240" y="-6" width="600" height="6" rx="3" fill="#0d0d1a"/>
      <rect x="240" y="-6" width="{p['cpu'] * 6}" height="6" rx="3" fill="{p['color']}"/>
      <text x="860" y="0" font-family="JetBrains Mono, monospace" font-size="9" fill="#cbd5e1">{p['cpu']}%</text>
      <rect x="900" y="-6" width="200" height="6" rx="3" fill="#0d0d1a"/>
      <rect x="900" y="-6" width="{p['mem'] * 2}" height="6" rx="3" fill="#a78bfa" opacity="0.7"/>
      <text x="1110" y="0" font-family="JetBrains Mono, monospace" font-size="9" fill="#cbd5e1">{p['mem']}%</text>
    </g>""")

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-label="Live Process Status">
  <title>JAIVARDHAN OS · Live Process Status</title>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#020617"/>
      <stop offset="100%" stop-color="#0a0a1a"/>
    </linearGradient>
    <style>
      .mono {{ font-family: 'JetBrains Mono', 'Fira Code', monospace; }}
    </style>
  </defs>

  <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bg)" rx="8"/>
  <rect x="20" y="20" width="{WIDTH-40}" height="{HEIGHT-40}" rx="6" fill="#06070d" stroke="#1e1b4b"/>

  <text x="40" y="46" class="mono" font-size="11" fill="#22d3ee" letter-spacing="3">▸ LIVE PROCESS STATUS · top · brain://jaivardhan</text>
  <text x="{WIDTH-40}" y="46" text-anchor="end" class="mono" font-size="9" fill="#64748b">{now}</text>

  <g transform="translate(40,72)" class="mono" font-size="9" fill="#64748b" letter-spacing="2">
    <text x="0">PROCESS</text>
    <text x="140">PID</text>
    <text x="200">STATUS</text>
    <text x="240">CPU ▸</text>
    <text x="900">MEM ▸</text>
  </g>

  <line x1="40" y1="62" x2="{WIDTH-40}" y2="62" stroke="#1e1b4b" stroke-width="1"/>

{chr(10).join(rows)}

  <text x="40" y="{HEIGHT-24}" class="mono" font-size="9" fill="#64748b" letter-spacing="2">▸ {BAR_COUNT} processes · 1 user · load: 0.42 0.31 0.28 · uptime: 142d</text>
  <text x="{WIDTH-40}" y="{HEIGHT-24}" text-anchor="end" class="mono" font-size="9" fill="#22d3ee">● AUTO-GENERATED · {last_modified}</text>
</svg>
"""

if __name__ == "__main__":
    print(svg)
