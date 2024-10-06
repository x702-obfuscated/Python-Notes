import random

class Player():

    def __init__(
        self,
        name = "Hero",
        health = 100,
        magic = 50,
        stamina = 75,
        speed = 1
    ):
        self.name = name
        self.health = health
        self.magic = magic
        self.stamina = stamina
        self.speed = speed

        self.equipped_weapon = None
        self.equipped_armor = None
     
        self.bag = {
            "Key Items":[],
            "Weapons":[],
            "Armor":[],
            "Potions":[],
        }
    


    def roll_dice(self, number = 1 , d = 20):
        rolls = []
        for n in range(number):
            rolls.append(random.randint(1,d))
        
        return max(rolls)

    def initiative(self):
        roll = roll_dice()
        return roll + speed

    def attack(self,weapon_modifier, difficulty = 1):
        roll = roll_dice()
        if roll <= difficulty:
            return 0
        return roll * weapon_modifier

    def defend(self, armour_modifier, difficulty= 1):
        roll = roll_dice()
        if roll <= difficulty:
            return 0
        return roll * armor_modifier
    
    def flee(self, difficulty_modifier = 1):
        roll = roll_dice()
        if roll <= difficulty:
            return 0
        return roll * speed

    def open_bag(self): 
        return self.bag

    def display_attributes(self):
        for key, item in vars(self).items():
            print(f"{key} : {item}")



if __name__ == "__main__":

    player1 = Player()
    player1.display_attributes()