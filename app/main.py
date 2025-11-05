print("App started")
from utils import greet, save_note, load_notes

if __name__ == "__main__":
    print(greet("Student"))
    save_note("Первый запуск приложения")
    for i, note in enumerate(load_notes(), 1):
        print(f"{i}. {note}")
