import time
from simple_term_menu import TerminalMenu

def menu():
    options = ["Continue", "Inventory", "Exit"]
    menu_exit = False
    terminal_menu = TerminalMenu(
        options,
        title="  Title\n",
        menu_highlight_style = ("bg_black", "fg_yellow"),
        menu_cursor_style = ("fg_blue", "bold"),
        clear_screen=True
        )

    while not menu_exit:
        menu_select = terminal_menu.show()
        if menu_select == 0:
            print('Continue selected')
            time.sleep(2)
        elif menu_select == 1:
            print('Inventory Selected')
            time.sleep(2)
        elif menu_select == 2:
            menu_exit = True
            print("Quit Selected")

# if __name__ == "__main__":
#     menu()


