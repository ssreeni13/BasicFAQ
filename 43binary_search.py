a = [5, 7, 19, 26, 34, 39, 149, 152]


def binary(arr, key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            right = mid - 1
        else:
            left = mid + 1

    return -1

result = binary(a, 152)

if result == -1:
    print("Key not Found")
else:
    print(f"Found at {result}")

