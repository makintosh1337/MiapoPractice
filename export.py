import csv, json
from data import load_games

def export_to_csv():
    games = load_games()
    if not games: return "⚠️ Нет данных."
    with open("games_export.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id","title","platform","status","hours"])
        w.writeheader(); w.writerows(games)
    return f"📁 Экспортировано в games_export.csv"