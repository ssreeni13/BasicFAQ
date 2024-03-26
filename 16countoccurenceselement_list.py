ls = [15, 6, 7, 10, 12, 20, 10, 28, 10]
n = 10
count = 0

# Approach1 - using loop
for i in ls:
    if n == i:
        count += 1
print("{} has occured {} times".format(n, count))

# Approach2- using count()
print("{} has occured {} times".format(n, ls.count(n)))

# Approach3 - using counter()
from collections import Counter
dic = Counter(ls)
print("{} has occured {} times".format(n, dic[n]))