import importlib
from pathlib import Path

def test_greet():
    utils = importlib.import_module("app.utils")
    assert utils.greet("Student") == "Hello, Student!"

def test_save_and_load_notes(tmp_path, monkeypatch):
    utils = importlib.import_module("app.utils")
    # переопределим путь к файлу, чтобы не трогать рабочий data.txt
    test_data = tmp_path / "data.txt"
    monkeypatch.setattr(utils, "DATA", test_data)
    utils.save_note("note1")
    utils.save_note("note2")
    assert utils.load_notes() == ["note1", "note2"]
