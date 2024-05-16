ls = [2,8,3,9,7,3]

# Approach1 - using sort() method
# ls.sort()
# print("Min no in list:", ls[0])
# print("Max no in list:", ls[-1])

# Approach2 - using loop
temp = ls[0]
for i in range(0, len(ls)):
    if temp <= ls[i]:
        temp = ls[i]
print("Max", temp)


# Approach3 - min & max
print(min(ls))
print(max(ls))