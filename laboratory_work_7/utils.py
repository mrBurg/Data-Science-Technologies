"""Utils"""

from typing import Callable
from dataclasses import dataclass
import time
from pathlib import Path

import pandas as pd


@dataclass
class Utils:
    """Utils"""

    @staticmethod
    def read_excel(file_path: Path, file_name: str, **kwargs):
        """File reading"""

        full_path = file_path / file_name

        if not full_path.exists():
            raise FileNotFoundError(f"Файл не знайдено: {full_path}")

        file_data = pd.read_excel(full_path, **kwargs)

        print("Джерело даних: ", full_path)

        return file_data

    @staticmethod
    def loop(loop_callback: Callable[[], bool], speed=0.01):
        """loop"""

        while loop_callback():
            time.sleep(speed)
