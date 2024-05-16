ls = [6, 4, 3, 8, 1, 2, 3, 4, 5]
for i in range(len(ls)):
    for j in range(len(ls)-1-i):
        if ls[j] > ls[j + 1]:
            ls[j], ls[j + 1] = ls[j+1], ls[j]

# ls.sort(reverse=True)
print(ls)

# ls = [6, 4, 3, 8, 1, 2, 3, 4, 5]
# for i in range(len(ls)):
#     for j in range(len(ls)-1-i):
#         if ls[j] < ls[j + 1]:
#             ls[j], ls[j + 1] = ls[j+1], ls[j]
#
# # ls.sort(reverse=True)
# print(ls)