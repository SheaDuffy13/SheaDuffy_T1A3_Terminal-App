import time
import random
import clearing
import art
import fish_art as fa

fish = 0

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
                        print("This fish seems a little strange.. better not eat it")
                    input("\n\ncontinue..")
                    break
            if '!!' not in sample:
                print('No fish..')
                time.sleep(0.7)
                return

        clearing.clear()
        print(art.lake_art)
        print(" You\'ve approached a murky pond and set up your rod.")
        print(" Something seems a little off about the water.. almost as if it has a green glow\n")
        print(" f: to fish \n i: to check fish bucket \n e: to end session")
        menu_choice = input(':')
        if menu_choice == 'f':
            clearing.clear()
            print(art.fishingline_art)
            cast()
        elif menu_choice == 'i':
            clearing.clear()
            print(art.lake_art)
            print(f'\nYou have {fish} fish in you bucket')
            print(art.bucket_art)
            input("continue..")
        elif menu_choice == 'e':
            return fish
        else:
            continue
