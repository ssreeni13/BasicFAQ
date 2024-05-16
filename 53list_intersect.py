ls = [1, 2, 3, 4, 5]
ls1 = [3, 1, 6, 8, 7, 9]

# Approach1 - using set
set1 = set(ls)
set2 = set(ls1)
set3 = set1.intersection(set2)
print(set3)

# Approach2 - using loop
ls2 = list()
for i in ls:
    if i in ls1:
        ls2.append(i)
print(ls2)

# Approach3 - using list comprehension
ls3 = [x for x in ls if x in ls2]
print(ls3)
