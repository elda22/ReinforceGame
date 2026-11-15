import tkinter as tk
from pathlib import Path

from PIL import ImageTk

from game.game_logic import STARTING_BALANCE, attempt_reinforcement, sell_current_weapon


class ReinforcementGame:
    """게임 상태와 화면을 관리한다."""

    def __init__(
        self, root: tk.Tk, weapons: list[dict], messages: dict[str, str], image_dir: Path
    ) -> None:
        self.root = root
        self.weapons = weapons
        self.messages = messages
        self.image_dir = image_dir
        self.current_weapon_index = 0
        self.balance = STARTING_BALANCE
        self.highest_weapon_index = 0
        self.weapon_image_cache: dict[int, ImageTk.PhotoImage] = {}

        self._build_ui()
        self._update_display()
        self.status_label.config(text=self.messages["welcome"])

    def _build_ui(self) -> None:
        """게임 화면과 버튼을 구성한다."""
        self.root.geometry("1000x600")
        self.root.title(self.messages["window_title"])
        self.root.option_add("*Font", "맑은고딕 23")
        self.root.config(bg="gray")

        self.current_weapon_image_label = tk.Label(self.root, background="gray")
        self.current_weapon_image_label.place(relx=0.23, rely=0.75, anchor="s")

        self.next_weapon_image_label = tk.Label(self.root, background="gray")
        self.next_weapon_image_label.place(relx=0.77, rely=0.75, anchor="s")

        self.status_label = tk.Label(self.root)
        self.status_label.place(relx=0.5, rely=0.7, anchor="s")

        self.balance_label = tk.Label(self.root)
        self.balance_label.place(relx=0.5, rely=0.785, anchor="s")

        self.current_weapon_label = tk.Label(self.root)
        self.current_weapon_label.place(relx=0.23, rely=0.05, anchor="n")

        self.next_weapon_label = tk.Label(self.root)
        self.next_weapon_label.place(relx=0.77, rely=0.05, anchor="n")

        self.reinforcement_button = tk.Button(
            self.root,
            text=self.messages["reinforcement_button"],
            command=self._handle_reinforcement,
            background="#FF6347",
        )
        self.reinforcement_button.place(relx=0.4, rely=0.9, anchor="s")

        self.sale_button = tk.Button(
            self.root,
            text=self.messages["sale_button"],
            command=self._handle_sale,
            background="#32CD32",
        )
        self.sale_button.place(relx=0.6, rely=0.9, anchor="s")

    def _get_weapon_image(self, weapon_index: int) -> ImageTk.PhotoImage:
        """무기 이미지를 불러오고 재사용한다."""
        if weapon_index not in self.weapon_image_cache:
            weapon_name = self.weapons[weapon_index]["weapon_name"]
            image_path = self.image_dir / "{}.png".format(weapon_name)
            self.weapon_image_cache[weapon_index] = ImageTk.PhotoImage(
                file=str(image_path)
            )
        return self.weapon_image_cache[weapon_index]

    def _update_display(self) -> None:
        """현재 게임 상태를 화면에 반영한다."""
        current_weapon = self.weapons[self.current_weapon_index]
        self.current_weapon_image_label.config(
            image=self._get_weapon_image(self.current_weapon_index)
        )
        self.balance_label.config(
            text=self.messages["balance"].format(balance=self.balance)
        )
        self.current_weapon_label.config(
            text=self.messages["current_weapon"].format(
                weapon_name=current_weapon["weapon_name"],
                sale_price=current_weapon["sale_price"],
            )
        )

        next_weapon_index = self.current_weapon_index + 1
        if next_weapon_index >= len(self.weapons):
            self.next_weapon_image_label.config(image="")
            self.next_weapon_label.config(text=self.messages["max_level"])
            return

        next_weapon = self.weapons[next_weapon_index]
        self.next_weapon_image_label.config(
            image=self._get_weapon_image(next_weapon_index)
        )
        self.next_weapon_label.config(
            text=self.messages["next_weapon"].format(
                weapon_name=next_weapon["weapon_name"],
                reinforcement_cost=next_weapon["reinforcement_cost"],
                success_rate=next_weapon["success_rate"],
            )
        )

    def _handle_reinforcement(self) -> None:
        """강화를 시도하고 결과를 화면에 반영한다."""
        (
            self.current_weapon_index,
            self.balance,
            self.highest_weapon_index,
            message_key,
        ) = attempt_reinforcement(
            self.weapons,
            self.current_weapon_index,
            self.balance,
            self.highest_weapon_index,
        )
        self.status_label.config(text=self.messages[message_key])
        self._update_display()

    def _handle_sale(self) -> None:
        """무기를 판매하고 결과를 화면에 반영한다."""
        weapon_name = self.weapons[self.current_weapon_index]["weapon_name"]
        self.current_weapon_index, self.balance = sell_current_weapon(
            self.weapons,
            self.current_weapon_index,
            self.balance,
        )
        self.status_label.config(
            text=self.messages["sale"].format(weapon_name=weapon_name)
        )
        self._update_display()
