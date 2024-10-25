"""Laboratory work 4"""

# pylint: disable=E1121, E0401, R0913, R0914

from pathlib import Path

import pylab

from utils import Utils
from model import Model
from voronin import Voronin
from olap_cube import OLAPcube


if __name__ == "__main__":
    root_file_path = Path(__file__).parent.joinpath("./").resolve()
    FILE_NAME = "data.xls"

    utils = Utils()

    file_data = utils.read_excel(root_file_path, FILE_NAME)

    print(file_data)

    model = Model(file_data)

    Voronin(model.integro, 100)
    OLAPcube(model.normals, model.integro)
