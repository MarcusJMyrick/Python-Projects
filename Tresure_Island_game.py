from turtle import left


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Welcome to Treasure island. Your mission is to find the treasure!')
road = input('You walk down a two way plit pathway and must choose between the left or right road. Please type "Left" or "Right". ').lower()

if road == "left":
    flood = input('The road begins to flood you hear strange noises coming from behind you. Do you "swim" or "wait" ').lower()
    if flood == "wait":
        door = input('You are driffed off into the water and washed up on another part of the island on this part of the island there is a castle with three doors "red" "blue" or "yellow". Pick the door you want to enter. ').lower()
        if door == "yellow":
            print("You win! You found the treasure! Thanks for playing. ")
        elif door == "red":
            print("Eaten By a dragon. ")
        elif door == "blue":
            print("You were burned by a fire. Game Over. ")
        else:
            print("Game Over. ")
    else:
        print("You were attacked by a sea beast. Game Over.  ")
else:
    print("You fell into a hole. Game Over. ")
