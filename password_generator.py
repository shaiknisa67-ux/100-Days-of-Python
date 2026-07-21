import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')']
print("welcome to the pypassword generator:")
L=int(input("how many letters do you like in your password:"))
N=int(input("how many numbers you like in your password:"))
S=int(input("enter how many symbols you like in your password:"))
password=""
for char in range(1,L + 1):
    password += random.choice(letters)
for char in range(1,N + 1):
    password += random.choice(symbols)
for char in range(1,S + 1):
    password += random.choice(numbers)
print(password)