s = input("Enter a string:")
s1 = ""
# Approach1 - using reverse() method
# revstr = s[::-1]
#
# if revstr == s:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# Approach2 - using for loop method
for char in range(len(s)-1,-1,-1):
    s1 += s[char]
if s1 == s:
    print("Palindrome")
else:
    print("Not Palindrome")


# n = "race car"
# n2 = n.split()
# n3 = "".join(n2)
# n1 = ""
# for i in range(len(n3)-1,-1,-1):
#     n1 += n3[i]
# if n3 == n1:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
# # print(n1)
# print(n3)
