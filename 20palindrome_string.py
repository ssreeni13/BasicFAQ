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

