class Character:
"""
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
        def __init__(self, name, health, inventory):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.dialogue = dialogue

    def talk_to_player(self, player):
        for sentence in self.dialogue:
            if player_msg == sentence:
                print(self.dialogue[sentence])

    def receive_item(self, item):
        self.inventory.append(item) 
