"""Laboratory work 7"""

# pylint: disable=E0401

from pathlib import Path

import pandas as pd
import numpy as np

from utils import Utils
from menu import Menu
from rendering import Rendering as Render

if __name__ == "__main__":
    FILE_PATH = Path(__file__).parent.joinpath("./").resolve()
    FILE_NAME = "Data_Set_6.xlsx"
    START_COLUMN = 2
    GRAPH_TITLE = "Sales chart"
    X_LABEL = "Month"
    Y_LABEL = "Sales"

    file_data = Utils.read_excel(FILE_PATH, FILE_NAME)
    file_data = Utils.file_parsing(
        file_data, replace={"n.a.": 0, "not avilable": 0, ",": "."}
    )

    regions = pd.Series(file_data.iloc[:, 1:START_COLUMN].values.ravel()).unique()
    print("regions > ", regions)

    columns = file_data.iloc[:, START_COLUMN:].columns
    print("columns > ", columns)

    aggregation_dict = {col: "sum" for col in columns}

    grouped_file_data = file_data.groupby("SALES_BY_REGION").agg(aggregation_dict)
    print("grouped_file_data > ", grouped_file_data)
    print("grouped_file_data.values >", grouped_file_data.values)

    # Render.show(grouped_file_data.values[0], labels=regions.tolist())

    menu = Menu(["ALL", *regions])

    if menu.selected < 0:
        match menu.selected:
            case -1:
                print("Відмінено користувачем")
    else:
        Utils.clear_cinsole()

        data_to_show = []
        labels_to_show = []

        match menu.selected:
            case _ if menu.selected == 0:
                data_to_show = grouped_file_data.values.T
                labels_to_show = regions.tolist()

            case _:
                data_to_show = grouped_file_data.values[menu.selected - 1]
                labels_to_show = [regions.tolist()[menu.selected - 1]]

        Render.show(
            data_to_show,
            labels=labels_to_show,
            title=GRAPH_TITLE,
            xlabel=X_LABEL,
            xticks=list(columns),
            ylabel=Y_LABEL,
        )
