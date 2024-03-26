n = int(input("Enter a number:"))
for i in range(1,100):
    if n % i == 0:
        print(n,"is divisible by ",i)