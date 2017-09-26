
myList1 = [1,3,5,7,9]
myList2 = [2,4,6,8]
fullList = []
i=0
j=0
cnt=0
List1Len = len(myList1)
List2Len = len(myList2)
size = (List1Len + List2Len)-1
print(myList1)
print(myList2)
print("total numbers in both lists:", size+1)

while cnt < size:
    if myList1[i] < myList2[j]:
        fullList.append(myList1[i])
        i = i + 1

    elif myList1[i] > myList2[j]:
        fullList.append(myList2[j])
        j = j + 1

    cnt+=1

List1Len-=1
List2Len-=1

if myList1[List1Len] < myList2[List2Len]:
    fullList.append(myList2[List2Len])
elif myList1[List1Len] > myList2[List2Len]:
    fullList.append(myList1[List1Len])

print("Combined ordered list: ")
for l in fullList:
    print(l)