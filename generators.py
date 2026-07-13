def generate_numbers(n):
    for i in range(n):
        yield i
for num in generate_numbers(4):
    print(num)