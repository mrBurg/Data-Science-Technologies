"""Utils"""

# pylint: disable=R0913

from typing import Callable
import time
from pathlib import Path
import os

import pandas as pd

pd.set_option("future.no_silent_downcasting", True)


class Utils:
    """Utils"""

    @staticmethod
    def clear_cinsole():
        """clear_cinsole"""

        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def read_excel(file_path: Path, file_name: str, **kwargs):
        """read_excel"""

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

    @staticmethod
    def file_parsing(
        data_frame,
        row_start=None,
        row_end=None,
        col_start=None,
        col_end=None,
        replace=None,
    ):
        """File parsing"""

        if replace is None:
            replace = {}

        data_frame.iloc[slice(row_start, row_end), slice(col_start, col_end)] = (
            data_frame.iloc[slice(row_start, row_end), slice(col_start, col_end)]
            .map(lambda x: x.strip() if isinstance(x, str) else x)
            .replace(replace)
        )

        return data_frame
