import json
import tkinter as tk
from pathlib import Path

from ui.game_ui import ReinforcementGame


BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    """데이터를 불러와 게임 화면을 실행한다."""
    with (BASE_DIR / "data" / "weapons.json").open(encoding="utf-8") as data_file:
        weapons = json.load(data_file)
    with (BASE_DIR / "data" / "messages.json").open(encoding="utf-8") as data_file:
        messages = json.load(data_file)

    root = tk.Tk()
    ReinforcementGame(root, weapons, messages, BASE_DIR / "image")
    root.mainloop()


if __name__ == "__main__":
    main()
