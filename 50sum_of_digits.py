sod = input("Enter a number:")
sum1 = 0
sum2 = 0
for i in sod:
    sum1 += int(i)
# print(sum)

if sum1 > 9:
    sum1 = str(sum1)
    for i in sum1:
        sum2 += int(i)
print(sum2)