import time
import random
import clearing
import ast
import art
class Money:
    def __init__(self, coins):
        self.set(coins)
  
    def set(self, coins):
        self.coins = coins

    def add(self, coins):
        self.coins += coins

    def __str__(self):
        return f"{self.coins}"

class Inventory:
    def __init__(self, contents):
        self.set(contents)

    def set(self, contents):
        self.contents = contents

    def add(self, contents):
        self.contents += contents

    def __str__(self):
        return f"{self.contents}"

class Player:
    def __init__(self, name):
        self.name = name
        self.coinpurse = Money(0)
        self.linen_bag = Inventory([])
        self.fishbucket = Money(0)

class Chest:
    def __init__(self, items, coins):
        self.loose_items = Inventory(items)
        self.loose_coins = Money(coins)

    #transfer contents to character
    def loot(self, player):
        clearing.clear()
        print(art.chest_art)
        art.draw()
        print("\nYou investigate the chest...")
        time.sleep(1)
        try:
            print(f"\nYou found: {', '.join(self.loose_items.contents)} and {self.loose_coins.coins} coins")
            input()
            player.coinpurse.add(self.loose_coins.coins)
            self.loose_coins = 0
            player.linen_bag.add(self.loose_items.contents)
            self.loose_items = []
        except AttributeError:
            print("\nAlready looted")
            time.sleep(1.2)


def randloot():
    chest_items = ["rusty dagger", "gold ring", "cheese wheel", "moldy bread roll", "moth-eaten linens",
                "baggie of strange herbs", "silk pantaloons", "silver necklace", "skooma",
                "a worn book", "aged wine", "emerald ring", "pearl earrings", 
                "silver fork", "bottle of rum", "silver ring", "a cabbage", "small animal skull"]
    randloot.randitems = random.sample(chest_items, k = random.randint(2,6))
    randloot.rcoins = random.randint(0, 80)
    return randloot.rcoins, randloot.randitems

randloot()
old_chest1 = Chest(randloot.randitems, randloot.rcoins)
randloot()
old_chest2 = Chest(randloot.randitems, randloot.rcoins)
randloot()
old_chest3 = Chest(randloot.randitems, randloot.rcoins)

print(old_chest2.loose_items)
print(', '.join(old_chest2.loose_items.contents))

# print(old_chest1.loose_items, old_chest1.loose_coins)
# print(old_chest2.loose_items, old_chest2.loose_coins)


#Testing Ground

# user = Player("Jay")
# user.coinpurse.set(30)
# user.linen_bag.set(["rusty dagger", "gold ring"])
# print(user.linen_bag)
# old_chest = Chest(["rusty dagger", "gold ring"], 30)
# print(old_chest.loose_coins, old_chest.loose_items)
# print(f"{user.name} has {user.coinpurse} coins and {user.linen_bag} in their bag")
# time.sleep(2)
# old_chest.loot(user)
# print(f"{user.name} has {user.coinpurse} coins and {user.linen_bag} in their bag")
