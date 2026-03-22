"""Arrays this are data structures which contain data of the same datatype"""

numbers = [3, 4, 5, 6, 7, 8, 9, 2, 1, 0]
minVal = numbers[0]
maxVal = numbers[0]
for number in numbers:
    if number < minVal:
        minVal = number
    if number > maxVal:
        maxVal = number
print("Heighest number:", maxVal)
