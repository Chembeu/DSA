numbers = [[2, 4, 5], [3, 5, 6], [1, 5, 7]]
m = len(numbers)
n = len(numbers[0])
total_sum = 0
for i in range(m):
    for j in range(n):
        total_sum += numbers[i][j]
print(total_sum)
