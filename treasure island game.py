print("WELCOME TO TREASURE ISLAND")
print("Your mission is to find the treasure")
print('''*******************************************************************************
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
*******************************************************************************

''')
c= input("Do you want to go right or left?\n")
if c=="left" :
  c1=input("There is a lake\n Do you want to wait for a boat or swim?(wait/swim)\n")
  if c1=="wait":
    c2= input("There are three doors yellow, red, blue.\n Which door do you want to go through?\n")
    if c2 =="red":
      print("There are monsters.You die!")
    elif c2 =="blue":
      print("The room is full of fire.You          loose!")
    elif c2 =="yellow":
      print("You chose the right door, you found the treasure.You win!")
    else:
      print("The door you chose does not exist")
  
  elif c1=="swim":
    print("You chose to swim, you were eaten by a shark. Game Over.")
  else:
    print("incorrect choice")

else:
  print("You came out of the island. Game Over.")
  
  
  

