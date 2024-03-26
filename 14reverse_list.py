ls = [1,2,3,4,5,6,7,8]

# Approach1 - using reverse() method
print("list before reverse:", ls)
ls.reverse()
print("list after reverse:", ls)

# Approach2 - using slicing() method
print("list before reverse:", ls)
ls1 = ls[::-1]
print("list after reverse:", ls1)