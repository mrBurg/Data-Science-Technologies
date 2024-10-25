"""Utils"""

# pylint: disable=C0209, E0401

from dataclasses import dataclass
from pathlib import Path

import pandas as pd
import numpy as np
from keras.preprocessing import image
from skimage.color import rgb2lab


@dataclass
class Utils:
    """Utils"""

    def read_excel(self, file_path: Path, file_name, **kwargs) -> np.ndarray:
        """File reading"""

        full_file_path = file_path / file_name

        if not full_file_path.exists():
            raise FileNotFoundError(f"Файл не знайдено: {full_file_path}")

        file_data = pd.read_excel(full_file_path, **kwargs)

        print("Джерело даних: ", full_file_path)

        return file_data

    def get_average_color(self, path):
        """get_average_color"""

        img = image.load_img(path)
        img_data = image.img_to_array(img)
        lab = rgb2lab(img_data / 255.0)
        mean_color = np.mean(lab[:, :, 1:3], axis=(0, 1))

        return mean_color
