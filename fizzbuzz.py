a=[10,20,30,40,50,60]                       
b=sum(a)
sum=0
for c in a:
    sum += c
print(sum)
print(max(a))
maxscore=0
for c in a:
    if c > maxscore:
        maxscore = c
print(maxscore)
for i in range(1,101):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)