
import random
import functions
import os

# player stats
player_hp = 100
player_strength = 50
player_agility = 30


# enemy stats
base_hp_monsters = 100
base_dmg_monsters = 60

skeleton_hp = base_hp_monsters
skeleton_dmg = base_dmg_monsters

zombie_hp = base_hp_monsters + 50
zombie_dmg = base_dmg_monsters + 20

dragon_hp = base_hp_monsters + 100
dragon_dmg = base_dmg_monsters + 60

cthulhu_hp = base_hp_monsters + 150
cthulhu_dmg = base_dmg_monsters + 90

#difficulty modifiers
shallows = 0.8
open_ocean = 1.0
nightmare = 1.5
doom_eternal = 2.5

# items

# default menu options
location_menu = "main"
difficulty_choice = "Open Ocean"

while True:
    if location_menu == "main":
        print("Welcome to Mr. Gallo's Dungeon! \n")
        print("[1] Play")
        print("[2] Class Selection")
        print("[3] Difficulty Selection")
        print("[4] A Message From The Developers")
        choice = int(input("Choice: "))

        if choice == 1:
            print("Welcome to the HMS Uthman.")
            location_menu = "start_game"
        # player classes
        elif choice == 2:
            location_menu = "class"
        # player difficulty
        elif choice == 3:
            location_menu = "difficulty"

        elif choice == 4:
            print("Long ago before grade 11 we were very bad coders but now we are pro")
            
    elif location_menu == "difficulty":
        print("Choose Difficulty:")
        print(f"Current difficulty: {difficulty_choice} \n")
        print("[1] Shallows") #easy
        print("[2] Open Ocean") #normal
        print("[3] Nightmare") #hard
        print("[4] Doom Eternal") #hell 
        print("[5] Back To Main Menu")
        difficulty_choice = int(input("> "))
    
        if difficulty_choice == 1:
            print("You have chosen the Shallows.")
            base_hp_monsters *= shallows
            base_dmg_monsters *= shallows
        elif difficulty_choice == 2:
            print("You have chosen the Open Ocean")
            base_hp_monsters *= open_ocean
            base_dmg_monsters *= open_ocean
        elif difficulty_choice == 3:
            print("You have chosen Nightmare")
            base_hp_monsters *= nightmare
            base_dmg_monsters *= nightmare
        elif difficulty_choice == 4:
            print("YOU HAVE CHOSEN DOOM ETERNAL")
        elif difficulty_choice == 5:
            location_menu = "main"
        else:
            
            pass
            #we use exceptions for wrong values
        base_hp_monsters *= doom_eternal
        base_dmg_monsters *= doom_eternal
        

    elif location_menu == "class":
        print("[1] Rogue")
        print("[2] Berserker")
        print("[3] Knight")
        class_choice = int(input("Choose a class: "))

        if class_choice == 1:
            print("You chose Rogue!")
            chosen_class = "rogue"
            player_hp /= 1.5
            player_strength /= 1.5
            player_agility *= 2

        elif class_choice == 2:
            print("You chose Berserker!")
            chosen_class = "berserker"
            player_hp *= 1.5
            player_strength *= 1.5
            player_agility /= 2


        elif class_choice == 3:
            print("You chose Knight!")
            chosen_class = "knight"
            player_hp *= 1.2
            player_strength *= 1.2
            player_agility *= 1.2
        
        #max HPs
        if chosen_class == "rogue" and player_hp <= 150:
            player_hp = 150
        elif chosen_class == "berserker" and player_hp <= 240:
            player_hp = 240
        elif chosen_class == "knight" and player_hp <= 180:
            player_hp = 180
