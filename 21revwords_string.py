str = "welcome to python programming"
words = str.split(" ")
words = words[::-1]
words2 = " ".join(words)
print(words2)
#
words1 = ""
for i in range(0,len(words2)):
    words1 += words2[i]
print(words1)

words4 = ""
for i in range(len(str)-1,-1,-1):
    words4 += str[i]
print(words1)
# words1 = str.split(" ")
# print(words1)
# words2 = " ".join(words1)
# print(words2)

