str1 = input("Enter 1st String:")
str2 = input("Enter 2nd String:")
if sorted(str1) == sorted(str2):
    print("Strings are Anagram")
else:
    print("Strings are not Anagram")