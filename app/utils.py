from pathlib import Path

DATA = Path(__file__).parent / "data.txt"

def greet(name: str) -> str:
    return f"Hello, {name}!"

def save_note(text: str) -> None:
    with open(DATA, "a", encoding="utf-8") as f:
        f.write(text.strip() + "\n")

def load_notes():
    if not DATA.exists():
        return []
    with open(DATA, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
# new constant added by person2
PI = 3.14159
# dev2 change in utils.py
