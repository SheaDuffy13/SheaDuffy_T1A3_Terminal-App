
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

class Player:
    def __init__(self, name):
        self.name = name
        self.coinpurse = Money(0)
        self.linen_bag = Inventory(None)

class Chest:
    def __init__(self, items, coins):
        self.loose_items = Inventory(items)
        self.loose_coins = Money(coins)

    #transfer contents to character
    def loot(self, player):
        player.coinpurse.add(self.loose_coins.coins)
        self.loose_coins = 0
        player.linen_bag.add(self.loose_items.contents)
