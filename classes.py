
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

# with open("save.txt") as f:
#     file = f.readlines()
#     x = file[0].strip()
#     y = file[1].strip()
#     # print(file[0])
#     # print(file[1])
#     print(x)
#     print(y)

# user = Player("Seth")

# chest = Chest(["rusty dagger"], 30)
# chest.loot(user)
# print(chest.loose_coins)
# print(f"{user.name} has {user.coinpurse} in their coinpurse")