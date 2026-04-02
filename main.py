from data import add_game, update_progress, view_library
from export import export_to_csv

APP_NAME = "🎮 Game Tracker v2"

def menu():
    print(f"\n{APP_NAME} | Версия 2.0")
    print("1. Добавить игру")
    print("2. Обновить прогресс")
    print("3. Библиотека")
    print("4. Экспорт в CSV")
    choice = input("Ваш выбор (1-4): ")
    if choice == "1":
        t = input("Название: "); p = input("Платформа: ")
        print(add_game(t, p))
    elif choice == "2":
        gid = int(input("ID: ")); s = input("Статус: "); h = input("Часы: ")
        print(update_progress(gid, s or None, h or None))
    elif choice == "3":
        print(view_library())
    elif choice == "4":
        print(export_to_csv())
    else:
        print("До свидания.")

    menu()

def add_game_menu():
    """Меню добавления игры"""
    print("\n--- Добавление новой игры ---")
    title = input("Название игры: ").strip()
    platform = input("Платформа (PC/PS5/Xbox/Switch): ").strip()
    
    if not title or not platform:
        print(" Название и платформа обязательны!")
        return
    
    result = add_game(title, platform)
    print(f"\n{result}")

def update_progress_menu():
    """Меню обновления прогресса"""
    print("\n--- Обновление прогресса ---")
    
    try:
        game_id = int(input("Введите ID игры: ").strip())
    except ValueError:
        print(" ID должен быть числом!")
        return
    
    print("\nОставьте поле пустым, если не хотите менять:")
    status = input("Новый статус (playing/completed/dropped): ").strip()
    hours = input("Время в часах: ").strip()
    
    if not status and not hours:
        print(" Нужно указать хотя бы одно значение для обновления!")
        return
    
    result = update_progress(game_id, status if status else None, hours if hours else None)
    print(f"\n{result}")

if __name__ == "__main__":
    menu()