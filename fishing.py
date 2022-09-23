import time
import random
import clearing
import art

fish = 0

def draw():
    print('\nXx--------------------------------------------------------xX\n')

def fishing():
    while True:
        def cast():
            text = ['..', '..', '!!', '..', '..', '..']
            sample = random.sample(text, k=5)
            global fish
            for char in sample:
                print(char)
                time.sleep(0.5)
                if char == '!!':
                    fish += 1
                    print('You got a fish!')
                    time.sleep(1)
                    break
            if '!!' not in sample:
                print('No fish..')
                time.sleep(0.7)
                return

        clearing.clear()
        print(art.lake_art)
        draw()
        print(" You\'ve approach a murky pond and set up your rod\n")
        print(" f: to fish \n i: to check fish bucket \n e: to end session")
        draw()
        menu_choice = input(': ')
        if menu_choice == 'f':
            clearing.clear()
            art.lake_art()
            cast()
        if menu_choice == 'i':
            clearing.clear()
            art.lake_art()
            print(f'\nYou have {fish} fish')
            input()
        if menu_choice == 'e':
            return fish
