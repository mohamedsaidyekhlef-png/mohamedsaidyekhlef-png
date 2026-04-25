# context-collapse

[![PyPI](https://img.shields.io/pypi/v/context-collapse?color=00d4aa&style=flat-square)](https://pypi.org/project/context-collapse/)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue?style=flat-square)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-yellow?style=flat-square)](LICENSE)
[![Zero Deps](https://img.shields.io/badge/dependencies-zero-brightgreen?style=flat-square)](#)

**Understand any codebase in 30 minutes — not 3 days.**

One command. Any repo. Any language. AI-powered Cold Start Pack in seconds.

→ **[Live Demo](https://context-collapse.ghostskill.com)**

---

## The Problem Nobody Named

```
Day 1  Reading files, trying to understand structure
Day 2  Tracing dependencies, hitting dead ends
Day 3  Finally have a mental model — start coding
Day 4  Make the actual change. Takes 20 minutes.

3 days wasted. Every time. For every developer.
Multiply by every new hire, every PR review, every open-source contributor.
```

This is the cold start problem. Nobody had a tool for it.

**context-collapse names it. And eliminates it.**

---

## Demo

```
$ context-collapse flask/

  context-collapse starting...
  Repo: /dev/flask

  [1/3] Mining git history...
        1,247 commits found
        30 active files tracked
        18 co-change pairs detected

  [2/3] Running AI analysis...
        Purpose inference... done
        Key decisions extracted (5)
  ⚡    Shock insight generated
  ⚠    3 danger zones found

  [3/3] Rendering Cold Start Pack...

  ✓ Done in 1.4s → cold-start-report.html

  ⚡ INSIGHT: app.py and ctx.py changed together in 34% of all commits.
     Changing one without the other causes silent context failures.

  ⚠  DANGER: sessions.py modified in every auth-related commit.
     No isolated test suite. Highest breakage risk in the repo.
```

---

## What's Inside Every Cold Start Pack

### 01 · Re-Entry Reading Sequence
Exactly which files to read first, ranked by importance score.

```
01  src/flask/ctx.py        58 changes  score 5.8  ← start here
02  src/flask/app.py        89 changes  score 5.0
03  src/flask/helpers.py    39 changes  score 4.9
04  src/flask/sessions.py   48 changes  score 4.2
05  src/flask/globals.py    21 changes  score 3.8
```

### 02 · File Churn Heatmap
What changes most — high churn = high importance OR high instability.

```
#1  src/flask/app.py         ████████████████████  89x
#2  CHANGES.rst              ██████████████████░░  82x
#3  src/flask/sansio/app.py  ███████████████░░░░░  69x
```

### 03 · Implicit Coupling Map
Files that always change together — the hidden architecture your diagram never shows.

```
app.py      <->  ctx.py       changed together 34x  ← silent entanglement
sessions.py <->  app.py       changed together 28x
sansio/app  <->  helpers.py   changed together 21x
```

### 04 · Danger Zones (AI-Identified)

```
⚠ [HIGH] IMPLICIT COUPLING
  app.py and ctx.py change together in 34% of all commits.
  They are architecturally entangled — touching one without
  the other causes silent context failures.

⚠ [HIGH] CHURN HOTSPOT
  app.py modified 89 times — the single most volatile file.
  Every PR that touches it carries elevated regression risk.

⚠ [HIGH] INSTABILITY SIGNAL
  41% of commits are bug fixes (healthy threshold: ~20%).
  This codebase is in chronic firefighting mode.
```

### 05 · Commit DNA
Every commit classified. Team culture made visible.

```
feature      ████████████░░░░  42%
fix          ████████░░░░░░░░  31%
refactor     ████░░░░░░░░░░░░  14%
docs         ██░░░░░░░░░░░░░░   7%
performance  █░░░░░░░░░░░░░░░   4%
test         █░░░░░░░░░░░░░░░   2%
```

### 06 · Key Architectural Decisions (AI-Extracted)

```
1. Merged app and request context to reduce complexity
2. Introduced sansio layer to separate protocol from framework
3. Added secret key rotation for zero-downtime key changes
4. Dropped Python 3.8 to use modern type hints throughout
5. Switched to uv for faster dependency management
```

### ⚡ Shock Insight (AI)
The one thing that makes developers go "I didn't expect that":

```
⚡ "app.py and ctx.py changed together in 34% of all commits —
    they are secretly one module that was never merged."
```

---

## Install

```bash
pip install context-collapse
```

## Usage

```bash
context-collapse path/to/repo     # analyze any local repo
context-collapse .                # current directory
context-collapse . --no-ai        # instant, no API key needed
context-collapse . -o report.html # custom output path
```

## AI Layer — Free

Get a free Gemini key at [aistudio.google.com](https://aistudio.google.com) — 1500 req/day, no credit card required.

```bash
# macOS/Linux
export GEMINI_API_KEY=your_key_here
context-collapse .

# Windows
set GEMINI_API_KEY=your_key_here
context-collapse .
```

---

## Architecture

```
context-collapse/
├── cc.py                    ← CLI entrypoint
└── src/
    ├── git_miner.py         ← Git history extraction engine
    ├── ai_brain.py          ← Gemini AI: purpose, decisions, shock insights, danger zones
    └── report_renderer.py   ← Self-contained HTML report generator

Zero external dependencies. Pure Python stdlib.
Any OS. Any git repo. Any language.
```

---

## Why This Exists

Tools like Sourcegraph, CodeSee, and Swimm solve documentation and navigation.  
Nobody solved **re-entry**.

The problem isn't missing docs. It's the cognitive overhead of rebuilding your mental  
model of a system you once understood — invisible in sprint planning, multiplied across  
every team member, completely unsolved by existing tooling.

context-collapse names it. And eliminates it.

---

## Contributing

```bash
git clone https://github.com/mohamedsaidyekhlef-png/context-collapse
cd context-collapse
python cc.py . --no-ai
```

PRs welcome. Open an issue first for large changes.

---

## License

MIT
