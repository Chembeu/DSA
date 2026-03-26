def reverse(x: int) -> int:
    INT_MIN = -(2**31)
    INT_MAX = 2**31 - 1

    reversed_num = 0

    while x != 0:
        # Extract last digit
        digit = x % 10

        # Fix Python behavior for negative numbers
        if x < 0 and digit > 0:
            digit -= 10

        # Remove last digit from x
        x = (x - digit) // 10

        # 🔥 Check overflow BEFORE updating reversed_num
        if reversed_num > INT_MAX // 10 or (
            reversed_num == INT_MAX // 10 and digit > 7
        ):
            return 0

        if reversed_num < INT_MIN // 10 or (
            reversed_num == INT_MIN // 10 and digit < -8
        ):
            return 0

        # Build reversed number
        reversed_num = reversed_num * 10 + digit

    return reversed_num
