def calc(v1,v2):
    c = input("Enter a operator(+,-,*,/):")
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        return a / b

a = int(input("Enter a 1st Number:"))
b = int(input("Enter a 2nd Number:"))
d = calc(a,b)
print(d)