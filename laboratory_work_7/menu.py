""" Menu """

# pylint: disable=E0401


from dataclasses import dataclass

from utils import Utils
from keyboard_handler import KeyboardHandler


@dataclass
class Menu:
    """Menu"""

    selected = 0

    def __init__(self, options):
        self.options = options
        self.key_handl = KeyboardHandler()

        self._refresh()

    def _refresh(self):
        """refresh"""

        pressed_key = self.key_handl.get_key()

        if pressed_key in {"space", "q"}:
            return

        self._display_menu()
        Utils.loop(self._selection, 0.075)
        self._refresh()

    def _display_menu(self):
        """display_menu"""

        Utils.clear_console()

        print(
            'Головне меню:\n["вгору"] та ["вниз"] – для перемикання\n["space"] – для підтвердження вибору\n["q"] – скасування\n'
        )

        for i, option in enumerate(self.options):
            if i == self.selected:
                print(f"-> {option} <-")
            else:
                print(f"   {option}   ")

    def _selection(self):
        """selection"""

        pressed_key = self.key_handl.get_key()

        match pressed_key:
            case "down":
                self.selected = (self.selected + 1) % len(self.options)

                return False

            case "up":
                self.selected = (self.selected - 1) % len(self.options)

                return False

            # case "space" | "q":
            case "space":
                return False

            case "q":
                self.selected = -1

                return False

        return True
