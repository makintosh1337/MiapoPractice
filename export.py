import csv
from data import load_games

def export_to_csv():
    """Экспорт библиотеки в CSV файл"""
    games = load_games()
    if not games:
        return " Нет данных для экспорта."
        
    fieldnames = ["id", "title", "platform", "status", "hours"]
    with open("games_export.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(games)
        
    return " Успешно экспортировано в games_export.csv"