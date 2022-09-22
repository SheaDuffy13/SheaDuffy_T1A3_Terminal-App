import time
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

class Chest:
    def __init__(self, items, coins):
        self.loose_items = Inventory(items)
        self.loose_coins = Money(coins)

    #transfer contents to character
    def loot(self, player):
        player.coinpurse.add(self.loose_coins.coins)
        self.loose_coins = 0
        player.linen_bag.add(self.loose_items.contents)



#Testing Ground

# user = Player("Jay")
# user.coinpurse.set(0)
# user.linen_bag.set([])
# print(user.linen_bag)
# old_chest = Chest(["rusty dagger", "gold ring"], 30)
# print(old_chest.loose_coins, old_chest.loose_items)
# print(f"{user.name} has {user.coinpurse} coins and {user.linen_bag} in their bag")
# time.sleep(2)
# old_chest.loot(user)
# print(f"{user.name} has {user.coinpurse} coins and {user.linen_bag} in their bag")
