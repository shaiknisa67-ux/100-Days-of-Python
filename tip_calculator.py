print("Welcome to the tip calculator")
a=float(input("what was the total bill?"))
b=int(input("how much tip would you like to give?10,12 or 15?"))
c=int(input("how many people to split the bill?"))
d=b/100
e=a*d
f=a+e
print(f"each person should pay:{f}")