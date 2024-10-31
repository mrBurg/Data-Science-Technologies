"""Laboratory work 7"""

# pylint: disable=E0401

from menu import Menu

if __name__ == "__main__":
    print("Ready")

    options = ["Опція 1", "Опція 2", "Опція 3", "Вихід"]
    menu = Menu(options)

    if menu.selected_option < 0:
        match menu.selected_option:
            case -1:
                print("Відмінено користувачем")
    else:
        LAST_OPTIONS = len(options) - 1

        match menu.selected_option:
            case _ if menu.selected_option == LAST_OPTIONS:
                print("Вихід із застосунку")
            case _:
                print(f"Selected item {menu.selected_option}")
