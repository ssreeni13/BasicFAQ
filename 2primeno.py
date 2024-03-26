n = int(input("Enter the Number:"))
count = 0
if n > 1:
    for i in range(1,n+1):
        if n % i == 0:
            count += 1

    if count == 2:
        print(n, "is a Prime Number")
    else:
        print(n, "is not a Prime Number")