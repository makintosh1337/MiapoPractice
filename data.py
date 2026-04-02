import json, os, datetime

DATA_FILE = "games.json"

def load_games():
    if not os.path.exists(DATA_FILE): return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_games(games):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(games, f, ensure_ascii=False, indent=2)

def add_game(title, platform):
    games = load_games()
    game = {"id": len(games)+1, "title": title.strip(), "platform": platform.strip(), "status": "playing", "hours": 0}
    games.append(game)
    save_games(games)
    return f" '{title}' добавлена."