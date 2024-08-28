import Character from character
import Item from item
import playWordle from wordle

print("Welcome to the game!")
d1 = input("You come up to a field and see a star! Do you want to pick it up? (y/n)")
if d1 == "y":
    star = Item("Star", "A shiny star", 10)
    dla = input("You pick up the star and it shines brightly. Now you see a dude. Want to talk to him? (y/n)")
    if dla == "y":
        character = Character("Dude", 100, [], {"Hello": "Hello there!"})
        character.talk_to_player("Hello")