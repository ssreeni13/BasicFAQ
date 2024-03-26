ls = [1, 2, 3, 4, 5]
temp = 0

for i in range(0, len(ls)):
    temp += ls[i]
print(temp)

print(sum(ls))
print(sum(ls, - 10))
print(sum(ls, 10))
