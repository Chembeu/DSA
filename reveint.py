def reverse(x):
    reverse_num = 0
    while x != 0:
        digit = x % 10
        x = (x - digit) // 10
        reverse_num = reverse_num * 10 + digit
    return reverse_num


print(reverse(144))
