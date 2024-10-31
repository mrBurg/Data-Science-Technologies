""" Menu """

# pylint: disable=E0401

import os
from dataclasses import dataclass

from utils import Utils
from keyboard_handler import KeyboardHandler


@dataclass
class Menu:
    """Menu"""

    selected_option = 0

    def __init__(self, options):
        self.options = options

        self.key_handl = KeyboardHandler()

        Utils.loop(self.display_menu, 0.05)

    def display_menu(self):
        """display_menu"""

        os.system("cls" if os.name == "nt" else "clear")

        print("Для використання меню використовуйте:")
        print('Стрілки "вгору" та "вниз" для перемикання')
        print('"Enter" для підтвердження вибору')
        print('"q" скасування\n')

        for i, option in enumerate(self.options):
            if i == self.selected_option:
                print(f"> {option} <")
            else:
                print(f"  {option}  ")

        pressed_key = self.key_handl.get_key()

        match pressed_key:
            case "down":
                self.selected_option = (self.selected_option + 1) % len(self.options)

            case "up":
                self.selected_option = (self.selected_option - 1) % len(self.options)

            # case "enter" | "q":
            case "enter":
                return False

            case "q":
                self.selected_option = -1

                return False

        return True
