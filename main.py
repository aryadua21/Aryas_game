import random
import time
import sys


print("You spawn in a room, without knowing why you are there. All you know is that you are craving some ice cream" \
"You see an ice cream machine in front of you. You also see two doors, one to the left and one to the right.")
print("You really want some ice cream so you make it your mission to find some.")

print("Where would you like to go?")
game = True

coin1 = False
coin2 = False

def gameRunning():
    global coin1
    global coin2
    while game == True:
        
        answer = input("Type 1 to go to the ice cream machine, 2 to go to the left room, and 3 to go to the right room: ")
        time.sleep(0.5)
        match (answer):
            case "1":
                print("You walk to the ice cream machine. It asks for two nickels")
                if coin1 == True and coin2 == True:
                    time.sleep(0.5)
                    print("You have enough money.")
                    if input("Do you buy the ice cream (y/n): ") == "y":
                        time.sleep(0.5)
                        print("Hooray you got the ice cream!")
                        sys.exit(0)
                    else:
                        time.sleep(0.5)
                else:
                    time.sleep(0.5)
                    print("You don't have enough money to buy the ice cream. Visit the other rooms to perhaps gain some.")
                    time.sleep(0.5)
                    gameRunning()
            case "2":
                if coin1 == True:
                    print("You already have this coin.")
                    time.sleep(1)
                    gameRunning()
                print("You enter the left room. There, there is a shiny nickel on a tall platform. To bring the platform down, you have to roll a multiple of 4 on a 20 sided dice, and insert it into the machine.")
                time.sleep(0.5)
                while True:
                    leftDoorAnswer = input("Press enter to roll the dice or q to leave the room: ")
                    if leftDoorAnswer == "":
                        print("Rolling the dice...")
                        time.sleep(0.5)
                        dice = random.randint(1,20)
                        print("You rolled a " + str(dice))
                        if dice % 4 == 0:
                            print("Hooray you acquired the nickel.")
                            coin1 = True
                            break
                        else:
                            print("Unfortunately you did not get the nickel.")
                    elif leftDoorAnswer == "q":
                        gameRunning()
                    else:
                        print("press one of the suggested keys please.")
                    

            case "3":
                if coin2 == True:
                    print("You already have this coin.")
                    time.sleep(1)
                    gameRunning()
                print("You see 4 boxes which you don't know the contents off. You can choose to search the boxes or leave the room")
                correctBox = str(random.randint(1,4))
                while True:
                    rightRoomAnswer = input("Type 1-4 to search the boxes or type q to leave the room: ")
                    if rightRoomAnswer == "q":
                        gameRunning()
                    elif rightRoomAnswer != correctBox:
                        print("Searching...")
                        time.sleep(0.5)
                        print("Sorry, there was nothing inside")
                    elif rightRoomAnswer == correctBox:
                        print("Searching...")
                        time.sleep(0.5)
                        print("Hooray, you found a nickel inside!")
                        coin2 = True
                        break
                    else:
                        print("please choose one of the options.")

            case _:
                print("please choose one of the options")



gameRunning()
