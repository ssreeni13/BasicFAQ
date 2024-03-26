# Approach1
num = int(input("Enter a number:"))
str1 = str(num)
length = len(str1)
arm = sum(int(digits)**length for digits in str1)
if arm == num:
    print(num, "is a Armstrong Number")
else:
    print(num, "is not a Armstrong Number")

# Approach2
def is_arm(num):
    str1 = str(num)
    length = len(str1)
    arm = sum(int(digits) ** length for digits in str1)
    return arm == num
print("Armstrong numbers in range of 500")
for i in range(1,501):
    if is_arm(i):
        print(i)
