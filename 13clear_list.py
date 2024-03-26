ls = [2, 8, 3, 9, 7, 5]

# Approach1 - using clear() method
print("list before clear:", ls)
ls.clear()
print("list after clear:", ls)

# Approach2 - Initialize list with no value
print("list before clear:", ls)
ls = []
print("list after clear:", ls)

# Approach3 - using "*=" method
print("list before clear:", ls)
ls *= 0
print("list after clear:", ls)

# Approach4 - using del method
print("list before clear:", ls)
del ls[:]
print("list after clear:", ls)

