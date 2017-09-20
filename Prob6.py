# Smallest and largest in list
import random

numbers = [2,4,6,1,3,7,9,10,5,8]
smallest = 1
largest = 1
cnt = 0

while cnt <= 10:
    i = random.randint(1, 20)
    cnt+=1
    numbers.append(i)

for x in numbers:
    print(x)
    if smallest < x:
        smallest = x
    if largest > x:
        largest = x

print("The largest numer in the list is %s and the smallest is %s", largest, smallest)