from character import Character
from wordle import playWordle
from item import Item0
from steps import stepcounter
import steps 


flashlight = Item0("Flashlight", "Light")

Map = Item0("Map", "Direction")


maincharacter = Character("", 100, [], "" )
maincharacter.name = input("Tell me your name brave warrior.")
maincharacter.rizz = input("What level of Looksmax Mogger are you?")


npccharacter = Character("The Traveler", 100, [], "")

walk = input("You are lost in a forest, where would you like to go? N/S/E/W?")


print("Welcome to the FOREST OF DOOM!!! Figure your way out of the forest before the skinwalker gets you. Work quick before you run out of steps. ")
d1 = input("You come up to a farm and see a flashlight. Would you like to have it in your inventory. (y/n)")

if d1 == "y":
    stepcounter()
    maincharacter.inventory.append(flashlight.name)
    



elif walk == "N":
    stepcounter()
    print(steps)
    

elif walk == "S": 
    print(npccharacter.name + "")

elif flashlight.name in maincharacter.inventory and Map.name not in maincharacter.inventory:
    print()
elif flashlight.name not in  maincharacter.inventory and Map.name in maincharacter.inventory:
    print("Look for a flashlight, you don't know where you are.")


print(steps)