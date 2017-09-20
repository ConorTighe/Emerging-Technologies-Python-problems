# Smallest and largest in list
import random

numbers = []
smallest = 0
largest = 0
cnt = 0
listSize = 100

#Create random list
while cnt < 10:
    i = random.randint(1, listSize)
    cnt+=1
    numbers.append(i)

# Function for finding largest and smallest
def LargestAndSmallest (nums, size):
    s = size + 1
    l = 0

    for x in nums:
        print(x)
        if s > x:
            s = x
        if l < x:
            l = x
    return l,s

largest, smallest = LargestAndSmallest(numbers, listSize)

print("The largest number in the list is %s " % largest)
print("The smallest number in the list is %s " % smallest)
