import time
import random
import clearing
import art
import fish_art as fa

fish = 0

def draw():
    print('\nXx--------------------------------------------------------xX\n')

def fishing():
    while True:
        def cast():
            text = ['..', '..', '!!', '..', '..', '..']
            sample = random.sample(text, k=5)
            global fish
            print("..")
            time.sleep(0.5)
            print("..")
            time.sleep(0.5)
            for char in sample:
                print(char)
                time.sleep(0.5)
                if char == '!!':
                    clearing.clear()
                    fish += 1
                    rand_fish = random.choice(fa.fish_art)
                    print(f"You got a fish! \n{rand_fish}")
                    if rand_fish == fa.fish1:
                        print("This fish seems a little strange.. better not eat it..")
                    # print(random.choice(fa.fish_art))
                    # time.sleep(1)
                    input("continue..")
                    break
            if '!!' not in sample:
                print('No fish..')
                time.sleep(0.7)
                return

        clearing.clear()
        print(art.lake_art)
        # draw()
        print(" You\'ve approach a murky pond and set up your rod\n")
        print(" f: to fish \n i: to check fish bucket \n e: to end session")
        # draw()
        menu_choice = input(': ')
        if menu_choice == 'f':
            clearing.clear()
            # print(art.lake_art)
            print(art.fishingline_art)
            cast()
        if menu_choice == 'i':
            clearing.clear()
            print(art.lake_art)
            print(f'\nYou have {fish} fish in you bucket')
            print(art.bucket_art)
            input("continue..")
        if menu_choice == 'e':
            return fish
