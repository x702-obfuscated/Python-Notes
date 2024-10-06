#Importing 'Player' class from the 'player' module (player.py)
from player import Player       

# Constructing a 'Player' object using the default Player() constructor
player1 = Player()  # The object is referenced using the variable 'player1'

# Accessing and printing the 'name' attribute of 'player1'
print(player1.name)


# Calling the 'display_attributes()' method of 'player1'
player1.display_attributes()