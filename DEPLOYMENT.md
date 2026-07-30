# 🚀 Deployment Guide — `jv-singh/jv-singh`

> A premium GitHub profile built like a product landing page.
> **Motto: Let's Make It Exist.**

---

## 📁 Final Folder Structure

After deploying, the `jv-singh/jv-singh` profile repo on GitHub should look exactly like this:

```
jv-singh/
├── README.md                          ← the master profile (the only file GitHub renders on your profile)
├── DEPLOYMENT.md                      ← this file (optional, hidden in collapsed view)
│
├── assets/                            ← all custom SVGs + static visuals
│   ├── banner.svg                     ← hero banner with name, motto, status card
│   ├── wave.svg                       ← gradient wave divider
│   ├── footer.svg                     ← motto / signature footer
│   ├── divider.svg                    ← section divider
│   ├── quote-box.svg                  ← gradient quote icon
│   ├── tech-mesh.svg                  ← tech node mesh graphic
│   ├── behelit-card.svg               ← Behelit AI project card
│   ├── agentic-rag-card.svg           ← Enterprise RAGBot project card
│   ├── vision-card.svg                ← Vision Bot project card
│   ├── lifeatlas-card.svg             ← LifeAtlas LPI project card
│   ├── redrob-card.svg                ← Redrob project card
│   └── typing-config.md               ← reference for typing SVG URLs
│
└── .github/
    └── workflows/
        ├── snake.yml                  ← generates animated contribution snake
        └── metrics.yml                ← generates lowlighter/metrics SVG reports
```

---

## 🪜 Step-by-Step Deployment

### 1. Create the profile repo
Create a **public** repo whose name is **identical to your GitHub username**:
- Repo name: `jv-singh`
- Visibility: **Public**
- Initialize: **without** a README (we already have one)
- Description: `Machine Learning Engineer · GenAI · Agentic AI · Let's Make It Exist.`

### 2. Push the contents
From the `jv-singh/` folder in this project:

```bash
cd jv-singh
git init
git add .
git commit -m "feat(profile): premium landing-page README · Let's Make It Exist"
git branch -M main
git remote add origin https://github.com/jv-singh/jv-singh.git
git push -u origin main
```

### 3. Verify
Visit **https://github.com/jv-singh** — the README renders on the profile page.

### 4. Trigger workflows
- `snake.yml` runs on push and every 12 hours → publishes `github-snake.svg` to the `output` branch.
- `metrics.yml` runs daily → publishes metrics to the `output` branch.

> **Note:** The `lowlighter/metrics` workflow needs a fine-grained PAT in `Settings → Secrets → Actions → METRICS_TOKEN` for private-repo access. For public-only metrics, the default `GITHUB_TOKEN` is enough.

---

## 🎨 Customization Checklist

When you publish your real repos, update these repo-name placeholders in `README.md`:

| Placeholder | Replace with |
| :--- | :--- |
| `behelit-ai` | your Behelit AI repo name |
| `agentic-ragbot` | your RAGBot repo name |
| `vision-bot` | your Vision Bot repo name |
| `lifeatlas-lpi` | your LifeAtlas LPI repo name |

Search the README for `repo=behelit-ai`, `repo=agentic-ragbot`, etc. — those are the four pinned-repo URLs to update.

Update social links:
- `linkedin.com/in/jv-singh` → your LinkedIn slug
- `twitter.com/jv_singh` → your X / Twitter handle
- `mailto:jaivardhan@example.com` → your real email
- `discord.gg/your-discord` → your Discord invite

---

## 🛠️ APIs / Services Used

| Service | URL | Used for |
| :--- | :--- | :--- |
| readme-typing-svg | `https://readme-typing-svg.demolab.com/` | Animated typing lines |
| github-readme-stats | `https://github-readme-stats.vercel.app` | Stats card, top langs, pin cards |
| github-readme-streak-stats | `https://github-readme-streak-stats.herokuapp.com` | Streak counter |
| github-profile-trophy | `https://github-profile-trophy.vercel.app` | Trophy grid |
| github-readme-activity-graph | `https://github-readme-activity-graph.vercel.app` | Activity graph |
| Platane/snk | GitHub Action | Animated contribution snake |
| lowlighter/metrics | GitHub Action | Detailed metrics SVG |
| komarev/ghpvc | `https://komarev.com/ghpvc/` | Profile view counter |
| visitor-badge.laobi.icu | `https://visitor-badge.laobi.icu` | Visitor counter |
| shields.io | `https://shields.io` | All badges |
| capsule-render | `https://capsule-render.vercel.app` | Animated footer capsule |

---

## 🌈 Design Tokens

| Token | Hex | Used for |
| :--- | :--- | :--- |
| `indigo-500` | `#6366f1` | Primary accent |
| `violet-500` | `#8b5cf6` | Secondary accent |
| `blue-500` | `#3b82f6` | Tertiary accent |
| `emerald-500` | `#10b981` | Success / status |
| `pink-500` | `#ec4899` | Highlights |
| `amber-500` | `#f59e0b` | Warnings / vision |
| `slate-900` | `#0d1117` | Card backgrounds |
| `slate-300` | `#cbd5e1` | Body text |

---

## ✨ The Final Line

> **🚀 Let's Make It Exist.**
> `github.com/jv-singh` · `Jaivardhan Singh`
