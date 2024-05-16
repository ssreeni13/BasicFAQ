def deco(func):
    def wrapper(*args, **kwargs):
        print("-----------------------")
        print("Decorating Sum", func.__name__)
        print("-----------------------")
        return func
    return wrapper()

@deco
def sum1(a, b):
    print(a + b)

sum1(10, 20)
