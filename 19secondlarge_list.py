ls = [2,8,3,9,7,3]

# Approach1 - using sort() method
ls.sort()
print("Largest no in list:", ls[-1])
print("2nd Largest in list:", ls[-2])

# Approach2 - using remove
ls_cpy = set(ls)
ls_cpy.remove(max(ls))
print(ls_cpy)
print(max(ls_cpy))

# Approach3 - using loop
for i in range(len(ls)):
    for j in range(len(ls)-1-i):
        if ls[j] > ls[j+1]:
            ls[j], ls[j+1] = ls[j+1], ls[j]
# print(ls)
print(f"{ls[-2]} is the second largest number")