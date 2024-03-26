ls = [2, 8, 3, 9, 7, 5]


# Approach1 - Simple Assign
print("Before Swap:", ls)
pos1, pos2 = 1, 3
ls[pos1], ls[pos2] = ls[pos2], ls[pos1]
print("After Swap:", ls)

# Approach2 - using pop()
print("Before Swap:", ls)
pos1, pos2 = 1, 3
a = ls.pop(pos1)
b = ls.pop(pos2-1)
ls.insert(pos1,b)
ls.insert(pos2,a)
print("After Swap:", ls)

# Approach3 - using tuple()
print("Before Swap:", ls)
get = (ls[1],ls[3])
ls[3],ls[1] = get
print("After Swap:", ls)

