from utils import greet, save_note, load_notes

def run():
    print("App started")
    print("App initialized by person1")
    print(greet("Student"))
    save_note("Первый запуск приложения")
    for i, note in enumerate(load_notes(), 1):
        print(f"{i}. {note}")

if __name__ == "__main__":
    run()
