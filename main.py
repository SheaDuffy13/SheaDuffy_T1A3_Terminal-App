import random
import time
import clearing
from simple_term_menu import TerminalMenu
import ast

import classes as c

running_game = True
menu = True
play = False
INVENTORY_MENU_RUN = False

def save():
    save_list = [
        user_name,
        str(user.coinpurse),
        ''.join(str(user.linen_bag)),
        str(user.fishbucket)
    ]
    with open("save.txt", "w") as f:
        f.write("\n".join(save_list))

def draw():
    print('Xx------------------------------xX')

def draw2():
    print('\nXx-------------------------------------------------------------------------------------xX\n')

# Home Screen
print('')
print("         ><><><><><><><><><><><><")
print("         ><><> Master Thief <><><")
print("         ><><><><><><><><><><><><")
print()
home_input = input('Press Enter to continue or e to exit.. ')
if home_input == 'e':
    exit()
else:
    clearing.clear()

# Main Program
while running_game:
    while menu:
        clearing.clear()
        draw()
        print(" 1. NEW GAME")
        print(" 2. LOAD GAME")
        print(" 3. QUIT GAME")
        draw()
        print("")
        choice = input('Select number: ')

        if choice == "1":
            user_name = input('Enter your thief\'s name: ')
            user = c.Player(user_name)
            user.coinpurse.set(0)
            user.linen_bag.set([])
            user.fishbucket.set(0)
            menu = False
            play = True

        if choice == "2":
            try:
                with open("save.txt") as f:
                    file = f.readlines()
                    user_name = file[0].strip()
                    usr_inv_load = ast.literal_eval(str(file[2].strip()))
                    user = c.Player(user_name)
                    user.coinpurse.set(int(file[1]))
                    user.linen_bag.set(usr_inv_load)
                    user.fishbucket.set(int(file[3]))
                clearing.clear()
                menu = False
                play = True
            except OSError:
                print("Save file not available..")
                input("Press enter to go back: ")

        if choice == "3":
            quit()

# INVENTORY MENU
    while INVENTORY_MENU_RUN:
        def menu_run():
            global play
            global INVENTORY_MENU_RUN
            usr_inv = ast.literal_eval(str(user.linen_bag))
            inventory_menu_items = ["back", "save & quit", ""] + usr_inv
            inventory_menu = TerminalMenu(
                inventory_menu_items,
                skip_empty_entries = True,
                clear_screen = True
            )
            inv_sel = inventory_menu.show()
            if inv_sel == 0:
                INVENTORY_MENU_RUN = False
                play = True
            if inv_sel == 1:
                print("See you next time")
                time.sleep(0.7)
                # save()
                quit()
            if inv_sel >= 3:
                print(f"A {inventory_menu_items[inv_sel]}!")
                time.sleep(1)
        menu_run()


# MAIN GAME
    while play:
        save()
        clearing.clear()
        draw2()
        print(f"{user.name} has {user.coinpurse} coins, {user.linen_bag} in bag and {user.fishbucket} fish")
        draw2()
        input()

        user_input = input('m: main menu \n1: loot chest \n2: loot kitchen drawer \ni: inventory \ne: exit \nf: fish at the old pond \n: ')
        if user_input == "m":
            play = False
            menu = True
            save()
            print("\nAutosaving...")
            time.sleep(0.4)
        if user_input == "1":
            old_chest = c.Chest(["rusty dagger", "gold ring"], 30)
            print(old_chest.loose_coins, old_chest.loose_items)
            time.sleep(0.7)
            old_chest.loot(user)
        if user_input == "2":
            kitchen_drawer = c.Chest(["silver fork"], 0)
            kitchen_drawer.loot(user)
            print(f"You have {user.coinpurse} coins and {user.linen_bag}")
            time.sleep(2)
        if user_input == "f":
            import fishing as f
            f.fishing()
            print(f"You came back from the trip with {f.fish} fish")
            user.fishbucket.add(f.fish)
            print(f"{user.fishbucket} in bucket")
            input()

        if user_input == "i":
            print('Inventory Selected')
            play = False
            INVENTORY_MENU_RUN = True
        if user_input == "e":
            print(f"See you next time, {user.name}")
            time.sleep(0.7)
            play = False
            running_game = False
