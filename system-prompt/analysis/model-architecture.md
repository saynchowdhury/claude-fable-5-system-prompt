# Model Architecture Insights

<!-- Extracted and analyzed by Sayan Chowdhury (https://github.com/saynchowdhury) -->

This document analyzes what the Claude Fable 5 system prompt reveals about the model's architecture, hierarchy, tooling, and infrastructure. While system prompts are behavioral instructions rather than technical specifications, they contain substantial clues, analyzed here by **[Sayan Chowdhury](https://github.com/saynchowdhury)**, about the underlying engineering decisions and system design.

---

## 1. Model Hierarchy: The Complete Claude 5 Lineup

The system prompt reveals the full model hierarchy as of mid-2026. Listed from least to most capable:

- **Claude Haiku 4.5** (model string: `claude-haiku-4-5-20251001`) -- the lightweight, fast model
- **Claude Sonnet 4.6** (model string: `claude-sonnet-4-6`) -- the balanced mid-tier model
- **Claude Opus 4.8** (model string: `claude-opus-4-8`) -- the previously top-tier model
- **Claude Fable 5 / Claude Mythos 5** (model string: `claude-fable-5`) -- the new Mythos-class frontier

Several observations emerge from this hierarchy. The version numbers suggest different release cadences for different tiers: Haiku is at 4.5, Sonnet at 4.6, and Opus at 4.8, implying that Opus has received more point releases than the lighter models. The jump from the 4.x family to the 5 family for Fable/Mythos suggests a generational leap rather than an incremental update.

The Haiku 4.5 model string includes a date suffix (`20251001`, suggesting October 1, 2025), while the others do not. This is consistent with Anthropic's existing practice of including date-based version identifiers for some models but using simpler strings for newer releases. The prompt notes that "the person is able to switch models mid-conversation, so previous messages claiming to be from a different model or to have a different knowledge cutoff may be accurate," implying that the conversation platform supports dynamic model switching within a single session.

---

## 2. The Mythos-Class Designation

The "Mythos-class" designation is a new architectural category in Anthropic's model taxonomy. The prompt explicitly positions it: "part of a new Mythos-class model tier that sits above Claude Opus in capability." This is not simply a model name but a classification of capability level.

What makes a model Mythos-class? While the prompt does not define the criteria explicitly, several inferences are possible. First, the model has "dual-use capabilities" that require "additional safety measures" for general release. This suggests capabilities that could be misused at scale, possibly including advanced code generation, autonomous agent behavior, sophisticated reasoning about security systems, or other domains where high capability creates genuine risk.

Second, the model is described as the most capable in Anthropic's lineup, above even Opus 4.8. Given that Opus has historically been Anthropic's most capable tier (designed for complex reasoning, long-form content, and difficult tasks), a tier above Opus represents a significant capability threshold.

The Mythos-class designation may also carry architectural implications. It is possible that Mythos-class models use a different architecture, larger parameter count, longer context windows, or different training methodologies compared to the standard tiers. The separate classification suggests these models are not simply larger versions of existing models but represent a qualitatively different approach.

---

## 3. Fable vs Mythos: Same Model, Different Safety Configurations

The prompt states clearly: "Claude Fable 5 and Claude Mythos 5 share the same underlying model." This is architecturally significant because it confirms that the difference between these two products is not model weights or architecture but safety configuration.

Claude Fable 5 "includes additional safety measures for dual-use capabilities." This suggests a safety layer or filter that is applied at inference time, possibly through additional system prompt instructions, output classifiers, refusal fine-tuning, or runtime guardrails that intercept certain types of requests or outputs.

Claude Mythos 5 is "available without those measures to only approved organizations." The access control is at the organizational level: only vetted institutions can access the unrestricted version. This implies an enterprise or government sales channel with contractual safeguards.

The architectural implication is that Anthropic has developed a modular safety system where the same base model can be deployed with different safety profiles. This is more efficient than training separate models and ensures that safety updates apply uniformly. It also means that the "true" capability level of the model is what Mythos 5 offers; Fable 5 is a deliberately constrained version.

This approach is analogous to how operating systems ship with different security profiles for consumer and enterprise use, or how cloud services offer different feature sets based on subscription tier, except here the gating is about safety rather than features.

---

## 4. Model Strings and Versioning Scheme

The versioning scheme visible in the model strings reveals Anthropic's approach to model identity and lifecycle management:

```
claude-fable-5
claude-opus-4-8
claude-sonnet-4-6
claude-haiku-4-5-20251001
```

The pattern follows `{provider}-{tier}-{major}-{minor}[-{date}]`. The inclusion of the date suffix on Haiku but not on other models may indicate that date-stamped strings are used during initial rollout and transitioned to simpler strings once the model is stable. Alternatively, it may indicate that Haiku 4.5 has a specific snapshot version that needs to be distinguished from other Haiku 4.x variants.

The versioning also implies a major/minor version system where the major version (4 or 5) represents the model generation and the minor version (5, 6, 8) represents point releases or fine-tuning iterations within that generation. The jump from generation 4 to generation 5 appears to coincide with the introduction of the Mythos-class tier.

The fact that the model string for Fable 5 is simply `claude-fable-5` without a minor version number suggests this is the first release in the Fable line, consistent with the prompt describing it as "the first model in Anthropic's new Claude 5 family."

---

## 5. Internal API Architecture: Sonnet 4 in Artifacts

The "Claudeception" feature reveals the internal API architecture. When Claude creates an Artifact that makes API calls, it uses the standard Anthropic `/v1/messages` endpoint with a fixed model selection:

```javascript
model: "claude-sonnet-4-20250514"
```

This is notable for several reasons. First, the model used inside artifacts is Sonnet 4 (with a date stamp of May 14, 2025), not Sonnet 4.6 or any newer version. This may indicate that the Artifact API integration was built against Sonnet 4 and has not been updated, or that Sonnet 4 offers the best balance of speed and cost for in-artifact inference.

Second, no API key is passed in the request. The prompt states: "The assistant should never pass in an API key, as this is handled already." This means the authentication is injected at the platform level, likely by the Artifact runtime environment. The user's Claude subscription presumably covers the cost of these nested API calls, or Anthropic absorbs them as a platform feature.

Third, the `max_tokens` parameter is always set to 1000, with the prompt noting "This is being handled already." This suggests the platform enforces its own token limits regardless of what the artifact code requests, preventing runaway costs.

The API also supports structured outputs (JSON mode), web search tools, MCP server integration, and multi-modal inputs (images and PDFs as base64). The full conversation history must be sent with each request since "Claude has no memory between completions."

The web search tool within the artifact API uses the version string `web_search_20250305`, suggesting a specific dated version of the search tool is available for programmatic access.

---

## 6. Tool Ecosystem: 22+ Tools with MCP Integration

The system prompt defines a rich tool ecosystem that Claude can invoke. Counting all tools mentioned:

**Core interaction tools:**
- `ask_user_input_v0` -- present tappable options for user preferences
- `message_compose_v1` -- draft emails, texts, or other messages
- `present_files` -- make files visible to the user
- `recommend_claude_apps` -- suggest Claude ecosystem apps

**Code execution tools:**
- `bash_tool` -- run bash commands in an Ubuntu 24 container
- `create_file` -- create new files with content
- `str_replace` -- edit existing files with string replacement
- `view` -- view files, images, or directory listings

**Information retrieval tools:**
- `web_search` -- search the web (Anthropic's own search integration)
- `web_fetch` -- fetch and extract web page content
- `image_search` -- find images on the web
- `fetch_sports_data` -- sports scores, standings, and stats
- `weather_fetch` -- weather information

**Location tools:**
- `places_search` -- Google Places search
- `places_map_display_v0` -- display locations on maps with itineraries

**Specialized tools:**
- `recipe_display_v0` -- interactive recipe display with serving adjustment

**MCP ecosystem tools:**
- `search_mcp_registry` -- discover available MCP connectors
- `suggest_connectors` -- present connector options to users

This yields at least 16 directly defined tools, plus the MCP ecosystem which can dynamically add more. The prompt mentions that MCP App tools are "identified by descriptions that begin with the tag `[third_party_mcp_app]`," indicating that MCP tools are dynamically injected into the tool list at runtime based on what the user has connected.

The `suggest_connectors` tool works via UUIDs from the `search_mcp_registry` results, suggesting a registry-based architecture where connectors are discovered, presented, and activated through a structured flow. The prompt also references `tool_search` as a way to find tools, suggesting there may be a meta-tool for discovering available capabilities.

The architecture separates internal tools (Google Drive, Slack, Gmail) from external tools (web search, web fetch) from consumer partner tools (third-party MCP apps). Internal tools are prioritized over web search for company-personal data, and consumer partner tools always require user opt-in.

Additionally, the prompt references an `end_conversation` tool and a `navigate` tool (for browser-based actions), neither of which are fully defined in the visible portion of the prompt but are clearly part of the tool ecosystem.

---

## 7. Knowledge Cutoff and Date Injection System

The knowledge cutoff system reveals how Anthropic manages temporal awareness in their models. The prompt contains multiple instances of the current date:

- In the `knowledge_cutoff` section: "Tuesday, June 09, 2026"
- In the `search_usage_guidelines`: "Current date is Tuesday, June 09, 2026"
- In the Identity Preamble: "The current date is Tuesday, June 09, 2026"

The fact that the date appears in multiple locations suggests it is injected programmatically at conversation start, likely through template substitution. The model's training data has a fixed cutoff ("the end of Jan 2026"), and everything after that must be discovered through web search.

The date injection is always the full day-of-week plus date format ("Tuesday, June 09, 2026"), which provides the model with enough context to reason about relative time expressions like "yesterday," "last week," or "next month."

The prompt's instructions for handling the gap between training data and current date are remarkably detailed. Claude should use current year in search queries, search for binary events and current position holders, and "default to searching for questions that appear historical or settled but are phrased in the present tense." This last instruction addresses a subtle failure mode where questions like "does X exist" or "is Y democratic" may have changed since training.

The system also handles the case where the user switches models mid-conversation: "previous messages claiming to be from a different model or to have a different knowledge cutoff may be accurate." This suggests the conversation platform preserves model identity metadata across messages.

---

## 8. Network Configuration and Domain Allowlist

The network architecture for Claude's code execution environment uses an egress proxy with a domain allowlist:

**Package management:**
- npm: `npmjs.com`, `npmjs.org`, `registry.npmjs.org`, `registry.yarnpkg.com`, `www.npmjs.com`, `www.npmjs.org`, `yarnpkg.com`
- Python: `pypi.org`, `files.pythonhosted.org`, `pythonhosted.org`
- Rust: `crates.io`, `index.crates.io`, `static.crates.io`
- Ubuntu: `archive.ubuntu.com`, `security.ubuntu.com`

**Code hosting:**
- GitHub: `github.com`, `api.github.com`, `codeload.github.com`, `raw.githubusercontent.com`

**AI services:**
- Anthropic API: `api.anthropic.com`
- Adobe: `*.adobe.io`, `adobe.io`

The architecture uses a proxy-based egress system where all outbound network traffic from the bash_tool passes through a proxy that checks the destination against the allowlist. Blocked requests return an `x-deny-reason` header, suggesting the proxy provides diagnostic information about why access was denied.

The prompt instructs: "If Claude is not able to access a domain, it should tell the user that they can update their network settings." This implies that users may have some ability to modify the allowlist, though the mechanism is not described in the prompt.

Notable by their absence: no general web domains are allowed. Claude cannot use `curl`, `wget`, or other command-line tools to access arbitrary websites. All web access must go through the dedicated `web_search` and `web_fetch` tools, which enforce copyright compliance, harmful content filtering, and other safety measures. This separation is an architectural enforcement mechanism that ensures all web access is mediated by Anthropic's safety layer.

The inclusion of `api.anthropic.com` enables the Claudeception feature (API calls from artifacts). The Adobe domains suggest integration with Adobe services, possibly for document processing, font rendering, or creative tool integrations.

---

## 9. Filesystem Architecture: Read-Only Mounts and Working Directories

The filesystem architecture uses a multi-directory layout with different access levels:

**Read-only mounts:**
- `/mnt/user-data/uploads` -- files uploaded by the user
- `/mnt/transcripts` -- conversation transcripts or other system data
- `/mnt/skills/public` -- built-in skill definitions
- `/mnt/skills/private` -- private or enterprise skill definitions
- `/mnt/skills/examples` -- example skills (including the skill-creator skill)

**Writable directories:**
- `/home/claude` -- Claude's working directory and scratchpad
- `/mnt/user-data/outputs` -- final output directory visible to the user

The architecture enforces a clear separation between input (read-only), processing (scratchpad), and output (user-visible). User uploads are read-only to prevent accidental modification. The skills directories are read-only to maintain integrity of skill definitions. The outputs directory is the only place where files become visible to the user.

The `present_files` tool serves as the final step in the output pipeline, making files accessible to the user. The prompt emphasizes: "Putting outputs in the outputs directory and calling present_files is essential; without it, users can't see or access their files."

The `str_replace` tool explicitly enforces the read-only constraint: "Files under /mnt/user-data/uploads, /mnt/transcripts, /mnt/skills/public, /mnt/skills/private, /mnt/skills/examples are read-only -- copy them to a writable location first if you need to edit them."

The skills directory structure reveals three tiers: `public` (built-in skills shipped with the platform), `private` (possibly enterprise or user-specific skills with restricted access), and `examples` (demonstration skills including a meta skill-creator that can create new skills). This suggests a skills marketplace or sharing system where skills can be created, distributed, and installed.

The filesystem "resets between tasks," indicating an ephemeral execution environment. This is consistent with container-based architectures where each conversation gets a fresh environment. The `/mnt/user-data/` path prefix suggests a mounted volume that persists across the ephemeral container lifecycle.

---

## 10. Skills System Architecture

The skills system is a sophisticated abstraction layer for document creation and specialized tasks. The prompt describes skills as "folders of best practices for creating different document types" that "encode hard-won trial-and-error about producing professional output."

The built-in skills identified in the prompt are:

- **docx** -- Word document creation and manipulation
- **pdf** -- PDF reading, creation, merging, splitting, form-filling, encryption
- **pptx** -- PowerPoint presentation creation
- **xlsx** -- Spreadsheet creation and manipulation
- **product-self-knowledge** -- Anthropic product facts and details
- **frontend-design** -- UI/UX design guidance for React and web components
- **file-reading** -- Router for reading different file types correctly
- **pdf-reading** -- Specialized PDF inspection and content extraction
- **skill-creator** -- Meta-skill for creating and modifying other skills

Skills are stored at structured paths under `/mnt/skills/` with a standard `SKILL.md` file as the entry point. The prompt mandates: "Reading the relevant SKILL.md is a required first step before writing any code, creating any file, or running any other computer tool."

The architecture is designed to be extensible. User-uploaded skills can exist at `/mnt/skills/user/` and are "very likely relevant" when present. Example skills exist at `/mnt/skills/examples/`. The skill-creator skill can create new skills, modify existing ones, and run evals to test skill performance.

Skills encode "environment-specific constraints (available libraries, rendering quirks, output paths) that aren't in Claude's training data." This is a clever solution to the problem of AI models producing code that doesn't work in specific environments. By reading environment-specific skill files, the model can adapt its output to the constraints of the current deployment.

The prompt emphasizes that "the mapping from task to skill isn't always obvious from the skill name," so Claude must scan the full `available_skills` list and match based on descriptions rather than names alone. The descriptions are detailed and include explicit trigger conditions, negative conditions (when not to use), and cross-references to related skills.

The system also supports dynamic skill availability: "user-provided skills since they're very likely relevant" and may not always be present. This suggests a plugin-like architecture where skills can be installed, uninstalled, or updated without modifying the core system prompt.

---

## Summary

The Claude Fable 5 system reveals a sophisticated, multi-layered architecture that goes far beyond a simple chat interface. The model hierarchy spans four capability tiers plus a new Mythos-class designation. The same base model can be deployed with different safety profiles for different audiences. The tool ecosystem includes over 22 tools spanning code execution, information retrieval, location services, and third-party integrations via MCP. The filesystem uses strict access controls with read-only mounts, ephemeral working directories, and a controlled output pipeline. The network layer uses an egress proxy with domain allowlisting. And the skills system provides an extensible abstraction layer for specialized tasks.

Together, these architectural elements paint a picture of a platform that has been designed for production-grade deployment with careful attention to security, safety, extensibility, and user experience.
