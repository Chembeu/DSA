def trasverse_arrays(number):
    m = len(number)
    n = len(number[0])

    for i in range(m):
        for j in range(n):
            print(number[i][j], end=" ")


arrays = [[1, 2, 3], [4, 6, 8], [7, 9, 6]]
trasverse_arrays(arrays)
