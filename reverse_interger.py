def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed = int(str(x)[::-1])
    reversed = sign * reversed
    return reversed
