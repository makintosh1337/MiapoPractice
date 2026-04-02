from data import add_game, update_progress

APP_NAME = " Game Tracker"

def menu():
    """Главное меню приложения"""
    print(f"\n{'='*40}")
    print(f"{APP_NAME}")
    print(f"{'='*40}")
    print("1. Добавить игру")
    print("2. Обновить прогресс")
    print("3. Выход")
    print(f"{'='*40}")
    
    choice = input("Выберите действие (1-3): ").strip()
    
    if choice == "1":
        add_game_menu()
    elif choice == "2":
        update_progress_menu()
    elif choice == "3":
        print("\n До свидания! Приятной игры!")
        return
    else:
        print("\n Неверный выбор. Попробуйте снова.")
    

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