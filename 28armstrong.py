# Approach1
num = input("Enter a number:")
# str1 = str(num)
length = len(num)
arm = sum(int(digits)**length for digits in num)
if arm == int(num):
    print(num, "is a Armstrong Number")
else:
    print(num, "is not a Armstrong Number")

# Approach2
# def is_arm(num):
#     str1 = str(num)
#     length = len(num)
#     arm = sum(int(digits) ** length for digits in num)
#     return arm == num
# print("Armstrong numbers in range of 500")
# for i in range(1,501):
#     if is_arm(i):
#         print(i)
