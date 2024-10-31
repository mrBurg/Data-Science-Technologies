""" KeyboardHandler """

# pylint: disable=E0401

from dataclasses import dataclass

import keyboard


@dataclass
class KeyboardHandler:
    """KeyboardHandler"""

    keys = {"up": False, "down": False, "q": False, "space": False}
    pressed_key = None

    def get_key(self):
        """get_key"""

        for i in self.keys:
            self.keys[i] = keyboard.is_pressed(i)

            if self.keys[i]:
                self.pressed_key = i

        keyboard.hook(self._hook)

        return self.pressed_key

    def _hook(self, event):
        """hook"""

        if event.event_type == "up":
            self.pressed_key = False
        elif event.event_type == "down":
            pass
