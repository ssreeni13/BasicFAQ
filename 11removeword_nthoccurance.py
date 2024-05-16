ls = ["geeks", "for", "geeks", "geeks", "geeks"]
word = "geeks"
n = 3
count = 0

for i in range(0,len(ls)-1):
    if ls[i] == word:
        count += 1
        if count == n:
            del ls[i]
print(ls)