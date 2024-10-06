import random

class Player():
    '''Defines a 'Player' of a classic role playing game.'''

    num_of_players = 0      # Class Variable

    @classmethod
    def from_dict(cls, player_info):
        '''Class Methods, returns a Player instance from a passed dictionary'''
        name = player_info["name"]
        health = player_info["health"]
        magic = player_info["magic"]
        stamina = player_info["stamina"]
        speed = player_info["speed"]

        return cls(name,health,magic,stamina,speed)


    def __init__(
        self, name = "Hero", health = 100, 
        magic = 50, stamina = 75, speed = 1
    ):
        '''Constructor: creates a Player instance'''
        Player.num_of_players += 1
        self.name = name                    # Instance Variable
        self.health = health                # Instance Variable
        self.magic = magic                  # Instance Variable
        self.stamina = stamina              # Instance Variable
        self.speed = speed                  # Instance Variable

        self.equipped_weapon = None         # Instance Variable
        self.equipped_armor = None          # Instance Variable
     
        self.bag = {                        # Instance Variable
            "Key Items":[],
            "Weapons":[],
            "Armor":[],
            "Potions":[],
        }
    


    def roll_dice(self, number = 1 , d = 20):
        '''Method to simulate dice roll'''
        rolls = []
        for n in range(number):
            rolls.append(random.randint(1,d))
        
        return max(rolls)

    def initiative(self):
        '''Method to roll for initiative'''
        roll = roll_dice()
        return roll + speed


    def attack(self,weapon_modifier, difficulty = 1):
        '''Method to return attack damage value'''
        roll = roll_dice()
        if roll <= difficulty:
            return 0
        return roll * weapon_modifier

    def defend(self, armour_modifier, difficulty= 1):
        '''Method to return defense attempt value'''
        roll = roll_dice()
        if roll <= difficulty:
            return 0
        return roll * armor_modifier
    
    def flee(self, difficulty_modifier = 1):
        '''Method to return flee attempt value'''
        roll = roll_dice()
        if roll <= difficulty:
            return 0
        return roll * speed

    def open_bag(self):
        '''Method to return the bag contents''' 
        return self.bag

    def display_vars(self):
        '''Method to display all instance variables'''
        for key, item in vars(self).items():
            print(f"{key} : {item}")