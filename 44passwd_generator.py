import random

lower = "abcdefghijklmnopqrstuvwxyz"   ''.join(random.sample(all_chars,length))
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+=?><{["

all_chars = lower + upper + numbers + symbols
length = int(input("Enter a length: "))

result = ''.join(random.sample(all_chars, length))
print("Generated Password", result)