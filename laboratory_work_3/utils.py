"""Utils"""

from dataclasses import dataclass

import pandas as pd
import numpy as np


@dataclass
class Utils:
    """Utils"""

    def read_excel(self, file_path: str, file_name: str) -> np.ndarray:
        """File reading"""

        full_file_path = file_path / file_name

        if not full_file_path.exists():
            raise FileNotFoundError(f"Файл не знайдено: {full_file_path}")

        file_data = pd.read_excel(full_file_path)

        print("Джерело даних: ", full_file_path)

        return file_data

    def file_parsing(self, data_name, data):
        """File parsing"""

        values_data = []

        for _, values in data[[data_name]].items():
            values_data = values

        data_len = int(len(values_data))
        process_data = np.zeros((data_len))

        for i in range(data_len):
            process_data[i] = values_data[i].replace(",", ".")

        return process_data
