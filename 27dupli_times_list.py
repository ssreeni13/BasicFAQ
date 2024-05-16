a = [2,3,2,4,5,6,2,5,3,2]
# dup = a[0]

for i in a:
    if a.count(i) > 1:
        print("Duplicate element=",i,"Repeated times=",a.count(i))

# Remove duplicate elements
# ls = [1,9,7,8,8,3,3,6,5]
# ls1 = []
#
# for i in ls:
#     if i not in ls1:
#         ls1.append(i)
#
# print(ls1)