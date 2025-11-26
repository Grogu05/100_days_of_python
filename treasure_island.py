print(''' *******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

      
print("Welcome to Treasure Island. Your mission is to find the treasure")
game= input("Your at a cross road. Where do you want to go? Left or Right?\n").lower()

if game == "right":
    print("You fell into a hole. Game over...")
    exit()
else:
    game = input("There is a lake infront of you. You can choose between waiting for a boat or swim over. Wait or Swim?\n").lower()
    if game == "swim":
        print("You got attacked by a trout. Game over...")
        exit()
    else:
        game = input("You got on a boat and crossed over safely. You find a hut nearby with 4 doors. Red, Blue, Green and Yellow. Which door will you choose?\n").lower()
        if game == "red":
            print("You walked inside and the moment the door closed behind you, the room lit on fire. Game over...")
            exit()
        elif game == "blue":
            print("You walked inside and closed the door behind you. it was dark, you lit your torch and went deeper inside and then got attacked by beasts. Game over...")
            exit()
        elif game == "green":
            print("You went inside and the door slammed closed behind you. It was cold inside and dark with no way out. You freeze to death. Game over...")
        elif game == "yellow":
            print("You found the room cover in gold! gold bars scattered everywhere! You found the long lost Treasure!!! You win!!!")
            exit()