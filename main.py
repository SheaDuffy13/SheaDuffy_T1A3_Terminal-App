import random
import time
import clearing
from simple_term_menu import TerminalMenu
import ast

#other pages
import classes as c
import art

running_game = True
menu = True
play = False
INVENTORY_MENU_RUN = False
CABIN = False

def save():
    save_list = [
        user_name,
        str(user.coinpurse),
        ''.join(str(user.linen_bag)),
        str(user.fishbucket)
    ]
    with open("save.txt", "w") as sf:
        sf.write("\n".join(save_list))

# Home Screen
clearing.clear()
print(art.moon_art)
print('')
print("    ><><><><><><><><><><><><")
print("    ><><> Master Thief <><><")
print("    ><><><><><><><><><><><><")
print()
home_input = input("    Press Enter to continue... ")
clearing.clear()

# Main Program
while running_game:
    while menu:
        clearing.clear()
        art.draw()
        print(" 1. NEW GAME")
        print(" 2. LOAD GAME")
        print(" 3. QUIT GAME")
        art.draw()
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
                with open("save.txt") as sf:
                    file = sf.readlines()
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
            inventory_menu_items = ["back", ""] + usr_inv
            inventory_menu = TerminalMenu(
                inventory_menu_items,
                title = "Inventory\n",
                skip_empty_entries = True,
                clear_screen = True
            )
            inv_sel = inventory_menu.show()
            if inv_sel == 0:
                INVENTORY_MENU_RUN = False
                play = True
            # if inv_sel == 1:
            #     print("See you next time")
            #     time.sleep(0.7)
            #     # save()
            #     quit()
            if inv_sel >= 2:
                print(f"A {inventory_menu_items[inv_sel]}!")
                time.sleep(1)
        menu_run()


# MAIN GAME
    while play:
        save()
        clearing.clear()
        art.draw2()
        # print(f"{user.name} has {user.coinpurse} coins, {user.linen_bag} in bag and {user.fishbucket} fish")
        art.draw2()
        # input()
        print(art.mountain_art)

        print("\n1: loot chest   2: go to cabin   f: fish at the old pond                 i: inventory    m: main menu    e: exit")
        user_input = input("\n: ")
        if user_input == "m":
            play = False
            menu = True
            save()
            print("\nAutosaving...")
            time.sleep(0.4)

        if user_input == "1":
            c.old_chest2.loot(user)

        if user_input == "2":
            while True:
                # c.kitchen_drawer.loot(user)
                clearing.clear()
                print(art.cabin_art)
                art.draw2()
                print("You've approached a lone cabin. It looks like no one is home. \na to approach or e to go back")
                art.draw2()
                cinput = input(": ")
                if cinput == "a":
                    CABIN = True
                    while CABIN:
                        clearing.clear()
                        print(art.room_art)
                        print("You/'ve slipped into the cabin and see an old chest in the corner.\n \no: open chest \ne: leave")
                        cinput = input(": ")
                        if cinput == "o":
                            c.kitchen_drawer.loot(user)
                            continue
                        if cinput == "e":
                            CABIN = False
                else:
                    break

        if user_input == "f":
            import fishing as f
            f.fishing()
            clearing.clear()
            print(art.road_art)
            print(f"You came back from the trip with {f.fish} fish")
            user.fishbucket.add(f.fish)
            print(f"{user.fishbucket} total in inventory")
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
