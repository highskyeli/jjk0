"""

class Character:

    Represents a character in the game.
    
    Attributes:
        name (str): The name of the character.
        health (int): The current health of the character.
        inventory (list): The items in the character's inventory.
        dialogue (dict): The dialogue responses for the character.
    
    Methods:
        talk_to_player(player): Prints the appropriate dialogue response based on the player's message.
        receive_item(item): Adds the given item to the character's inventory.
    """

class Character:
    def __init__(self, name, health, inventory, rizz):
        self.name = name
        self.health = health
        self.inventory = inventory
        
        self.rizz = rizz


    def receive_item(self, item):
        self.inventory.append(item) 



