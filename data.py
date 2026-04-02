import json, os, datetime

DATA_FILE = "games.json"

def load_games():
    """Загрузить все игры из JSON файла"""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_games(games):
    """Сохранить все игры в JSON файл"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(games, f, ensure_ascii=False, indent=2)

def add_game(title, platform):
    """Добавить новую игру в библиотеку"""
    games = load_games()
    game = {
        "id": len(games) + 1,
        "title": title.strip(),
        "platform": platform.strip(),
        "status": "playing",
        "hours": 0,
        "added_at": datetime.datetime.now().strftime("%Y-%m-%d")
    }
    games.append(game)
    save_games(games)
    return f" Игра '{title}' добавлена в библиотеку (ID: {game['id']})"

def update_progress(game_id, status=None, hours=None):
    """Обновить прогресс игры по ID"""
    games = load_games()
    
    for game in games:
        if game["id"] == game_id:
            if status is not None and status != "":
                game["status"] = status.strip()
            if hours is not None and hours != "":
                game["hours"] = int(hours)
            
            game["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%d")
            save_games(games)
            return f" Игра '#{game_id}' обновлена: {game['title']} [{game['status']}] - {game['hours']}ч"
    
    return f" Игра с ID {game_id} не найдена"
    
def view_library():
    games = load_games()
    if not games: return "📭 Библиотека пуста."
    out = "\n📚 Игры:\n" + "-"*40 + "\n"
    for g in games:
        out += f"#{g['id']} {g['title']} [{g['platform']}] | {g['status']} | {g['hours']}ч\n"
    return out