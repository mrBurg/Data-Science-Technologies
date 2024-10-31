"""Laboratory work 7"""

# pylint: disable=E0401

from pathlib import Path

from utils import Utils
from menu import Menu
from rendering import Rendering as Render

if __name__ == "__main__":
    FILE_PATH = Path(__file__).parent.joinpath("./").resolve()
    FILE_NAME = "Data_Set_6.xlsx"
    START_COLUMN = 2
    GRAPH_TITLE = "Sales chart"
    X_LABEL = ("Region",)
    Y_LABEL = ("Total",)

    file_data = Utils.read_excel(FILE_PATH, FILE_NAME)
    file_data = Utils.file_parsing(
        file_data, col_start=START_COLUMN, replacer={"n.a.": 0, "not avilable": 0}
    )

    columns = file_data.iloc[:, START_COLUMN:].columns

    menu = Menu([*columns, "ALL"])

    if menu.selected < 0:
        match menu.selected:
            case -1:
                print("Відмінено користувачем")
    else:
        Utils.clear_cinsole()

        match menu.selected:
            case _ if menu.selected == len(columns):
                print(file_data.iloc[:, START_COLUMN:].values)
                Render.show(
                    file_data.iloc[:, START_COLUMN:].values,
                    labels=list(columns),
                    title=GRAPH_TITLE,
                    xlabel=X_LABEL,
                    ylabel=Y_LABEL,
                )
            case _:
                print(f"Selected item {menu.selected}")
                print(file_data[columns[menu.selected]])
                Render.show(
                    file_data[columns[menu.selected]].values,
                    labels=columns[menu.selected],
                    title=GRAPH_TITLE,
                    xlabel=X_LABEL,
                    ylabel=Y_LABEL,
                )
