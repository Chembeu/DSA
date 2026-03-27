def trasverse_arrays(number):
    m = len(number)
    n = len(number[0])
    flat = []

    for i in range(m):
        for j in range(n):
            flat.append(number[i][j])
    reverse_array = flat[::-1]
    print(reverse_array)


def transverse(number):
    new_array = []
    for i in range(len(number) - 1):
        new_array.append(number[i])
    print(new_array)


value = [1, 2, 3, 4, 5]
arrays = [[1, 2, 3], [4, 6, 8], [7, 9, 6]]
trasverse_arrays(arrays)
transverse(value)
