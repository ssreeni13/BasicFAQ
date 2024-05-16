str1 = "sreeni"
vow = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
count = 0
for i in str1:
    if i in vow:
        count += 1
        print(i)
print(count)
