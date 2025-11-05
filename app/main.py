from app.utils import greet, save_note, load_notes


def run():
    """Main entry point of the app."""
    print("App started successfully.")
    print(greet("Student"))
    save_note("Application initialized by person1.")
    notes = load_notes()
    print("Notes:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")


if __name__ == "__main__":
    run()
