print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input(print("you are at a cross road , where do you want to go?" \
" type 'left' or 'right'.")).lower()
if choice1 == "left":
        choice2=input(print("you can continue the game. now you have come to a lake." \
        "there is an island in the middle of the lake." \
        "Type 'wait' to wait for a boat.Type 'swim' to swim across")).lower()
        if choice2 =="wait":
                choice3=input(print("you arrive at the island unharmed" \
                "there is a house with 3 doors.one red," \
                "one rellow,one blue" \
                "which colour you choose?")).lower()
                if choice3 == "red":
                    print("its room full of fire.Game over")
                elif choice3 == "yellow":
                    print("you found the treasure.You Win")
                elif choice3 == "blue":
                    print("you enter a room of beasts.Game over")
                else:
                    print("you choose the door that doesnot exist")
        else:
                print("you got attacked by angry trout.Game Over")
else:
    print("you fell into a hole,so Game over.")