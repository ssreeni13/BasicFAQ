myList = [3,5,7]
ls2 = list()
myList.append(1)
# myList.reverse()
for i in range(len(myList)-1,-1,-1):
    ls2.append(myList[i])
print(ls2)

myList = [1,4,7]
new_elements = [2,3]
myList.insert(1,new_elements)
print(myList)

