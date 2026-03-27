def trasverse_arrays(number):
    m = len(number)
    n = len(number[0])
    flat = []

    for i in range(m):
        for j in range(n):
            flat.append(number[i][j])
    reverse_array = flat[::-1]
    print(reverse_array)


arrays = [[1, 2, 3], [4, 6, 8], [7, 9, 6]]
trasverse_arrays(arrays)
