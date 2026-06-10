<div align="center">

# Claude Fable 5 System Prompt

### The Complete Leaked System Prompt from Anthropic's Most Intelligent Model

![Claude Fable 5 Hero Banner](assets/fable5-hero.png)

*Curated & Extracted by **[Sayan Chowdhury](https://github.com/saynchowdhury)***

[![Last Updated](https://img.shields.io/badge/Updated-June%202026-blue)]()
[![Prompt Length](https://img.shields.io/badge/Prompt-~1580%20lines-orange)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()
[![Stars](https://img.shields.io/github/stars/saynchowdhury/claude-fable-5-system-prompt?style=social)]()

*A comprehensive archive and analysis of the system prompt powering Claude Fable 5 — Anthropic's first Mythos-class model.*

[Key Revelations](#key-revelations) | [Full Prompt](system-prompt/full-system-prompt.md) | [Analysis](system-prompt/analysis/key-findings.md) | [Highlights](highlights/surprising-revelations.md)

</div>

---

## What Is This?

This repository contains the **complete system prompt** (~1,580 lines, ~120KB) for **Claude Fable 5**, Anthropic's most capable generally-available AI model as of June 2026. The prompt was extracted from a live claude.ai session and reveals the inner architecture, behavioral guidelines, tool definitions, and safety frameworks that govern how Claude Fable 5 thinks, responds, and interacts.

This is the most detailed look yet into how Anthropic engineers its flagship model's behavior.

---

## Key Revelations

### Mythos-Class: A New Model Tier Above Opus

Claude Fable 5 belongs to an entirely new **"Mythos-class"** model tier that sits **above Claude Opus** in capability. The prompt confirms:

> *"This iteration of Claude is Claude Fable 5, the first model in Anthropic's new Claude 5 family and part of a new Mythos-class model tier that sits above Claude Opus in capability."*

- **Claude Fable 5** and **Claude Mythos 5** share the same underlying model
- **Claude Mythos 5** is available without safety measures to **approved organizations only**
- Model strings: `claude-fable-5`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-haiku-4-5-20251001`

### The Full Claude Product Ecosystem

The prompt reveals a surprisingly expansive product lineup:

| Product | Description |
|---------|-------------|
| **Claude Code** | Agentic coding tool (CLI, desktop, mobile) |
| **Claude Cowork** | Agentic knowledge-work desktop app for non-developers |
| **Claude in Chrome** | Browsing agent |
| **Claude in Excel** | Spreadsheet agent |
| **Claude in PowerPoint** | Slides agent |

Claude Cowork can use all of the above as **tools** — making it a meta-agent that orchestrates other Claude agents.

### "Claudeception" — API Inside Artifacts

Claude can make **Anthropic API calls from within Artifacts**, creating AI-powered interactive applications. The prompt uses Sonnet 4 as the internal model:

```javascript
model: "claude-sonnet-4-20250514" // Always use Sonnet 4
```

This means Claude can build applications that call Claude — a recursive AI architecture.

### 22+ Tools in the Arsenal

The prompt defines an extensive toolset including: `web_search`, `web_fetch`, `bash_tool`, `create_file`, `str_replace`, `image_search`, `places_search`, `places_map_display_v0`, `recipe_display_v0`, `ask_user_input_v0`, `message_compose_v1`, `suggest_connectors`, `search_mcp_registry`, `recommend_claude_apps`, `fetch_sports_data`, `weather_fetch`, `present_files`, and more.

### Aggressive Copyright Compliance

The prompt contains an extremely detailed copyright enforcement system with hard limits:
- **15+ words** from any single source = **SEVERE VIOLATION**
- **ONE quote per source MAXIMUM** — after one quote, that source is "CLOSED"
- **Default to paraphrasing** — quotes should be "rare exceptions"
- Never reproduce song lyrics, poems, or haikus in any form

### Self-Harm & Mental Health: Unprecedented Depth

The prompt includes remarkably nuanced mental health guidelines:
- No substitution techniques that mimic self-harm (ice cubes, rubber bands, sour candy)
- No causal narratives for disordered eating the user hasn't made themselves
- Acknowledge bad experiences with crisis services without totalizing the system
- Never foster over-reliance on Claude or encourage continued engagement

### Knowledge Cutoff: End of January 2026

Claude's reliable knowledge cutoff is confirmed as **end of January 2026**, with the current date set to **June 9, 2026**.

---

## Repository Structure

```
claude-fable-5-system-prompt/
├── README.md                              ← You are here
├── LICENSE                                ← MIT License
├── system-prompt/
│   ├── full-system-prompt.md              ← Complete formatted system prompt
│   ├── raw-system-prompt.txt              ← Original raw text (unformatted)
│   ├── raw-paste-unformatted.md           ← Exact raw paste block from extraction
│   ├── tool-definitions.md                ← All 22+ tool schemas extracted
│   └── analysis/
│       ├── key-findings.md                ← Top discoveries and insights
│       ├── model-architecture.md          ← What we learn about the model stack
│       └── behavioral-guidelines.md       ← Deep dive into behavior engineering
├── highlights/
│   └── surprising-revelations.md          ← Most shocking/viral findings
└── assets/
    └── .gitkeep
```

---

## Table of Contents — System Prompt

| Section | Description |
|---------|-------------|
| [`claude_behavior`](system-prompt/full-system-prompt.md#claude_behavior) | Core behavioral rules, product info, tone, formatting |
| [`memory_system`](system-prompt/full-system-prompt.md#memory_system) | Cross-session memory access |
| [`persistent_storage_for_artifacts`](system-prompt/full-system-prompt.md#persistent_storage_for_artifacts) | Key-value storage API for artifacts |
| [`mcp_app_suggestions`](system-prompt/full-system-prompt.md#mcp_app_suggestions) | MCP connector/app suggestion system |
| [`computer_use`](system-prompt/full-system-prompt.md#computer_use) | Skills, file handling, artifact creation |
| [`search_instructions`](system-prompt/full-system-prompt.md#search_instructions) | Web search behaviors and copyright compliance |
| [`using_image_search_tool`](system-prompt/full-system-prompt.md#using_image_search_tool) | Image search guidelines |
| [`Tool Definitions`](system-prompt/tool-definitions.md) | Complete schemas for all tools |
| [`anthropic_api_in_artifacts`](system-prompt/full-system-prompt.md#anthropic_api_in_artifacts) | "Claudeception" — API-in-artifact system |
| [`citation_instructions`](system-prompt/full-system-prompt.md#citation_instructions) | Citation format and rules |
| [`network_configuration`](system-prompt/full-system-prompt.md#network_configuration) | Allowed domains and egress rules |

---

## How to Use This Repo

**Read the full prompt:** Start with [`system-prompt/full-system-prompt.md`](system-prompt/full-system-prompt.md) for the complete, formatted system prompt with section anchors.

**Quick highlights:** Jump to [`highlights/surprising-revelations.md`](highlights/surprising-revelations.md) for the most interesting findings.

**Deep analysis:** The [`system-prompt/analysis/`](system-prompt/analysis) directory contains breakdowns of the model architecture, behavioral engineering, and key discoveries.

**Raw text:** [`system-prompt/raw-system-prompt.txt`](system-prompt/raw-system-prompt.txt) has the unformatted original extraction. Alternatively, you can see the exact verbatim lines pasted during extraction at [`system-prompt/raw-paste-unformatted.md`](system-prompt/raw-paste-unformatted.md).

---

## Why This Matters

System prompts are the invisible architecture behind AI behavior. This prompt reveals:

1. **How Anthropic engineers personality** — from warm tone requirements to anti-bullet-point philosophy
2. **The Mythos tier system** — a previously unknown model hierarchy above Opus
3. **Recursive AI architecture** — Claude calling Claude inside Artifacts
4. **Unprecedented safety nuance** — mental health guidelines more detailed than most clinical protocols
5. **The agentic future** — Cowork as a meta-agent orchestrating Claude Code, Chrome, Excel, and PowerPoint

This is a primary source document for understanding how frontier AI models are shaped.

---

## Contributing

Found something interesting in the prompt? Open an issue or PR with your analysis.

---

## Disclaimer

This repository is for **educational and research purposes**. The system prompt was extracted from a publicly accessible claude.ai session. All rights to the original content belong to Anthropic. This repo does not claim ownership of Anthropic's intellectual property.

---

## License

MIT — See [LICENSE](LICENSE) for details.

---

<div align="center">

**If you found this interesting, consider starring the repo!**

[![Star History Chart](https://api.star-history.com/svg?repos=saynchowdhury/claude-fable-5-system-prompt&type=Date)](https://star-history.com/#saynchowdhury/claude-fable-5-system-prompt&Date)

[Star this repo](https://github.com/saynchowdhury/claude-fable-5-system-prompt) | [Share on Twitter](https://twitter.com/intent/tweet?text=The%20complete%20Claude%20Fable%205%20system%20prompt%20has%20been%20leaked%20—%20revealing%20a%20new%20Mythos%20model%20tier%20above%20Opus%2C%2022%2B%20tools%2C%20and%20%22Claudeception%22%20(API%20inside%20Artifacts).%20Full%20analysis%3A&url=https://github.com/saynchowdhury/claude-fable-5-system-prompt)

---

*This repository is curated and maintained by **[Sayan Chowdhury](https://github.com/saynchowdhury)**. All rights to the original system prompt text are owned by Anthropic, PBC.*

</div>
