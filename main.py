import random
import time
import clearing

import main_menu

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
    # clears screen
    clearing.clear()
user_name = input('Enter your thief\'s name: ')
print('')
print(f'Hide yo kids, hide yo wife, and hide yo husband.. {user_name} is robbing everybody out here')
time.sleep(5)
clearing.clear()

# Main Program
main_menu.menu()