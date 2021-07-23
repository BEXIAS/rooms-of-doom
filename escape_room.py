import time
def main_room():
    welcome = open("welcome.txt", "r")
    print(welcome.read())
    welcome.close()
    print("WELCOME TO THE ROOMS OF DOOM")
    print("\nYou are currently in room 1, there are 6 rooms in total. Each room has 2 doors,")
    print("\nTo win, you must choose the correct door in each room. Choosing the wrong room may result in death.")
    print("\nChoose your first door...")
    print("\nDoor 1: The Bear Room")
    print("\nDoor 2: The Monster Room")
    cont = True
    while cont == True:
        choice1 = input("enter your choice. Enter 1 or 2:")
        if choice1 == "1":
            bear_room()
            cont = False
        elif choice1 == "2":
            monster_room()
            cont = False
        else:
            print("Invalid Input! ")
def bear_room():
    print("\nThe bear is starving, it charges straight for you.")
    print("You died")
    bear = open("bear.txt", "r")
    print(bear.read())
    bear.close()
    reason = " a hungry bear"
    game_over(reason)
# room 2
def monster_room():
    print("\nYou enter the monster room, there is a large sleeping monster lying across the room.")
    monster = open("monster.txt", "r")
    print(monster.read())
    monster.close()
    time.sleep(3)
    print("\n The monster seems to be in a very deep sleep so you slowly walk across the room towards the next two selections of doors. ")
    time.sleep(2)
    print("\nDoor 1: The Gold Room")
    print("\nDoor 2: The Silver Room")
    cont = True
    while cont == True:
        choice2 = input("enter your choice. Enter 1 or 2")
        if choice2 == "1":
            gold_room()
            cont = False
        elif choice2 == "2":
            silver_room()
            cont = False
        else:
            print("Invalid Input!")
def silver_room():
    print("\nThis room does not have silver valuables....")
    print("you're suspecting something and walk around the stone pillar holding the roof")
    time.sleep(2)
    print("you see a shiny humanoid figure appear in the distance... it seems to be holding a knife")
    print("suddenly it turns around revealing a bloody smile and charges for you with a silver knife")
    reason = "Silver Assassin"
    game_over(reason)



# room 3
def gold_room():
    print("\nNice! You've discovered a room full of raw gold")
    print("Be sure you take some with you. It may become useful later.")
    print("\nYou move on to the next two doors")
    print("\nDoor 1: The Mahogany Room")
    print("\nDoor 2: The Oak Room")
    print("")
    choice3 = input("now choose your next room")
    cont = True
    while cont == True:
        choice3 = input("enter your choice. Enter 1 or 2")
        if choice3 == "1":
            mahogany_room()
            cont = False
        elif choice3 == "2":
            oak_room()
            cont = False
        else:
            print("invalid input!")
def mahogany_room():
    print("You step into the mahogany room and see multiple logs stacked up apon each other on the side")
    print("wondering what they are there for you step closer.")
    print("suddenly multiple logs start rolling towards you")
    reason = "rolled over by logs"
    game_over(reason)

# room 4
def oak_room():
    print("\nThis room is full of beautiful and fresh oak boards")
    print("Take one with you it might become useful later")
    print("\n You walk around the large oak tree to the next two doors ahead")
    print("\nDoor 1: The Diamond Room")
    print("\nDoor 2: The Crystal Room")
    cont = True
    while cont == True:
        choice4 = input("enter your choice. Enter 1 or 2")
        if choice4 == "1":
            diamond_room()
            cont = False
        elif choice4 == "2":
            crystal_room()
            cont = False
        else:
            print("Invalid Input!")
def diamond_room():
    print("\ncongradulations, you've found a giant diamond!")
    print("It is one of the biggest, most shiny and brilliant diamonds you've ever seen!")
    print("Well done for making it this far, just one more room to go")
    time.sleep(2)
    print("\nchoose carefully or all your progress will be lost")
    print("\nDoor 1: Wizard's Room")
    print("Door 2: Magician's Room")
    cont5 = True
    while cont5 == True:
        choice5 = input("enter your choice. Enter 1 or 2")
        if choice5 == "1":
            wizard_room()
            cont5 = False
        elif choice5 == "2":
            magician_room()
            cont5 = False
        else:
            print("Invalid Input!")
def crystal_room():
    print("you step into the crystal room, only to trip on a super thin wire and fall into the deep hole ahead")
    print("You land inside a dark cave lighten up by lots of glowing crystals.")
    print("they seem to be calling out to you to touch them")
    print("You see no harm in touching the crystal and slowly reach towards it")
    print("your heart stops beating and you immediately fall dead")
    reason = "a dark force"
    game_over(reason)
def magician_room():
    print("\n The magician is amazed by your precious items you have collected")
    print("He offers to use his magic to make them into a beautiful trophy")
    print("All you have to do is type the following magic word:")
    print("\nABRACADABRA")
    print("")
    magic = input("enter the magic word here")

    if magic.upper() == "ABRACADABRA":
        win()
    else:
        reason = "wrong word! the magician casted a dark spell!"
        game_over(reason)
def play_again():
    satisfied = int(input("Do you want to play again? Option 1: Yes Option 2: No"))
    if satisfied == 1:
        main_room()
    elif satisfied == 2:
        print("See you next time!Thank you for playing")
def wizard_room():
    print("You step into the wizard room")
    print("the wizard looks at you and tells you to come inside his small hut")
    print("Once inside he gives you a cup of tea and a seat at the table to rest")
    print("After talking to the wizard you decide its time to head on to the next door and finish your adventure")
    print("You say goodbye and head over to the door of the hut")
    print("The door does not budge")
    print("You turn around only to see a giant ball of fire shot from the very hands of the wizard")
    reason = "a fireball"
    game_over(reason)
def game_over(reason):
    print("\nGAME OVER!")
    print(f"you have been killed by {reason}")
    play_again()
def win():
    print("You enter the last room and see the sun shining above")
    print("A entity resembling an eye floats towards you")
    print("EYE: Congradulations of finishing the rooms of doom. Your rewards are up ahead. Well done adventurer")
    trophy = open("trophy.txt", "r")
    print(trophy.read())
    trophy.close()
    play_again()

main_room()
