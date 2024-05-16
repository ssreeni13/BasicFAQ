print("\nNormal Pyramid")
for i in range(5):
    x = '* '
    x = x * i
    print(f'{x:^10}')

print("\nInverted Pyramid")
for i in range(5):
    x = '* '
    x = x * (5-i)
    print(f'{x:^10}')

print("\nLeft side Pyramid")
for i in range(5):
    x = '* '
    x = x * i
    print(f'{x:<10}')

print("\nRight side  Pyramid")
for i in range(5):
    x = '* '
    x = x * i
    print(f'{x:>10}')
