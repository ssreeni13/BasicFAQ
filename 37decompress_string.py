import string

# s = "a3b2c4"
# result = ""
# for i in range(0, len(s), 2):
#     char = s[i]
#     count = int(s[i + 1])
#     result += char * count
# print(result)

s1 = "aaabbcccc"
res = ""
count = 1
for i in range(len(s1)):
        if i < len(s1) - 1 and s1[i] == s1[i+1]:
            count += 1
        else:
            char = s1[i]
            res += char + str(count)
            count = 1
print(res)
