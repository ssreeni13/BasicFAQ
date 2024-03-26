str = "welcome"
count = 0

# Approach1
print(len(str))

# Approach2
for i in range(0, len(str)):
    count += 1
print(count)

# Approach3
while str[count:]:
    count += 1
print(count)

# Approach4
rand_str = "X"
print(rand_str.join(str))
print(rand_str.join(str).count(rand_str))
print(rand_str.join(str).count(rand_str)+1)
