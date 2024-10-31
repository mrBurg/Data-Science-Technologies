"""Laboratory work 7"""

# pylint: disable=E0401

from pathlib import Path
import math as mt

import pandas as pd

from utils import Utils
from menu import Menu
from rendering import Rendering as Render
from model import Model

if __name__ == "__main__":
    FILE_PATH = Path(__file__).parent.joinpath("./").resolve()
    FILE_NAME = "Data_Set_6.xlsx"
    START_COLUMN = 2
    GRAPH_TITLE = "Sales chart"
    X_LABEL = "Months"
    Y_LABEL = "Sales"
    EXTRAPOL_COEF = 0.3

    model = Model()

    file_data = Utils.read_excel(FILE_PATH, FILE_NAME)
    file_data = Utils.file_parsing(
        file_data, replace={"n.a.": 0, "not avilable": 0, ",": "."}
    )

    regions_col = file_data.columns[1]
    regions = pd.Series(file_data.iloc[:, 1:START_COLUMN].values.ravel()).unique()
    print("Unique regions > ", regions)

    columns = file_data.iloc[:, START_COLUMN:].columns

    aggregation_dict = {col: "sum" for col in columns}
    grouped_file_data = file_data.groupby(regions_col).agg(aggregation_dict)
    print(f"Grouped data by {regions_col} >\n", grouped_file_data)

    menu = Menu(["ALL", *regions])

    if menu.selected < 0:
        match menu.selected:
            case -1:
                print("Відмінено користувачем")
    else:
        Utils.clear_console()

        match menu.selected:
            case _ if menu.selected == 0:
                data_to_show = []
                labels_to_show = []

                for i, item in enumerate(grouped_file_data.values):
                    data_to_show.append(item)
                    data_to_show.append(
                        model.mnk_extrapol(
                            item, mt.ceil(len(columns) * EXTRAPOL_COEF)
                        ).ravel()
                    )
                    labels_to_show.append(regions.tolist()[i])
                    labels_to_show.append(f"{regions.tolist()[i]} ext")

                Render.show(
                    *data_to_show,
                    labels=labels_to_show,
                    title=GRAPH_TITLE,
                    xlabel=X_LABEL,
                    xticks=list(columns),
                    ylabel=Y_LABEL,
                )

            case _:
                data_to_show = grouped_file_data.values[menu.selected - 1]
                extrapol_data_to_show = model.mnk_extrapol(
                    grouped_file_data.values[menu.selected - 1],
                    mt.ceil(len(columns) * EXTRAPOL_COEF),
                )
                labels_to_show = [
                    regions.tolist()[menu.selected - 1],
                    f"{regions.tolist()[menu.selected - 1]} ext",
                ]

                Render.show(
                    data_to_show,
                    extrapol_data_to_show,
                    labels=labels_to_show,
                    title=GRAPH_TITLE,
                    xlabel=X_LABEL,
                    xticks=list(columns),
                    ylabel=Y_LABEL,
                )
