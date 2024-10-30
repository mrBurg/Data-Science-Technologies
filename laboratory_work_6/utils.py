"""Utils"""

from dataclasses import dataclass
from pathlib import Path

import pandas as pd
import numpy as np


@dataclass
class Utils:
    """Utils"""

    def read_excel(self, file_path: Path, file_name: str, **kwargs):
        """File reading"""

        full_path = file_path / file_name

        if not full_path.exists():
            raise FileNotFoundError(f"Файл не знайдено: {full_path}")

        file_data = pd.read_excel(full_path, **kwargs)

        print("Джерело даних: ", full_path)

        return file_data

    def create_sequence(self, data, seq_size):
        """create_sequences"""

        seq1, seq2 = [], []

        for i in range(seq_size, len(data)):
            seq1.append(data[i - seq_size : i])
            seq2.append(data[i])

        return np.array(seq1), np.array(seq2)
