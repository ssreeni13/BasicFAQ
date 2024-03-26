ls = [2,8,3,9,7,5]


# Approach1 - Temp
print("Before Swap:", ls)
size = len(ls)
temp = ls[0]
ls[0] = ls[size-1]
ls[size-1] = temp

print("After Swap:", ls)

# Approach2 - Simple Assign
print("Before Swap:", ls)
ls[0],ls[size-1] = ls[size-1],ls[0]
print("After Swap:", ls)

# Approach3 - using tuple
print("Before Swap:", ls)
get=(ls[0],ls[size-1])
ls[size-1],ls[0] = get
print("After Swap:", ls)

# Approach4 - * operand
print("Before Swap:", ls)
start,*middle,end = ls
ls = [end,*middle,start]
print("After Swap:", ls)

# Approach5 - using pop()
print("Before Swap:", ls)
a = ls.pop(0)
b = ls.pop(-1)
ls.append(a)
ls.insert(0,b)
print("After Swap:", ls)
