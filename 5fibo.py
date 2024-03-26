n1 = 0
n2 = 1
num = 5

print(n1)
print(n2)

for i in range(2,num+1):
    temp = n1 + n2
    print(temp)
    n1 = n2
    n2 = temp

