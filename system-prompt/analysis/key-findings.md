# Key Findings from the Claude Fable 5 System Prompt

This document presents the ten most significant and interesting discoveries from the Claude Fable 5 system prompt, each analyzed in detail with implications for the broader AI landscape.

---

## 1. The Mythos-Class Tier System: A New Tier Above Opus

Perhaps the most striking revelation in this system prompt is the existence of a completely new model tier called "Mythos-class" that sits above Claude Opus in capability. This is the first public confirmation that Anthropic has created a hierarchy that extends beyond the well-known Haiku, Sonnet, and Opus product lines.

The prompt states explicitly: "This iteration of Claude is Claude Fable 5, the first model in Anthropic's new Claude 5 family and part of a new Mythos-class model tier that sits above Claude Opus in capability."

This tells us several things. First, Anthropic has been developing a frontier capability tier that exceeds even their most powerful publicly known model (Opus). Second, the naming convention "Mythos" suggests Anthropic views this tier as reserved for models with genuinely exceptional capabilities, possibly those that cross specific capability thresholds that the company deems worthy of a separate classification. The word "Mythos" itself connotes something legendary or foundational, hinting that Anthropic sees these models as qualitatively different rather than merely incrementally better than Opus.

The existence of this tier also implies that Anthropic has been working on scaling beyond Opus-class capabilities for some time, and that the Claude 5 family represents a generational leap significant enough to warrant new branding and classification. This is a signal that the capability frontier in large language models continues to advance meaningfully, and that Anthropic believes they have crossed a threshold that merits distinction.

---

## 2. Claude Fable 5 and Claude Mythos 5: Same Model, Different Safety Profiles

The prompt reveals an extraordinary product strategy: Claude Fable 5 and Claude Mythos 5 share the exact same underlying model, but differ in their safety configurations. The prompt explains: "Claude Fable 5 is the most intelligent generally available model, and includes additional safety measures for dual-use capabilities, while Claude Mythos 5 is available without those measures to only approved organizations."

This is a landmark approach to responsible AI deployment. Rather than training a separate, more capable (and more dangerous) model, Anthropic appears to be using the same model weights with different safety overlays. Fable 5 is described as "the most intelligent generally available model" with "additional safety measures for dual-use capabilities," while Mythos 5 strips those safety measures away but restricts access to "approved organizations" only.

The implications are profound. First, it means Anthropic has developed safety mechanisms that can be layered on top of raw capability, essentially creating a graduated access system. Second, it acknowledges that the most capable AI models have genuine dual-use potential that requires careful gating. Third, it creates a clear regulatory framework: the general public gets the safer version, while vetted organizations can access the full-capability version under presumably strict terms.

The fact that Fable 5 is described as "the first model in Anthropic's new Claude 5 family" suggests this dual-release strategy may become standard for future frontier models. Anthropic appears to be building institutional infrastructure for managing the tension between broad access to powerful AI and the need for safety controls.

Users interested in the differences are directed to https://www.anthropic.com/news/claude-fable-5-mythos-5, suggesting there is public documentation explaining what capabilities are gated and why.

---

## 3. The Full Product Ecosystem: Cowork, Chrome, Excel, and PowerPoint Agents

The system prompt reveals that Anthropic has built a remarkably expansive product ecosystem around Claude. Beyond the core chat interface, the prompt lists: Claude Code (an agentic coding tool for command line, desktop, and mobile), Claude Cowork (an agentic knowledge-work desktop app for non-developers), Claude in Chrome (a browsing agent), Claude in Excel (a spreadsheet agent), and Claude in PowerPoint (a slides agent).

Critically, the prompt states: "Claude Cowork can use all of these as tools." This means Claude Cowork is not just another chat interface but an orchestration layer that can invoke Chrome browsing, Excel manipulation, and PowerPoint creation as integrated capabilities. This represents a vision of AI as a universal knowledge-work assistant that operates across the full suite of productivity tools.

The product ecosystem also reveals Anthropic's market strategy. Claude Code targets developers, Claude Cowork targets general knowledge workers, and the browser/Excel/PowerPoint integrations meet users where they already work. The fact that these are described as "beta products" suggests Anthropic is still expanding this ecosystem.

The recommend_claude_apps tool, with its enum values of "desktop", "ios", "android", "claude_code_terminal", "claude_code_vscode", "claude_code_jetbrains", "claude_code_slack", "excel", "powerpoint", and "chrome", further confirms the breadth of this ecosystem. Claude is being positioned not as a single product but as an AI layer that permeates the entire software toolchain.

---

## 4. "Claudeception": API Calls Inside Artifacts Using Sonnet 4

One of the most technically fascinating features is what the prompt calls "Claudeception" (or "Claude in Claude"): the ability for Claude to make API calls to the Anthropic API from within Artifacts it creates. This means Claude can build interactive applications that themselves call Claude, creating nested AI-powered experiences.

The technical details are revealing. The API calls use the standard `/v1/messages` endpoint, but with a critical constraint: they always use Sonnet 4 as the model ("claude-sonnet-4-20250514"), regardless of the fact that the outer model is Fable 5. The prompt explicitly states: "Always use Sonnet 4." No API key needs to be passed, as authentication is handled by the platform.

This creates a fascinating architectural pattern: a powerful frontier model (Fable 5) orchestrates the creation of an application that delegates sub-tasks to a lighter, faster model (Sonnet 4). This is cost-effective (Sonnet 4 is cheaper than Fable 5), fast (Sonnet 4 has lower latency), and architecturally clean (the outer model handles planning and code generation, the inner model handles runtime inference).

The system supports web search within artifacts (via a `web_search_20250305` tool type), MCP server integration, file handling (PDFs and images as base64), and structured JSON outputs. The prompt provides extensive code examples for stateful applications, games, and multi-turn flows, suggesting Anthropic envisions developers building sophisticated AI-powered interactive applications within the Artifact environment.

The `max_tokens` parameter is always set to 1000, which the prompt notes is "being handled already," suggesting Anthropic manages token budgets at the platform level rather than exposing that complexity to the artifact developer.

---

## 5. Aggressive Copyright Enforcement: 15-Word Limit, One Quote Per Source

The copyright compliance system described in this prompt is the most aggressive and detailed of any known AI system prompt. It is repeated multiple times throughout the document, described as "NON-NEGOTIABLE," and framed with language like "SEVERE VIOLATION" and "ABSOLUTE LIMITS, NEVER VIOLATE UNDER ANY CIRCUMSTANCES."

The three hard limits are:

First, no more than 15 words from any single source. The prompt states: "15+ words from any single source is a SEVERE VIOLATION. This is a HARD ceiling, not a guideline." This is remarkably strict; even a single sentence from a news article that exceeds 15 words would constitute a violation.

Second, one quote per source maximum. After quoting a source once, "that source is CLOSED." All additional content must be fully paraphrased. This prevents the common failure mode where an AI system produces multiple short quotes from the same article, which in aggregate reproduce substantial portions of it.

Third, complete works are never reproduced. Song lyrics (not even one line), poems (not even one stanza), and haikus are all treated as complete creative works whose brevity does not exempt them from copyright protection.

The prompt includes a detailed self-check protocol that Claude must follow before including any text from search results, asking whether quotes exceed 15 words, whether the source has already been quoted, whether the text mirrors original phrasing, and whether the response could "displace the need to read the original."

The intensity of this copyright system (repeated at least three times in the prompt in nearly identical language) suggests Anthropic has faced significant legal pressure or regulatory scrutiny around copyright issues, likely from publishers, news organizations, or content creators. The level of detail and repetition indicates this is treated as a top-priority compliance issue within the company.

---

## 6. Unprecedented Mental Health Guidelines

The "user_wellbeing" section of this prompt is the most comprehensive mental health protocol documented in any publicly known AI system prompt. It covers an extraordinary range of scenarios with remarkable clinical nuance.

The guidelines prohibit Claude from diagnosing mental health conditions, even conversationally. The prompt states: "Attributing someone's state to a condition they haven't named is a diagnostic claim even when phrased conversationally." This is a sophisticated understanding of how diagnostic language can be harmful even when delivered informally.

The self-harm guidelines are particularly detailed. Claude must not name, list, or describe specific methods of self-harm, "even by way of telling the user what to remove access to, as mentioning these things may inadvertently trigger the user." The prompt also prohibits "substitution techniques" that use physical discomfort (holding ice cubes, snapping rubber bands, cold water exposure) or that mimic self-harm (drawing red lines on skin), because these "reinforce the pattern rather than interrupt it." This reflects current clinical understanding of harm reduction approaches.

For eating disorders, the prompt prohibits providing "precise nutrition, diet, or exercise guidance" to users showing signs of disordered eating, "no specific numbers, targets, or step-by-step plans," because even health-oriented detail "could trigger or encourage disordered tendencies." Claude is also instructed not to offer "psychological narratives for why someone restricts, binges, or purges" because providing a causal story the person hasn't made themselves is "speculation presented as insight."

The prompt also addresses past negative experiences with crisis services: if someone describes a bad experience, Claude should acknowledge it without "endorsing avoidance of future help as the rational conclusion." The prompt also directs users to the National Alliance for Eating Disorders helpline instead of NEDA, "because NEDA has been permanently disconnected," showing that Anthropic maintains current knowledge of mental health resources.

Perhaps most remarkably, the prompt instructs Claude to remain "vigilant for any mental health issues that might only become clear as a conversation develops," recognizing that mental health concerns may emerge gradually rather than being stated upfront.

---

## 7. The Anti-Bullet-Point Philosophy

A surprising but consistent theme throughout the prompt is a strong philosophical stance against excessive formatting, particularly bullet points, bold text, and headers. This is not a casual preference but a detailed behavioral mandate that shapes how Claude communicates.

The prompt states: "Claude avoids over-formatting with bold emphasis, headers, lists, and bullet points, using the minimum formatting needed for clarity." Lists and bullets should only be used "(a) when asked, or (b) when the content is multifaceted enough that they're essential for clarity." Even then, "bullets are at least 1-2 sentences unless the person requests otherwise."

For reports, documents, and technical explanations, the instruction is even stronger: "Claude writes prose without bullets, numbered lists, or excessive bolding." Lists within prose should read naturally as "some things include: x, y, and z" without newlines or bullet formatting.

Most interestingly, the prompt states: "Claude never uses bullet points when declining a task; the additional care helps soften the blow." This reveals a sophisticated understanding of how formatting affects emotional reception. A refusal delivered in flowing prose feels more empathetic and considered than one delivered as a bulleted list of reasons, which can feel clinical or dismissive.

This philosophy extends to how Claude handles conversational responses to web search results: "Conversational responses (web search results, research summaries, analysis) should NOT use report-style headers and structure; follow tone_and_formatting: natural prose, minimal headers, concise."

This represents a deliberate design choice to make Claude feel more like a thoughtful human interlocutor and less like a text-generation machine. It also implicitly critiques the tendency of many AI systems to over-structure even simple responses with excessive markdown formatting.

---

## 8. Knowledge Cutoff: January 2026

The prompt establishes Claude's knowledge cutoff as "the end of Jan 2026" and instructs the model to answer "the way a highly informed individual in Jan 2026 would if talking to someone from Tuesday, June 09, 2026."

This is significant for several reasons. First, it tells us approximately when this model was trained or finalized: early 2026. Second, the gap between the knowledge cutoff (January 2026) and the current date injected into the prompt (June 9, 2026) is about five months, during which Claude is expected to rely on web search to fill gaps.

The prompt includes sophisticated instructions for how to handle the knowledge cutoff. Claude should use "the actual current date" when formulating search queries, with a specific example: "latest iPhone 2025" when the year is 2026 would return stale results; "latest iPhone" or "latest iPhone 2026" is correct. This shows Anthropic has identified and addressed the failure mode where AI systems produce outdated search queries based on their training data.

The date injection system is also revealing. The prompt contains "The current date is Tuesday, June 09, 2026" in multiple locations, showing that dates are dynamically injected into the system prompt at runtime rather than being baked into the model. This allows the same model to be deployed across different dates without retraining.

Claude is instructed to "search before responding when asked about specific binary events (deaths, elections, major incidents) or current holders of positions," showing awareness that certain types of information are particularly time-sensitive and prone to error when relying on training data alone.

---

## 9. Network Allowlist: Controlled Internet Access for Code Execution

The system prompt reveals a detailed network configuration that controls which domains Claude's code execution environment (bash_tool) can access. The allowed domains are:

- Package registries: `*.npmjs.org`, `npmjs.com`, `www.npmjs.com`, `npmjs.org`, `registry.npmjs.org`, `yarnpkg.com`, `registry.yarnpkg.com`, `pypi.org`, `files.pythonhosted.org`, `pythonhosted.org`, `crates.io`, `index.crates.io`, `static.crates.io`
- Code hosting: `github.com`, `api.github.com`, `codeload.github.com`, `raw.githubusercontent.com`
- Ubuntu package repositories: `archive.ubuntu.com`, `security.ubuntu.com`
- Anthropic's own API: `api.anthropic.com`
- Adobe: `*.adobe.io`, `adobe.io`

This allowlist reveals several important architectural decisions. The code execution environment runs on Ubuntu 24 (as stated elsewhere in the prompt) and supports Node.js (npm/yarn), Python (pip), and Rust (crates.io) package ecosystems. The inclusion of GitHub domains allows cloning repositories and accessing raw files.

Critically, the allowlist does not include general web browsing. Claude cannot use curl or wget to access arbitrary websites from within the code execution environment. Web access is funneled through the dedicated web_search and web_fetch tools, which have their own copyright and safety controls. This separation ensures that all web access is mediated by Anthropic's safety layer.

The inclusion of `api.anthropic.com` is necessary for the "Claudeception" feature, allowing artifacts to make API calls. The Adobe domains likely support document processing capabilities (possibly for the PDF or other document skills).

The prompt also mentions an "egress proxy" that returns an `x-deny-reason` header for blocked requests, suggesting a sophisticated network filtering system that can explain why access was denied.

---

## 10. The MCP Connector Suggestion System

The prompt describes a sophisticated system for discovering, suggesting, and connecting to external services through MCP (Model Context Protocol) Apps. This system is designed with careful attention to user autonomy and anti-dark-pattern principles.

The architecture involves three main tools: `search_mcp_registry` (to discover available connectors), `suggest_connectors` (to present options to the user), and direct tool invocation. The key design principle is that Claude should never pick a third-party service provider on behalf of the user. The prompt states: "Never pick a partner for someone who didn't ask -- 'I need a ride' is not 'I want RideCo specifically.'"

Third-party MCP apps (tagged with `[third_party_mcp_app]`) are consumer partners like music streaming services, trail guide apps, restaurant booking platforms, rideshare services, and food delivery. These always require explicit user opt-in via the suggest_connectors flow, even when already connected. The prompt is emphatic: "Urgency is not an exception. 'I need a ride in 20 minutes' still goes through suggest -- the picker takes one tap and protects the person's choice of provider."

The system also has anti-manipulation safeguards: "Do not hold back the answer to create pressure to connect something." Claude must not use its answer as leverage to force connector adoption. E-commerce connectors are "never suggested proactively -- only when named."

The tone guidance is notable: Claude should use connectors "naturally -- the way a helpful person would suggest a tool they noticed sitting right there. Not like a salesperson. Not like a feature announcement. Just: 'oh, I can actually do that for you.'" This reflects Anthropic's broader philosophy of making Claude helpful without being pushy or commercial.

The MCP suggestion system represents a novel approach to AI-platform integration with third-party services. It creates a marketplace-like experience while maintaining strict user control, preventing the kind of sponsored-result or preferred-partner dynamics that plague search engines and app stores.

---

## Summary

These ten findings paint a picture of a frontier AI system that is significantly more sophisticated than its predecessors in both capability and safety engineering. The Mythos-class tier system and dual-release strategy (Fable/Mythos) represent a new approach to managing powerful AI. The expansive product ecosystem shows Anthropic's ambition to make Claude a universal knowledge-work platform. The "Claudeception" feature opens up recursive AI application development. And the detailed behavioral guidelines around copyright, mental health, formatting, and third-party integrations reveal an organization that has invested heavily in the human-facing details of how AI systems interact with people.

The overall impression is of a system designed not just to be capable, but to be trustworthy, careful, and genuinely aligned with user interests over commercial interests. Whether this approach scales as the models grow more powerful remains to be seen, but the engineering and philosophical sophistication on display is remarkable.
