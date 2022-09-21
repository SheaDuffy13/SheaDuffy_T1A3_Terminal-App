class location:
    def __init__(self, description):
        self.description = description
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.pickups = []
    
    def add_pickup(self, x):
        self.pickups.append(x)

    def remove_pickup(self, x):
        self.pickups.remove(x)
        return x

living_room = location("A fancy living Room \n")
kitchen = location("A kitchen with vase of flowers on the counter \n")
kitchen.add_pickup("flower ")
bedroom = location("A bedroom with a gold ring on the nightstand \n")
bathroom = location("A bathroom \n")
bedroom.add_pickup("")
porch = location("A creaky porch \n")

living_room.north = bedroom
living_room.south = porch
living_room.east = kitchen
living_room.west = bathroom

# print(living_room.description)

location = living_room

response = ""
while response != "quit":
    response = input(f"You see {location.description}")
    if response == "north":
        location = location.north
    elif response == "south":
        location = location.south
    elif response == "east":
        location = location.east
    elif response == "west":
        location = location.west
    elif response.startswith("take "):
        for pickup in location.pickups:
            if response.endswith(pickup):
                location.remove_pickup(pickup)
                success = True
                break
        if success:
            print(f"Picked up {pickup}")
        else:
            print("Command not recognized")