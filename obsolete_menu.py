# import main_menu
import time
from simple_term_menu import TerminalMenu
import classes as cl

running_game = True
menu = True
play = False
inventory = False


while running_game:
    while menu:
        def menu_run():
            global menu
            global inventory
            options = ["Continue", "Inventory", "Exit Game"]
            terminal_menu = TerminalMenu(
                options,
                title="  Title\n",
                menu_highlight_style = ("bg_black", "fg_yellow"),
                menu_cursor_style = ("fg_blue", "bold"),
                clear_screen=True
            )

            inventory_menu_items = ["back", ""] + cl.bag_list
            inventory_menu_back = False
            inventory_menu = TerminalMenu(
                inventory_menu_items,
                skip_empty_entries = True,
                clear_screen = True
            )

            menu_select = terminal_menu.show()
            if menu_select == 0:
                print('Continue selected')
                time.sleep(1)

            #Inventory menu select
            elif menu_select == 1:
                print('Inventory Selected')
                inventory = True
                
                #Inventory menu
                while not inventory_menu_back:
                    inv_sel = inventory_menu.show()
                    if inv_sel == 0:
                        time.sleep(1)
                        inventory_menu_back = True
                    if inv_sel == 2:
                        print(f"hi {inventory_menu_items[1]}")
                        print(f"Y {inventory_menu_items[inv_sel]}!")
                        time.sleep(1)
                    if inv_sel >= 3:
                        print(f"A {inventory_menu_items[inv_sel]}!")
                        time.sleep(1)

            #Back to main_menu   
            elif menu_select == 2:
                print("Quit Selected")
                # menu = False
                quit()
        menu_run()

                


    while play:
        pass

    print('running game')
    input('')