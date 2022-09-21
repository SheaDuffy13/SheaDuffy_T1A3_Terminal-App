import random
# from secrets import choice
import time
import clearing

import classes as c

running_game = True
menu = True
play = False

def save():
    save_list = [
        user_name,
        str(user.coinpurse)
    ]
    # sf = open("load.txt", "w")
    # for item in save_list:
    #     sf.write(item + "\n")
    # sf.close()
    with open("save.txt", "w") as f:
        f.write("\n".join(save_list))


def draw():
    print('Xx------------------------------xX')

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
            bag_list = ['rose', 'rusty dagger','baggie of strange herbs','gold ring']
            menu = False
            play = True
        if choice == "2":
            try:
                # sf = open("load.txt", "r")
                # load_file = sf.readlines()
                # if len(load_file) == 2:        # <----    update for number of saved parameters
                if menu is True:
                    with open("save.txt") as f:
                        file = f.readlines()
                        user_name = file[0].strip()
                        user.coinpurse.add(file[1].strip())

                    # user_name = load_file[0]
                    # user.coinpurse = int(load_file[1])
                    clearing.clear()
                    print(f"Welcome back, {user_name}")
                    time.sleep(1)
                    menu = False
                    play = True
                else:
                    print("Corrupt save file")
                    input("Press enter to go back: ")
            except OSError:
                print("Save file not available..")
                input("Press enter to go back: ")

        if choice == "3":
            quit()

    while play:
        # save()  #autosave
        clearing.clear()

        # print(chest.loose_coins)
        print(f"{user.name} has {user.coinpurse} in their coinpurse")

        user_input = input('Press e to exit back to menu: ')
        if user_input == "e":
            save()
            print("")
            print("Autosaving...")
            time.sleep(0.4)
            play = False
            menu = True
        if user_input == "s":
            chest = c.Chest(["rusty dagger"], 30)
            print(chest.loose_coins)
            time.sleep(0.7)
            chest.loot(user)
            print(chest.loose_coins)
            time.sleep(0.7)
        input("")