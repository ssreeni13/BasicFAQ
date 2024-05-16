a = [5, 7, 19, 6, 24, 32, 159, 45]


def search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


result = search(a, 45)

if result == -1:
    print("Key not Found")
else:
    print(f"Found at {result}")
