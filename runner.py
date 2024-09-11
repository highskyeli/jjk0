from character import Character
from wordle import playWordle
from item import Item0
from steps import stepcounter
import steps 


flashlight = Item0("Flashlight", "Light")

Map = Item0("Map", "Direction")


maincharacter = Character("", 100, [], "" )
maincharacter.name = input("Tell me your name brave warrior. ")
maincharacter.rizz = input("What level of Looksmax Mogger are you? ")


npccharacter = Character("The Traveler", 100, [], "")

walk = input("You are lost in a forest, where would you like to go? N/S/E/W? ")


print("Welcome to the FOREST OF DOOM!!! Figure your way out of the forest before the skinwalker gets you. Work quick before you run out of steps. ")
    



if walk == "N":

    flashlightopp = input("You come up to a farm and see a flashlight. Would you like to have it in your inventory. (y/n)")

    if flashlightopp == "y":
        stepcounter()
        maincharacter.inventory.append(flashlight.name)
        walk = input("You are still lost in a forest, where would you like to go? N/S/E/W? ")
    else:
        print("You are lost in the forest. Game Over.")

    print(steps)
    

elif walk == "S":
    mapopp = input(npccharacter.name + " Hello Fellow Traveler, I am the Traveler. I am here to help you find your way out of the forest. I have a map that will help you find your way out of the forest. But to gain the map, you must solve this puzzle. Would you like to have it in your inventory? (y/n)")
   
    if mapopp == "y":
        stepcounter()
        playWordle
        maincharacter.inventory.append(Map.name)
        walk = input("You are still lost in a forest, where would you like to go? N/S/E/W? ")
    else:
        print("You are lost in the forest. Game Over.")

elif walk == "E":
    runaway = input("You walk as far as you can. There's a fog beginning to rustle between the trees. You hear a screech in the mist, and you panick. What do you do? (Run/Fight)")
    if runaway == "Run":
        print("You run as fast as you can, but the fog is too thick. You are eaten by a skinwalker. Game Over.")
    elif runaway == "Fight":
        print("You fight the skinwalker. You have no weapon, so using your bare hands, you manage to kill the skinwalker. However, as the mist goes away, you see yourself. On the floor. Pale and Paralyzed. You have fallen asleep. ")

elif walk == "W":
    if flashlight.name in maincharacter.inventory and Map.name not in maincharacter.inventory:
        print("Find a map, you don't know where you are.")
    elif flashlight.name not in  maincharacter.inventory and Map.name in maincharacter.inventory:
        print("Look for a flashlight, you don't know where you are.")
    elif flashlight.name in maincharacter.inventory and Map.name in maincharacter.inventory:
        print("You have found your way out. Congrats.")


print(steps)