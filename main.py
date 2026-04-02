from data import add_game, update_progress, view_library
from export import export_to_csv

APP_NAME = "Game Tracker v2"

def menu():
    print(f"\n{APP_NAME} | Версия 2.0")
    print("1. Добавить игру")
    print("2. Обновить прогресс")
    print("3. Библиотека")
    print("4. Экспорт в CSV")
    print("5. Выход")

def add_game_menu():
    """Меню добавления игры"""
    print("\n--- Добавление новой игры ---")
    title = input("Название игры: ").strip()
    platform = input("Платформа (PC/PS5/Xbox/Switch): ").strip()
    
    if not title or not platform:
        print(" Название и платформа обязательны!")
        return
    
    print(add_game(title, platform))

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
    hours_input = input("Время в часах: ").strip()
    
    if not status and not hours_input:
        print(" Нужно указать хотя бы одно значение для обновления!")
        return
    
    hours = None
    if hours_input:
        try:
            hours = int(hours_input)
        except ValueError:
            print(" Время должно быть целым числом!")
            return
            
    status_val = status if status else None
    print(update_progress(game_id, status_val, hours))

def main():
    while True:
        menu()
        choice = input("Ваш выбор (1-5): ").strip()
        
        if choice == "1":
            add_game_menu()
        elif choice == "2":
            update_progress_menu()
        elif choice == "3":
            print(view_library())
        elif choice == "4":
            print(export_to_csv())
        elif choice == "5":
            print(" До свидания!")
            break
        else:
            print(" Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()