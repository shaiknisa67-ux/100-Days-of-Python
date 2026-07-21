print("welcome to python pizza delivery:")
size=input("enter what size of pizza do you want? s or l or m?")
pepperoni=input("enter do you want pepperoni or not?y or n:")
cheese=input("enter do you want extra cheese or not?y or n:")
bill = 0
if size=="s":
    bill += 15
elif size=="m":
    bill += 20
elif size=="l":
    bill += 25
else:
    print("you typed wrong :")
if pepperoni=="y":
    if size=="s":
        bill += 2
    else:
        bill += 3
if cheese=="y":
    bill += 1
else:
    print("no extra cheese:")
print(f"your final bill is {bill}")