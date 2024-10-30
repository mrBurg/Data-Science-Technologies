"""Laboratory work 5"""

# pylint: disable=E0401

from pathlib import Path

from utils import Utils
from cluster import Cluster


if __name__ == "__main__":
    root_file_path = Path(__file__).parent.joinpath("./").resolve()
    FILE_NAME = "user_behavior_dataset.xls"

    utils = Utils()
    cluster = Cluster()

    colums = ["Operating System", "App Usage Time (min/day)"]
    op_systems = ["Android", "iOS"]
    file_data = utils.read_excel(
        root_file_path,
        FILE_NAME,
        usecols=colums,
    )

    FILES_DIR = root_file_path / "images"

    cluster.point(file_data, op_systems, colums, cluster_num=4)
    cluster.picture(FILES_DIR, cluster_num=4, view_columns=5)
