
class Money:
    def __init__(self, coins):
        # self.coins = coins
        self.set(coins)
  
    def set(self, coins):
        self.coins = coins

    def add(self, coins):
        self.coins += coins

    def __str__(self):
        return f"{self.coins}"

class Player:
    def __init__(self, name):
        self.name = name
        self.coinpurse = Money(0)
        self.linen_bag = []

class Chest:
    def __init__(self, items, coins):
        self.items = items  #items be a list of objects
        self.loose_coins = Money(coins)

    #transfer contents to character
    def loot(self, player):
        player.coinpurse.add(self.loose_coins.coins)
        self.loose_coins = 0
