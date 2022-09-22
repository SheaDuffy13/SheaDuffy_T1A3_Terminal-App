import ast
import time
from simple_term_menu import TerminalMenu
import classes as cl


# play = True
# INVENTORY_MENU_RUN = False

# while play:
#     #Inventory menu
#     while INVENTORY_MENU_RUN:
def menu_run():
    global play
    global INVENTORY_MENU_RUN
    # from main import user
    #INVENTORY MENU
    usr_inv = ast.literal_eval(str(cl.user.linen_bag))
    inventory_menu_items = ["back", "save & quit", ""] + usr_inv
    inventory_menu = TerminalMenu(
        inventory_menu_items,
        skip_empty_entries = True,
        clear_screen = True
    )
    inv_sel = inventory_menu.show()
    if inv_sel == 0:
        INVENTORY_MENU_RUN = False
        
    if inv_sel == 1:
        print("See you next time")
        time.sleep(0.7)
        # save()
        quit()
        
    if inv_sel >= 3:
        print(f"A {inventory_menu_items[inv_sel]}!")
        time.sleep(1)
# menu_run()

    # selection = input("i for inventory, e for exit: ")

    #Inventory menu select
    # if selection == "i":
    #     print('Inventory Selected')
    #     INVENTORY_MENU_RUN = True
    # if selection == "e":
    #     print(f"See you next time {cl.user.name}")
    #     time.sleep(0.7)
    #     play = False
    #     # quit()




# user = cl.Player("Jay")
# user.coinpurse.set(30)
# user.linen_bag.set(["rusty dagger", "gold ring"])


# lili = ast.literal_eval(str(user.linen_bag))
# print(lili[0])
# print(type(lili))
