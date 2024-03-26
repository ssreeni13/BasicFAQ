ls = [2, 8, 3, 9, 7, 5]

# Approach1 - using loop

ele = 2
flag = False
for i in ls:
    if i == ele:
        print("Element Exists")
        flag = True
        break
if not flag:
        print("Element not Exists")

# Approach2 - using operator
if ele in ls:
    print("Element Exists")
else:
    print("Element not Exists")

