import random
choices=["rock","paper","scissors"]
user=input("Enter your choice of rock,paper,scissors::")
computer=random.choice(choices)
print("computer chooses:",computer)
if user==computer:
    print("its a tie")
elif (user=="rock" and computer=="scissors") or\
     (user=="scissors" and computer=="paper") or\
     (user=="paper" and computer=="rock"):
    print("You Win")
else:
    print("Computer Wins")
