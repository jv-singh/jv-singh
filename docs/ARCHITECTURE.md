# 🏗️ JAIVARDHAN OS · Architecture

> *"The system is the README. The README is the system."*

## 1. Concept

JAIVARDHAN OS is a GitHub profile re-imagined as an **operating system**.
Every section is a module. Every scroll is a level. Every animation is a heartbeat.

**Design philosophy:** *Cinematic, OS-feel, no repeated layouts, every section tells a story.*

**Inspiration (not imitation):** Apple · OpenAI · Cyberpunk 2077 · TRON Legacy · Iron Man HUD · Stripe · Figma · Interstellar · Arc Browser.

## 2. Folder Structure

```
jv-singh/
├── README.md                    # The OS front-end
├── assets/
│   ├── svg/
│   │   ├── icons/              # 34 custom monochrome-with-accent icons
│   │   ├── projects/           # 5 cinematic project posters
│   │   ├── meters/             # 7 live meters (consciousness, brain, radar, ...)
│   │   ├── diagrams/           # 3 animated architecture diagrams
│   │   └── sections/           # Hero, footer, dividers, boot, timeline, ...
│   ├── banner.svg              # legacy banner
│   ├── divider.svg             # legacy divider
│   ├── footer.svg              # legacy footer
│   └── wave.svg                # legacy wave
├── .github/
│   └── workflows/
│       ├── metrics.yml         # hourly lowlighter/metrics refresh
│       ├── snake.yml           # daily Platane/snk contribution snake
│       ├── auto-update.yml     # daily README date stamping
│       └── lint-assets.yml     # SVG lint on PR
├── scripts/
│   └── python/
│       ├── generate_assets.py  # master generator runner
│       ├── generate_status.py  # live process status SVG
│       ├── generate_heatmap.py # 52-week heatmap SVG
│       └── generate_skill_tree.py # animated skill tree
├── docs/
│   ├── ARCHITECTURE.md         # this file
│   ├── DEPLOYMENT.md           # how to ship this
│   └── FUTURE_IDEAS.md         # what's next
└── examples/
    └── README-snippets.md      # reusable building blocks
```

## 3. Visual System

### Color Palette (OS Theme)

| name | hex | use |
|------|-----|-----|
| `void` | `#020617` | deepest background |
| `core` | `#0a0a1a` | panel background |
| `panel` | `#06070d` | card background |
| `edge` | `#1e1b4b` | panel stroke |
| `accent-deep` | `#312e81` | inactive UI |
| `cyan` | `#22d3ee` | primary signal |
| `violet` | `#a78bfa` | secondary signal |
| `pink` | `#ec4899` | tertiary signal |
| `emerald` | `#10b981` | success / online |
| `amber` | `#f59e0b` | warning / running |
| `rose` | `#ef4444` | danger / error |
| `muted` | `#64748b` | labels, captions |
| `text` | `#cbd5e1` | body text |
| `bright` | `#e2e8f0` | titles |

### Typography

- **Display:** `Inter`, `SF Pro Display`, system-ui
- **Mono:** `JetBrains Mono`, `Fira Code`, monospace
- **Sizes:** titles 56–120px · section headers 32px · body 13–16px · mono captions 9–11px

### Motion

- **Pulse** — opacity 0.5↔1 over 2s
- **Spin** — full rotation over 14–30s (rings, orbits)
- **Flow** — `stroke-dashoffset` for connected lines, 3s
- **Scan** — translating gradient overlay, 4.5s
- **Bloom** — Gaussian-blur filter for glowing accents

## 4. Section Manifest (26 modules)

| # | section | asset | purpose |
|---:|:---|:---|:---|
| 00 | boot | `sections/boot.svg` | set the tone — feels like an OS booting up |
| 01 | mission briefing | text + icons | orient the visitor |
| 02 | system monitor | `meters/monitor.svg` | show 6 live metrics |
| 03 | consciousness | `meters/consciousness.svg` | quant self-report |
| 04 | brain waves | `meters/brain.svg` | flow-state visualization |
| 05 | neural density | `meters/density.svg` | 12-month knowledge compound |
| 06 | innovation radar | `meters/radar.svg` | where the next wave is forming |
| 07 | skill galaxy | `meters/galaxy.svg` | 8 constellations |
| 08 | mission compass | `meters/compass.svg` | bearing 042° |
| 09 | career timeline | `sections/timeline.svg` | 2023 → 2027+ |
| 10 | tech universe | badges | tools & capabilities |
| 11 | RAG pipeline | `diagrams/rag-pipeline.svg` | blueprint |
| 12 | agent mesh | `diagrams/agent-mesh.svg` | A2A + MCP |
| 13 | neural net | `diagrams/neural-net.svg` | substrate |
| 14 | shipped projects | 5 posters | movie-poster style |
| 15 | memory vault | `sections/memory.svg` | 3-tier memory |
| 16 | constellation | `sections/constellation.svg` | research interests |
| 17 | live goals | `sections/goals.svg` | 2026 progress |
| 18 | life heatmap | `sections/heatmap.svg` | 52 weeks |
| 19 | GitHub analytics | vercel app + graphs | telemetry |
| 20 | contribution snake | Platane/snk | playful touch |
| 21 | support | badges | sponsor / coffee |
| 22 | connect | badges | social links |
| 23 | education | table | formal |
| 24 | achievements | cards | proof of work |
| 25 | currently | table | building/learning/vibing |
| 26 | words I live by | quotes | philosophy |

## 5. SVG Conventions

All SVGs follow a shared pattern so the OS feels coherent:

```xml
<svg viewBox="0 0 W H" role="img" aria-label="...">
  <title>JAIVARDHAN OS · ...</title>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#020617"/>
      <stop offset="100%" stop-color="#0a0a1a"/>
    </linearGradient>
    <filter id="b" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2"/>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="W" height="H" fill="url(#bg)" rx="8"/>
  <rect x="20" y="20" width="W-40" height="H-40" rx="6" fill="#06070d" stroke="#1e1b4b"/>

  <!-- Section-specific content -->
</svg>
```

- **Width** is usually 1200, height varies by purpose.
- **Outer panel:** `rx=6`, stroke `#1e1b4b`, fill `#06070d`.
- **Title strip:** mono, `#22d3ee`, letter-spacing 3, `▸ SECTION NAME`.
- **Caption strip:** mono, `#64748b`, top-right or bottom-right.
- **Animations** are CSS-keyframe-based so GitHub renders them inline (no JS).

## 6. Why This Works on GitHub

GitHub renders SVGs in `<img>` tags as static or animated images.
CSS `@keyframes` and `<animate>` elements *do* play.
`filter` and `feGaussianBlur` work. JavaScript is sandboxed — that's why we don't use it.

**Limitations we worked around:**

| limit | workaround |
|---|---|
| no JS | use CSS animations + `<animate>` |
| no `<canvas>` | use SVG primitives |
| size limits | keep each SVG < 50KB by avoiding redundant patterns |
| no fonts | use system mono + sans-serif stacks |
| no interactivity | design for "feels interactive" via motion + state hints |

## 7. Why It Should Be Shared

A profile built like an OS makes the visitor feel like they've *entered* something.
Not scrolled past something. The frame, the panel, the boot sequence, the radial radar —
each one says "this person takes their craft seriously."

That's the goal.

---

**Author:** Jaivardhan Singh · Noida, India · 2026