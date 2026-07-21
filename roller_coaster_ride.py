print("welcome to the roller coaster ride:")
height=int(input("enter your height in cm?"))
bill = 0
if height >= 120:
    print("you can ride:")
    age=int(input("enter your age:"))
    if age <= 12 :
        bill = 5
        print("child tickets are 5$")
    elif age <= 18 :
        bill = 7
        print("youth tickets are $7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("free ride for these")
    else:
        bill = 12
        print("adult tickets are $12")
    photos = input("do you want to take any photos?")
    if photos == "y":
        bill += 3
    print(f"your final bill is{bill}")
else:
    print("sorry you cannot ride:")
    print(f"your final bill is{bill}")