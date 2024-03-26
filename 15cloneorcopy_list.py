ls = [1,2,3,4,5,6,7,8]

# Approach1 - using slicing() method
print("list before clone:", ls)
ls_copy = ls[:]
print("list after clone:", ls_copy)

# Approach2 - using extend() method
print("list before clone:", ls)
ls_copy = []
ls_copy.extend(ls)
print("list after clone:", ls_copy)

# Approach3 - using list() method
print("list before clone:", ls)
ls_copy = list(ls)
print("list after clone:", ls_copy)

# Approach4 - using copy() method
print("list before clone:", ls)
ls_copy = ls.copy()
print("list after clone:", ls_copy)

# Approach5 - using list comprehension
print("list before clone:", ls)
ls_copy = [i for i in ls]
print("list after clone:", ls_copy)
