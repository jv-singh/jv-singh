#!/usr/bin/env python3
"""
generate_skill_tree.py — Animated skill tree SVG.

Renders a literal "skill tree" inspired by gaming progression —
each node is a skill, edges are unlocks, glow intensity is mastery.

Output:
    assets/svg/sections/skill-tree.svg
"""
import math

WIDTH, HEIGHT = 1200, 480

# Skill tree definition: (id, x, y, level, label, parent)
SKILLS = [
    # tier 0 — root
    ("python",          600,  60, 5, "PYTHON",       None),
    # tier 1 — foundations
    ("sql",             400, 140, 5, "SQL",          "python"),
    ("stats",           600, 140, 4, "STATS",        "python"),
    ("linux",           800, 140, 4, "LINUX",        "python"),
    # tier 2 — ML
    ("pytorch",         300, 220, 4, "PYTORCH",      "sql"),
    ("sklearn",         500, 220, 5, "SKLEARN",      "stats"),
    ("cv",              700, 220, 4, "OPENCV",       "stats"),
    ("nlp",             900, 220, 4, "NLP",          "linux"),
    # tier 3 — agents
    ("rag",             250, 320, 4, "RAG",          "pytorch"),
    ("prompts",         450, 320, 4, "PROMPTS",      "sklearn"),
    ("vision",          650, 320, 5, "VISION",       "cv"),
    ("rl",              850, 320, 3, "RL",           "nlp"),
    # tier 4 — frontier
    ("langgraph",       300, 400, 4, "LANGGRAPH",    "rag"),
    ("mcp",             500, 400, 3, "MCP",          "prompts"),
    ("prod",            700, 400, 4, "PRODUCTION",   "vision"),
    ("a2a",             900, 400, 3, "A2A",          "rl"),
]

def node_color(level):
    if level >= 5: return "#22d3ee"
    if level >= 4: return "#a78bfa"
    if level >= 3: return "#ec4899"
    if level >= 2: return "#f59e0b"
    return "#94a3b8"

# Build map
by_id = {s[0]: s for s in SKILLS}

# Edges
edges = []
for s in SKILLS:
    if s[5]:
        edges.append((by_id[s[5]], s))

edge_lines = []
for parent, child in edges:
    edge_lines.append(
        f'<line x1="{parent[1]}" y1="{parent[2]}" x2="{child[1]}" y2="{child[2]}" '
        f'stroke="#a78bfa" stroke-width="1" stroke-dasharray="2 4" opacity="0.5"/>'
    )

nodes = []
for s in SKILLS:
    _, x, y, lvl, label, _ = s
    color = node_color(lvl)
    r = 10 + lvl * 2
    nodes.append(f"""
    <g transform="translate({x},{y})">
      <circle r="{r+6}" fill="none" stroke="{color}" stroke-opacity="0.2" stroke-width="1" class="pulse"/>
      <circle r="{r}" fill="#0a0a1a" stroke="{color}" stroke-width="1.4" filter="url(#b)"/>
      <text text-anchor="middle" y="3" class="mono" font-size="9" fill="{color}" font-weight="700">{lvl}</text>
      <text text-anchor="middle" y="{r+16}" class="mono" font-size="9" fill="#cbd5e1" letter-spacing="2">{label}</text>
    </g>""")

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-label="Skill Tree">
  <title>JAIVARDHAN OS · Skill Tree</title>
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#0a0a1a"/>
      <stop offset="100%" stop-color="#020617"/>
    </radialGradient>
    <filter id="b" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2"/>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <style>
      .mono {{ font-family: 'JetBrains Mono', monospace; }}
      .pulse {{ animation: p 2s ease-in-out infinite; transform-origin: center; }}
      @keyframes p {{ 0%,100% {{ opacity: 0.2 }} 50% {{ opacity: 0.6 }} }}
    </style>
  </defs>

  <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bg)" rx="8"/>
  <rect x="20" y="20" width="{WIDTH-40}" height="{HEIGHT-40}" rx="6" fill="#06070d" stroke="#1e1b4b"/>

  <text x="40" y="50" class="mono" font-size="11" fill="#22d3ee" letter-spacing="3">▸ SKILL TREE · PROGRESSION</text>
  <text x="{WIDTH-40}" y="50" text-anchor="end" class="mono" font-size="9" fill="#64748b">UNLOCK ORDER · BOTTOM-UP</text>

  <g transform="translate(0,30)">
    {chr(10).join(edge_lines)}
    {''.join(nodes)}
  </g>

  <text x="40" y="{HEIGHT-20}" class="mono" font-size="9" fill="#64748b" letter-spacing="2">▸ LVL 5 · mastered  ·  LVL 4 · strong  ·  LVL 3 · learning  ·  LVL 2 · exploring</text>
  <text x="{WIDTH-40}" y="{HEIGHT-20}" text-anchor="end" class="mono" font-size="9" fill="#22d3ee">● 16 NODES UNLOCKED</text>
</svg>
"""

if __name__ == "__main__":
    print(svg)
