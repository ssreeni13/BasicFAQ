def perf_square(x):
    s = int(x ** 0.5)
    return s * s == x


def check_fibonacci(n):
    return perf_square(5 * n * n + 4) or perf_square(5 * n * n - 4)


num = int(input("Enter a number:"))

if check_fibonacci(num):
    print(f"{num} is a Fibonacci Number")
else:
    print(f"{num} is not a Fibonacci Number")
