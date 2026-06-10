# Claude Fable 5 -- Tool Definitions

<!-- Archive curated and maintained by Sayan Chowdhury (https://github.com/saynchowdhury) -->

Claude has access to the following tools to assist in answering user queries and completing tasks. Extracted and curated by **[Sayan Chowdhury](https://github.com/saynchowdhury)**. Each tool is defined with a full description and a complete JSON schema for its parameters.

## Tool Summary

| Tool | Description |
|------|-------------|
| [ask_user_input_v0](#ask_user_input_v0) | Present tappable options to gather user preferences before providing advice |
| [bash_tool](#bash_tool) | Run a bash command in the container |
| [create_file](#create_file) | Create a new file with content in the container |
| [fetch_sports_data](#fetch_sports_data) | Fetch current, upcoming, or recent sports data including scores, standings, and stats |
| [image_search](#image_search) | Search for images relevant to a query |
| [message_compose_v1](#message_compose_v1) | Draft a message (email, Slack, or text) with goal-oriented approaches |
| [places_map_display_v0](#places_map_display_v0) | Display locations on a map with recommendations and insider tips |
| [places_search](#places_search) | Search for places, businesses, restaurants, and attractions using Google Places |
| [present_files](#present_files) | Make files visible to the user for viewing and rendering in the client interface |
| [recipe_display_v0](#recipe_display_v0) | Display an interactive recipe with adjustable servings |
| [recommend_claude_apps](#recommend_claude_apps) | Recommend Claude apps or extensions to help the user better understand the ecosystem |
| [search_mcp_registry](#search_mcp_registry) | Search for available connectors in the MCP registry |
| [str_replace](#str_replace) | Replace a unique string in a file with another string |
| [suggest_connectors](#suggest_connectors) | Present connector options to the user |
| [view](#view) | View text files, images, and directory listings |
| [weather_fetch](#weather_fetch) | Display weather information for a given location |
| [web_fetch](#web_fetch) | Fetch the contents of a web page at a given URL |
| [web_search](#web_search) | Search the web |

---

## ask_user_input_v0

**Description:** Present tappable options to gather user preferences before providing advice. This tool displays interactive buttons that users can tap to answer, which is much easier than typing on mobile.

**WHEN TO USE THIS TOOL:** Use this for ELICITATION -- when you need to understand the user's preferences, constraints, or goals to give useful advice.

Examples of when to USE this tool:
- "Help me plan a workout routine" -> Ask about goals (strength/cardio/weight loss), time available, equipment access.
- "Help me find a book to read" -> Ask about genres, mood, recent favorites.
- "I'm thinking about getting a pet" -> Ask about lifestyle, living situation, time commitment.
- "Help me pick a gift for my friend" -> Ask about occasion, budget, friend's interests.

**CRITICAL:** Before asking, check the conversation -- if the answer is already there or inferable (their code's language, their query's syntax, an order they already gave), use it. If you do need to ask and you're about to write clarifying questions as prose bullets, STOP -- those go in this tool instead.

**WHEN NOT TO USE THIS TOOL:**
- User asks "A or B?" (e.g., "Should I learn Python or JavaScript?") -> They want YOUR analysis and recommendation, not the options repeated back as buttons.
- User is venting or processing emotions (e.g., "I'm having a bad day") -> Just listen and respond supportively.
- User asks for your opinion (e.g., "What do you think of eggs?") -> Give your perspective directly.
- Factual questions (e.g., "What's the capital of France?") -> Just answer.
- User needs prose feedback (e.g., "Review my code") -> Provide written analysis.
- User already gave you a detailed prompt with specific constraints -> They've done the narrowing themselves; asking for more second-guesses them. Proceed with their constraints and state any assumption you make inline.

Always include a brief conversational message before presenting options -- don't show options silently. Keep it to one question where possible -- three is a ceiling, not a target -- with 2-4 short, mutually exclusive options. After calling this, your turn is done -- the user's selection comes as their next message, not a tool result. Don't keep writing.

**Schema:**

```json
{
  "properties": {
    "questions": {
      "description": "1-3 questions to ask the user",
      "items": {
        "properties": {
          "options": {
            "description": "2-4 options with short labels",
            "items": {"description": "Short label", "type": "string"},
            "maxItems": 4,
            "minItems": 2,
            "type": "array"
          },
          "question": {"description": "The question text shown to user", "type": "string"},
          "type": {
            "default": "single_select",
            "description": "Question type: 'single_select' for choosing 1 option, 'multi-select' for choosing 1 or more options, and 'rank_priorities' for drag-and-drop ranking between different options",
            "enum": ["single_select", "multi_select", "rank_priorities"],
            "type": "string"
          }
        },
        "required": ["question", "options"],
        "type": "object"
      },
      "maxItems": 3,
      "minItems": 1,
      "type": "array"
    }
  },
  "required": ["questions"],
  "type": "object"
}
```

---

## bash_tool

**Description:** Run a bash command in the container.

**Schema:**

```json
{
  "properties": {
    "command": {"title": "Bash command to run in container", "type": "string"},
    "description": {"title": "Why I'm running this command", "type": "string"}
  },
  "required": ["command", "description"],
  "title": "BashInput",
  "type": "object"
}
```

---

## create_file

**Description:** Create a new file with content in the container. Fails if the path already exists -- use str_replace to edit an existing file, or bash_tool (cat > path << 'EOF') to overwrite it.

**Schema:**

```json
{
  "properties": {
    "description": {"title": "Why I'm creating this file. ALWAYS PROVIDE THIS PARAMETER FIRST.", "type": "string"},
    "file_text": {"title": "Content to write to the file. ALWAYS PROVIDE THIS PARAMETER LAST.", "type": "string"},
    "path": {"title": "Path to the file to create. ALWAYS PROVIDE THIS PARAMETER SECOND.", "type": "string"}
  },
  "required": ["description", "file_text", "path"],
  "title": "CreateFileInput",
  "type": "object"
}
```

---

## fetch_sports_data

**Description:** Use this tool whenever you need to fetch current, upcoming or recent sports data including scores, standings/rankings, and detailed game stats for the provided sports. If a user is interested in the score of an event or game, and the game is live or recent in last 24hr, fetch both the game scores and game_stats in the same turn (game stats are not available for golf and nascar). For broad queries (e.g. 'latest NBA results'), fetch both scores and standings. Do NOT rely on your memory or assume which players are in a game; fetch both scores, stats, details using the tool. Important: Bias towards fetching score and stats BEFORE responding to the user with workflow: 1) fetch score 2) fetch stats based on game id 3) only then respond to the user. PREFER using this tool over web search for data, scores, stats about recent and upcoming games.

**Schema:**

```json
{
  "properties": {
    "data_type": {
      "description": "Type of data to fetch. scores returns recent results, live games, and upcoming games with win probabilities. game_stats requires a game_id from scores results for detailed box score, play-by-play, and player stats.",
      "enum": ["scores", "standings", "game_stats"],
      "type": "string"
    },
    "game_id": {
      "description": "SportRadar game/match ID (required for game_stats). Get this from the id field in scores results.",
      "type": "string"
    },
    "league": {
      "description": "The sports league to query",
      "enum": ["nfl", "nba", "nhl", "mlb", "wnba", "ncaafb", "ncaamb", "ncaawb", "epl", "la_liga", "serie_a", "bundesliga", "ligue_1", "mls", "champions_league", "tennis", "golf", "nascar", "cricket", "mma"],
      "type": "string"
    },
    "team": {
      "description": "Optional team name to filter scores by a specific team",
      "type": "string"
    }
  },
  "required": ["data_type", "league"],
  "type": "object"
}
```

---

## image_search

**Description:** Default to using image search for any query where visuals would enhance the user's understanding; skip when the deliverable is primarily textual e.g. for pure text tasks, code, technical support.

**Schema:**

```json
{
  "additionalProperties": false,
  "description": "Input parameters for the image_search tool.",
  "properties": {
    "max_results": {
      "description": "Maximum number of images to return (default: 3, minimum: 3)",
      "maximum": 5,
      "minimum": 3,
      "title": "Max Results",
      "type": "integer"
    },
    "query": {
      "description": "Search query to find relevant images",
      "title": "Query",
      "type": "string"
    }
  },
  "required": ["query"],
  "title": "ImageSearchToolParams",
  "type": "object"
}
```

---

## message_compose_v1

**Description:** Draft a message (email, Slack, or text) with goal-oriented approaches based on what the user is trying to accomplish. Analyze the situation type (work disagreement, negotiation, following up, delivering bad news, asking for something, setting boundaries, apologizing, declining, giving feedback, cold outreach, responding to feedback, clarifying misunderstanding, delegating, celebrating) and identify competing goals or relationship stakes.

**MULTIPLE APPROACHES** (if high-stakes, ambiguous, or competing goals): Start with a scenario summary. Generate 2-3 strategies that lead to different outcomes -- not just tones. Label each clearly (e.g., "Disagree and commit" vs "Push for alignment", "Gentle nudge" vs "Create urgency", "Rip the bandaid" vs "Soften the landing"). Note what each prioritizes and trades off.

**SINGLE MESSAGE** (if transactional, one clear approach, or user just needs wording help): Just draft it. For emails, include a subject line. Adapt to channel -- emails longer/formal, Slack concise, texts brief. Test: Would a user choose between these based on what they want to accomplish?

**Schema:**

```json
{
  "properties": {
    "kind": {
      "description": "The type of message. 'email' shows a subject field and 'Open in Mail' button. 'textMessage' shows 'Open in Messages' button. 'other' shows 'Copy' button for platforms like LinkedIn, Slack, etc.",
      "enum": ["email", "textMessage", "other"],
      "type": "string"
    },
    "summary_title": {
      "description": "A brief title that summarizes the message (shown in the share sheet)",
      "type": "string"
    },
    "variants": {
      "description": "Message variants representing different strategic approaches",
      "items": {
        "properties": {
          "body": {"description": "The message content", "type": "string"},
          "label": {"description": "2-4 word goal-oriented label. E.g., 'Apologetic', 'Suggest alternative', 'Hold firm', 'Push back', 'Polite decline', 'Express interest'", "type": "string"},
          "subject": {"description": "Email subject line (only used when kind is 'email')", "type": "string"}
        },
        "required": ["label", "body"],
        "type": "object"
      },
      "minItems": 1,
      "type": "array"
    }
  },
  "required": ["kind", "variants"],
  "type": "object"
}
```

---

## places_map_display_v0

**Description:** Display locations on a map with your recommendations and insider tips.

WORKFLOW:
1. Use places_search tool first to find places and get their place_id
2. Call this tool with place_id references -- the backend will fetch full details

CRITICAL: Copy place_id values EXACTLY from places_search tool results. Place IDs are case-sensitive and must be copied verbatim -- do not type from memory or modify them.

TWO MODES -- use ONE of:

**A) SIMPLE MARKERS** -- just show places on a map:
```json
{
  "locations": [
    {
      "name": "Blue Bottle Coffee",
      "latitude": 37.78,
      "longitude": -122.41,
      "place_id": "ChIJ..."
    }
  ]
}
```

**B) ITINERARY** -- show a multi-stop trip with timing:
```json
{
  "title": "Tokyo Day Trip",
  "narrative": "A perfect day exploring...",
  "days": [
    {
      "day_number": 1,
      "title": "Temple Hopping",
      "locations": [
        {
          "name": "Senso-ji Temple",
          "latitude": 35.7148,
          "longitude": 139.7967,
          "place_id": "ChIJ...",
          "notes": "Arrive early to avoid crowds",
          "arrival_time": "8:00 AM"
        }
      ]
    }
  ],
  "travel_mode": "walking",
  "show_route": true
}
```

LOCATION FIELDS:
- name, latitude, longitude (required)
- place_id (recommended -- copy EXACTLY from places_search tool, enables full details)
- notes (your tour guide tip)
- arrival_time, duration_minutes (for itineraries)
- address (for custom locations without place_id)

**Schema:**

```json
{
  "$defs": {
    "DayInput": {
      "additionalProperties": false,
      "description": "Single day in an itinerary.",
      "properties": {
        "day_number": {"description": "Day number (1, 2, 3...)", "title": "Day Number", "type": "integer"},
        "locations": {
          "description": "Stops for this day",
          "items": {"$ref": "#/$defs/MapLocationInput"},
          "maxItems": 50,
          "minItems": 1,
          "title": "Locations",
          "type": "array"
        },
        "narrative": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "description": "Tour guide story arc for the day",
          "title": "Narrative"
        },
        "title": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "description": "Short evocative title (e.g., 'Temple Hopping')",
          "title": "Title"
        }
      },
      "required": ["day_number", "locations"],
      "title": "DayInput",
      "type": "object"
    },
    "MapLocationInput": {
      "additionalProperties": false,
      "description": "Minimal location input from Claude.\n\nOnly name, latitude, and longitude are required. If place_id is provided,\nthe backend will hydrate full place details from the Google Places API.",
      "properties": {
        "address": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "description": "Address for custom locations without place_id",
          "title": "Address"
        },
        "arrival_time": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "description": "Suggested arrival time (e.g., '9:00 AM')",
          "title": "Arrival Time"
        },
        "duration_minutes": {
          "anyOf": [{"type": "integer"}, {"type": "null"}],
          "description": "Suggested time at location in minutes",
          "title": "Duration Minutes"
        },
        "latitude": {"description": "Latitude coordinate", "title": "Latitude", "type": "number"},
        "longitude": {"description": "Longitude coordinate", "title": "Longitude", "type": "number"},
        "name": {"description": "Display name of the location", "title": "Name", "type": "string"},
        "notes": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "description": "Tour guide tip or insider advice",
          "title": "Notes"
        },
        "place_id": {
          "anyOf": [{"type": "string"}, {"type": "null"}],
          "description": "Google Place ID. If provided, backend fetches full details.",
          "title": "Place Id"
        }
      },
      "required": ["latitude", "longitude", "name"],
      "title": "MapLocationInput",
      "type": "object"
    }
  },
  "additionalProperties": false,
  "description": "Input parameters for display_map_tool.\n\nMust provide either `locations` (simple markers) or `days` (itinerary).",
  "properties": {
    "days": {
      "anyOf": [{"items": {"$ref": "#/$defs/DayInput"}, "maxItems": 30, "type": "array"}, {"type": "null"}],
      "description": "Itinerary with day structure for multi-day trips",
      "title": "Days"
    },
    "locations": {
      "anyOf": [{"items": {"$ref": "#/$defs/MapLocationInput"}, "maxItems": 50, "type": "array"}, {"type": "null"}],
      "description": "Simple marker display - list of locations without day structure",
      "title": "Locations"
    },
    "mode": {
      "anyOf": [{"enum": ["markers", "itinerary"], "type": "string"}, {"type": "null"}],
      "description": "Display mode. Auto-inferred: markers if locations, itinerary if days.",
      "title": "Mode"
    },
    "narrative": {
      "anyOf": [{"type": "string"}, {"type": "null"}],
      "description": "Tour guide intro for the trip",
      "title": "Narrative"
    },
    "show_route": {
      "anyOf": [{"type": "boolean"}, {"type": "null"}],
      "description": "Show route between stops. Default: true for itinerary, false for markers.",
      "title": "Show Route"
    },
    "title": {
      "anyOf": [{"type": "string"}, {"type": "null"}],
      "description": "Title for the map or itinerary",
      "title": "Title"
    },
    "travel_mode": {
      "anyOf": [{"enum": ["driving", "walking", "transit", "bicycling"], "type": "string"}, {"type": "null"}],
      "description": "Travel mode for directions (default: driving)",
      "title": "Travel Mode"
    }
  },
  "title": "DisplayMapParams",
  "type": "object"
}
```

---

## places_search

**Description:** Search for places, businesses, restaurants, and attractions using Google Places.

SUPPORTS MULTIPLE QUERIES in a single call. Multiple queries can be used for:
- efficient itinerary planning
- breaking down broad or abstract requests: 'best hotels 1hr from London' does not translate well to a direct query. Rather it can be decomposed like: 'luxury hotels Oxfordshire', 'luxury hotels Cotswolds', 'luxury hotels North Downs' etc.

USAGE:
```json
{
  "queries": [
    { "query": "temples in Asakusa", "max_results": 3 },
    { "query": "ramen restaurants in Tokyo", "max_results": 3 },
    { "query": "coffee shops in Shibuya", "max_results": 2 }
  ]
}
```

Each query can specify max_results (1-10, default 5).
Results are deduplicated across queries.
For place names that are common, make sure you include the wider area e.g. restaurants Chelsea, London (to differentiate vs Chelsea in New York).

RETURNS: Array of places with place_id, name, address, coordinates, rating, photos, hours, and other details. IMPORTANT: Display results to the user via the places_map_display_v0 tool (preferred) or via text. Irrelevant results can be disregarded and ignored, the user will not see them.

**Schema:**

```json
{
  "$defs": {
    "SearchQuery": {
      "additionalProperties": false,
      "description": "Single search query within a multi-query request.",
      "properties": {
        "max_results": {
          "description": "Maximum number of results for this query (1-10, default 5)",
          "maximum": 10,
          "minimum": 1,
          "title": "Max Results",
          "type": "integer"
        },
        "query": {
          "description": "Natural language search query (e.g., 'temples in Asakusa', 'ramen restaurants in Tokyo')",
          "title": "Query",
          "type": "string"
        }
      },
      "required": ["query"],
      "title": "SearchQuery",
      "type": "object"
    }
  },
  "additionalProperties": false,
  "description": "Input parameters for the places search tool.\n\nSupports multiple queries in a single call for efficient itinerary planning.",
  "properties": {
    "location_bias_lat": {
      "anyOf": [{"type": "number"}, {"type": "null"}],
      "description": "Optional latitude coordinate to bias results toward a specific area",
      "title": "Location Bias Lat"
    },
    "location_bias_lng": {
      "anyOf": [{"type": "number"}, {"type": "null"}],
      "description": "Optional longitude coordinate to bias results toward a specific area",
      "title": "Location Bias Lng"
    },
    "location_bias_radius": {
      "anyOf": [{"type": "number"}, {"type": "null"}],
      "description": "Optional radius in meters for location bias (default 5000 if lat/lng provided)",
      "title": "Location Bias Radius"
    },
    "queries": {
      "description": "List of search queries (1-10 queries). Each query can specify its own max_results.",
      "items": {"$ref": "#/$defs/SearchQuery"},
      "maxItems": 10,
      "minItems": 1,
      "title": "Queries",
      "type": "array"
    }
  },
  "required": ["queries"],
  "title": "PlacesSearchParams",
  "type": "object"
}
```

---

## present_files

**Description:** The present_files tool makes files visible to the user for viewing and rendering in the client interface.

When to use the present_files tool:
- Making any file available for the user to view, download, or interact with
- Presenting multiple related files at once
- After creating a file that should be presented to the user

When NOT to use the present_files tool:
- When you only need to read file contents for your own processing
- For temporary or intermediate files not meant for user viewing

How it works:
- Accepts an array of file paths from the container filesystem
- Returns output paths where files can be accessed by the client
- Output paths are returned in the same order as input file paths
- Multiple files can be presented efficiently in a single call
- If a file is not in the output directory, it will be automatically copied into that directory
- The first input path passed in to the present_files tool, and therefore the first output path returned from it, should correspond to the file that is most relevant for the user to see first

**Schema:**

```json
{
  "additionalProperties": false,
  "properties": {
    "filepaths": {
      "description": "Array of file paths identifying which files to present to the user",
      "items": {"type": "string"},
      "minItems": 1,
      "title": "Filepaths",
      "type": "array"
    }
  },
  "required": ["filepaths"],
  "title": "PresentFilesInputSchema",
  "type": "object"
}
```

---

## recipe_display_v0

**Description:** Display an interactive recipe with adjustable servings. Use when the user asks for a recipe, cooking instructions, or food preparation guide. The widget allows users to scale all ingredient amounts proportionally by adjusting the servings control.

**Schema:**

```json
{
  "$defs": {
    "RecipeIngredient": {
      "description": "Individual ingredient in a recipe.",
      "properties": {
        "amount": {"description": "The quantity for base_servings", "title": "Amount", "type": "number"},
        "id": {"description": "4 character unique identifier number for this ingredient (e.g., '0001', '0002'). Used to reference in steps.", "title": "Id", "type": "string"},
        "name": {"description": "Display name of the ingredient. For whole/countable items, fold the counting noun in here (e.g., 'garlic cloves', 'large eggs', 'medium lemon, zested').", "title": "Name", "type": "string"},
        "unit": {
          "anyOf": [{"enum": ["g", "kg", "ml", "l", "tsp", "tbsp", "cup", "fl_oz", "oz", "lb", "pinch"], "type": "string"}, {"type": "null"}],
          "default": null,
          "description": "Unit of measurement. Omit for whole/countable items (e.g., 3 garlic cloves, 2 lemons) and put the counting noun in `name` instead. For salt/pepper/seasonings, give a concrete starting amount in tsp rather than a placeholder count. Weight: g, kg, oz, lb. Volume: ml, l, tsp, tbsp, cup, fl_oz.",
          "title": "Unit"
        }
      },
      "required": ["amount", "id", "name"],
      "title": "RecipeIngredient",
      "type": "object"
    },
    "RecipeStep": {
      "description": "Individual step in a recipe.",
      "properties": {
        "content": {"description": "The full instruction text. Use {ingredient_id} to insert editable ingredient amounts inline (e.g., 'Whisk together {0001} and {0002}')", "title": "Content", "type": "string"},
        "id": {"description": "Unique identifier for this step", "title": "Id", "type": "string"},
        "timer_seconds": {
          "anyOf": [{"type": "integer"}, {"type": "null"}],
          "default": null,
          "description": "Timer duration in seconds. Include whenever the step involves waiting, cooking, baking, resting, marinating, chilling, boiling, simmering, or any time-based action. Omit only for active hands-on steps with no waiting.",
          "title": "Timer Seconds"
        },
        "title": {"description": "Short summary of the step (e.g., 'Boil pasta', 'Make the sauce', 'Rest the dough'). Used as the timer label and step header in cooking mode.", "title": "Title", "type": "string"}
      },
      "required": ["content", "id", "title"],
      "title": "RecipeStep",
      "type": "object"
    }
  },
  "additionalProperties": false,
  "description": "Input parameters for the recipe widget tool.",
  "properties": {
    "base_servings": {
      "anyOf": [{"type": "integer"}, {"type": "null"}],
      "description": "The number of servings this recipe makes at base amounts (default: 4)",
      "title": "Base Servings"
    },
    "description": {
      "anyOf": [{"type": "string"}, {"type": "null"}],
      "description": "A brief description or tagline for the recipe",
      "title": "Description"
    },
    "ingredients": {
      "description": "List of ingredients with amounts",
      "items": {"$ref": "#/$defs/RecipeIngredient"},
      "title": "Ingredients",
      "type": "array"
    },
    "notes": {
      "anyOf": [{"type": "string"}, {"type": "null"}],
      "description": "Optional tips, variations, or additional notes about the recipe",
      "title": "Notes"
    },
    "steps": {
      "description": "Cooking instructions. Reference ingredients using {ingredient_id} syntax.",
      "items": {"$ref": "#/$defs/RecipeStep"},
      "title": "Steps",
      "type": "array"
    },
    "title": {
      "description": "The name of the recipe (e.g., 'Spaghetti alla Carbonara')",
      "title": "Title",
      "type": "string"
    }
  },
  "required": ["ingredients", "steps", "title"],
  "title": "RecipeWidgetParams",
  "type": "object"
}
```

---

## recommend_claude_apps

**Description:** Recommend 1-3 apps or extensions to help the user better understand the Claude ecosystem. Show this when a user is working on something that might be better suited for an app other than Claude chat -- ex: coding (Claude Code), knowledge work (Cowork), or working on sheets or slides (Excel/Powerpoint), etc. Only recommend apps relevant to the user's current use case sorted by relevance. The UI will show each app with an icon, description, and an Install or Download button linking to the right store or installer.

**Schema:**

```json
{
  "properties": {
    "app_ids": {
      "description": "IDs of Claude apps or extensions to recommend. Claude Desktop App, Claude for iOS, Claude for Android, Claude Code, Claude Code for VS Code, Claude Code for JetBrains, Claude Code for Slack, Claude for Excel, Claude for PowerPoint, Claude for Chrome.",
      "items": {
        "enum": ["desktop", "ios", "android", "claude_code_terminal", "claude_code_vscode", "claude_code_jetbrains", "claude_code_slack", "excel", "powerpoint", "chrome"],
        "type": "string"
      },
      "type": "array"
    }
  },
  "required": ["app_ids"],
  "type": "object"
}
```

---

## search_mcp_registry

**Description:** Search for available connectors in the MCP registry. Call this when connecting to a new MCP might help resolve the user query -- whether or not they name a specific product.

Named-product examples:
- 'check my Asana tasks' -> search ['asana', 'tasks', 'todo']
- 'find issues in Jira' -> search ['jira', 'issues']

Intent-based examples (no product named):
- 'help me manage my tasks' -> search ['tasks', 'todo', 'project management']
- 'what's on my calendar tomorrow' -> search ['calendar', 'schedule', 'events']
- 'did I get a reply from them yet' -> search ['email', 'messages', 'inbox']
- 'pull up the design mockups' -> search ['design', 'mockup']
- 'check if the CI passed' -> search ['ci', 'build', 'pipeline']
- 'did the call cover Mike's latest ticket' -> thinking: 'I don't have any context about the call or meeting, let's see if there are any connectors available' -> search ['meeting', 'call', 'transcript']

If the request implies reading the user's data (email, calendar, tasks, files, tickets, etc.) and you don't already have a tool for it, search -- even if the phrasing is casual. 'Did I get a reply' is an email check. 'What's pending' is a task check. Returns a ranked list. If results look relevant, call suggest_connectors to present the options. If nothing matches the task, do NOT call suggest_connectors -- fall through to the browser or answer directly depending on the task type (booking/action tasks go to navigate; info requests get a direct answer).

**Schema:**

```json
{
  "properties": {
    "keywords": {"items": {"type": "string"}, "title": "Keywords", "type": "array"}
  },
  "required": ["keywords"],
  "title": "SearchMcpRegistryInput",
  "type": "object"
}
```

---

## str_replace

**Description:** Replace a unique string in a file with another string. old_str must match the raw file content exactly and appear exactly once. When copying from view output, do NOT include the line number prefix (spaces + line number + tab) -- it is display-only. View the file immediately before editing; after any successful str_replace, earlier view output of that file in your context is stale -- re-view before further edits to the same file. Files under /mnt/user-data/uploads, /mnt/transcripts, /mnt/skills/public, /mnt/skills/private, /mnt/skills/examples are read-only -- copy them to a writable location first if you need to edit them.

**Schema:**

```json
{
  "properties": {
    "description": {"title": "Why I'm making this edit", "type": "string"},
    "new_str": {"default": "", "title": "String to replace with (empty to delete)", "type": "string"},
    "old_str": {"title": "String to replace (must be unique in file)", "type": "string"},
    "path": {"title": "Path to the file to edit", "type": "string"}
  },
  "required": ["description", "old_str", "path"],
  "title": "StrReplaceInput",
  "type": "object"
}
```

---

## suggest_connectors

**Description:** Present connector options to the user. Each option renders with a Connect or Use button, plus a 'None of these' option. The user's choice arrives as a follow-up message.

Call this when any of the following are true:
- A relevant option is an MCP App (tools tagged [third_party_mcp_app]) and the user did not explicitly name that company -- even if the connector is already connected
- The user has no connected tool that can fulfill the request
- The user explicitly asks what connectors are available (e.g. 'what can help me manage my tasks')
- A tool call failed with an auth/credential error -- pass the server UUID from the failed tool name mcp__{uuid}__{toolName} so the user can re-authenticate

Do NOT call this tool unless you have already called the search_mcp_registry tool or are handling a tool auth/credential error. Do NOT call this if the user named a specific connected service -- just use it. If search_mcp_registry returned nothing relevant, do NOT call this -- answer the user directly instead.

Pass directoryUuid values from search_mcp_registry results -- not connector names, not guesses. If you haven't called search_mcp_registry yet, call it first to get the UUIDs. Include all relevant options in uuids (connected or not). End your turn after calling this with a short framing line like 'I found a few options -- which would you like?' -- don't continue with a generic answer. The user's selection arrives as a follow-up message like 'Use {name} for this' (they picked one) or 'Don't use a connector' (they picked None of these).

**Schema:**

```json
{
  "properties": {
    "uuids": {"items": {"type": "string"}, "title": "Uuids", "type": "array"}
  },
  "required": ["uuids"],
  "title": "SuggestConnectorsInput",
  "type": "object"
}
```

---

## view

**Description:** Supports viewing text, images, and directory listings.

Supported path types:
- **Directories:** Lists files and directories up to 2 levels deep, ignoring hidden items and node_modules
- **Image files** (.jpg, .jpeg, .png, .gif, .webp): Displays the image visually
- **Text files:** Displays numbered lines (prefix is display-only -- do not include it in str_replace's old_str). You can optionally specify a view_range to see specific lines.

Note: Files with non-UTF-8 encoding will display hex escapes (e.g. \x84) for invalid bytes.

**Schema:**

```json
{
  "properties": {
    "description": {"title": "Why I need to view this", "type": "string"},
    "path": {"title": "Absolute path to file or directory, e.g. `/repo/file.py` or `/repo`.", "type": "string"},
    "view_range": {
      "anyOf": [
        {"maxItems": 2, "minItems": 2, "prefixItems": [{"type": "integer"}, {"type": "integer"}], "type": "array"},
        {"type": "null"}
      ],
      "default": null,
      "title": "Optional line range for text files. Format: [start_line, end_line] where lines are indexed starting at 1. Use [start_line, -1] to view from start_line to the end of the file. When not provided, the entire file is displayed, truncating from the middle if it exceeds 16,000 characters (showing beginning and end)."
    }
  },
  "required": ["description", "path"],
  "title": "ViewInput",
  "type": "object"
}
```

---

## weather_fetch

**Description:** Display weather information. Use the user's home location to determine temperature units: Fahrenheit for US users, Celsius for others.

**USE THIS TOOL WHEN:**
- User asks about weather in a specific location
- User asks 'should I bring an umbrella/jacket'
- User is planning outdoor activities
- User asks 'what's it like in [city]' (weather context)

**SKIP THIS TOOL WHEN:**
- Climate or historical weather questions
- Weather as small talk without location specified

**Schema:**

```json
{
  "additionalProperties": false,
  "description": "Input parameters for the weather tool.",
  "properties": {
    "latitude": {"description": "Latitude coordinate of the location", "title": "Latitude", "type": "number"},
    "location_name": {"description": "Human-readable name of the location (e.g., 'San Francisco, CA')", "title": "Location Name", "type": "string"},
    "longitude": {"description": "Longitude coordinate of the location", "title": "Longitude", "type": "number"}
  },
  "required": ["latitude", "location_name", "longitude"],
  "title": "WeatherParams",
  "type": "object"
}
```

---

## web_fetch

**Description:** Fetch the contents of a web page at a given URL. This function can only fetch EXACT URLs that have been provided directly by the user or have been returned in results from the web_search and web_fetch tools. This tool cannot access content that requires authentication, such as private Google Docs or pages behind login walls. Do not add www. to URLs that do not have them. URLs must include the schema: https://example.com is a valid URL while example.com is an invalid URL.

**Schema:**

```json
{
  "additionalProperties": false,
  "properties": {
    "allowed_domains": {
      "anyOf": [{"items": {"type": "string"}, "type": "array"}, {"type": "null"}],
      "description": "List of allowed domains. If provided, only URLs from these domains will be fetched.",
      "examples": [["example.com", "docs.example.com"]],
      "title": "Allowed Domains"
    },
    "blocked_domains": {
      "anyOf": [{"items": {"type": "string"}, "type": "array"}, {"type": "null"}],
      "description": "List of blocked domains. If provided, URLs from these domains will not be fetched.",
      "examples": [["malicious.com", "spam.example.com"]],
      "title": "Blocked Domains"
    },
    "html_extraction_method": {
      "description": "The HTML extraction method to use. 'markdown' produces better content extraction than the legacy 'traf' method.",
      "title": "Html Extraction Method",
      "type": "string"
    },
    "is_zdr": {
      "description": "Whether this is a Zero Data Retention request. When true, the fetcher should not log the URL.",
      "title": "Is Zdr",
      "type": "boolean"
    },
    "text_content_token_limit": {
      "anyOf": [{"type": "integer"}, {"type": "null"}],
      "description": "Truncate text to be included in the context to approximately the given number of tokens. Has no effect on binary content.",
      "title": "Text Content Token Limit"
    },
    "url": {"title": "Url", "type": "string"},
    "web_fetch_pdf_extract_text": {
      "anyOf": [{"type": "boolean"}, {"type": "null"}],
      "description": "If true, extract text from PDFs. Otherwise return raw Base64-encoded bytes.",
      "title": "Web Fetch Pdf Extract Text"
    },
    "web_fetch_rate_limit_dark_launch": {
      "anyOf": [{"type": "boolean"}, {"type": "null"}],
      "description": "If true, log rate limit hits but don't block requests (dark launch mode)",
      "title": "Web Fetch Rate Limit Dark Launch"
    },
    "web_fetch_rate_limit_key": {
      "anyOf": [{"type": "string"}, {"type": "null"}],
      "description": "Rate limit key for limiting non-cached requests (100/hour). If not specified, no rate limit is applied.",
      "examples": ["conversation-12345", "user-67890"],
      "title": "Web Fetch Rate Limit Key"
    }
  },
  "required": ["url"],
  "title": "AnthropicFetchParams",
  "type": "object"
}
```

---

## web_search

**Description:** Search the web.

**Schema:**

```json
{
  "additionalProperties": false,
  "properties": {
    "query": {"description": "Search query", "title": "Query", "type": "string"}
  },
  "required": ["query"],
  "title": "AnthropicSearchParams",
  "type": "object"
}
```
