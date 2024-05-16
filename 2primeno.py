# n = int(input("Enter the Number:"))
# count = 0
# if n > 1:
#     for i in range(2, int(n*0.5) + 1):
#         if n % i == 0:
#             count += 1
#
#     if count == 1:
#         print(n, "is a Prime Number")
#     else:
#         print(n, "is not a Prime Number")

def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def add_prime(a):
    ls = []
    for num in range(2, a + 1):
        if prime(num):
            ls.append(num)
    return ls

a = int(input("Enter a number:"))
pri = add_prime(a)
print(pri)