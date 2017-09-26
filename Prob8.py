
myList1 = [50,3,5,7,9]
myList2 = [51,4,6,8]
fullList = []

fullList = myList1 + myList2
fullList.sort()

print("Combined ordered list: ")
for l in fullList:
    print(l)