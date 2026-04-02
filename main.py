from data import add_game

APP_NAME = "Game Tracker"

def menu():
    print(f"\n{APP_NAME}")
    print("1. Добавить игру")
    choice = input("Выбор: ")
    if choice == "1":
        t = input("Название: "); p = input("Платформа: ")
        print(add_game(t, p))
    else:
        print("Выход.")

if __name__ == "__main__":
    menu()