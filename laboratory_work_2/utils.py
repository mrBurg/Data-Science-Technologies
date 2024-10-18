"""Utils"""

from dataclasses import dataclass

import pandas as pd
import numpy as np


@dataclass
class Utils:
    """Utils"""

    def read_excel(self, file_path: str, file_name: str, data_name: str) -> np.ndarray:
        """File parsing"""

        full_file_path = file_path / file_name

        if not full_file_path.exists():
            raise FileNotFoundError(f"Файл не знайдено: {full_file_path}")

        file_data = pd.read_excel(full_file_path)

        print("Джерело даних: ", file_path)

        return np.array((file_data[[data_name]].values))
