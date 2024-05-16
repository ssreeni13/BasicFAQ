s = "abcabcdbb"
max_length = 0
start = 0
end = 0
n = len(s)
char_set = set()
while end < n:
    if s[end] not in char_set:
        char_set.add(s[end])
        end += 1
        max_length = max(max_length, end - start)
    else:
        char_set.remove(s[start])
        start += 1
print(max_length)
