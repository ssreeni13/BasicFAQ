def rotate_array(arr, d):
    n = len(arr)
    d %= n
    arr[:] = arr[d:] + arr[:d]
    print(arr)


ls = [1, 2, 3, 4, 5]
tm = 2
rotate_array(ls, tm)
