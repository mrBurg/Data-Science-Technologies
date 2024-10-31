""" KeyboardHandler """

# pylint: disable=E0401

from dataclasses import dataclass

import keyboard


@dataclass
class KeyboardHandler:
    """KeyboardHandler"""

    keys = {"up": False, "down": False, "q": False, "enter": False}
    pressed_key = None

    def get_key(self):
        """get_key"""

        for i in list(self.keys.keys()):
            self.keys[i] = keyboard.is_pressed(i)

            if self.keys[i]:
                self.pressed_key = i

        keyboard.hook(self.hook)

        return self.pressed_key

    def hook(self, event):
        """hook"""

        if event.event_type == "down":
            pass
        elif event.event_type == "up":
            self.pressed_key = False
