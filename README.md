# Overview
This is a sample personal project for Boot.dev. It creates a questlog that can be completed in the CLI using storage in a local JSON file to keep track of quests.

## Setup
```
python3 -m venv .
bin/pip install python-dateutil
```

## Usage
```
bin/python3 main.py
```

Data is stored in `quests.json` in the working directory (created automatically on first run).

### Commands
- `add` — prompts for a name, xp value, and a future due date, then saves a new quest
- `complete {id}` — marks the quest with that id as complete and awards its xp (or marks it failed if the due date has passed)
- `abandon {id}` — deletes a pending quest (or marks it failed instead of deleting, if the due date has already passed)
- `list-pending` — lists quests that are neither complete nor failed; any with a due date in the past are marked failed
- `list-complete` — lists completed quests
- `list-failed` — lists failed quests
- `level` — prints current level and overall xp
- `help` — prints the list of accepted commands
- `end` — prints the raw quest data and exits
