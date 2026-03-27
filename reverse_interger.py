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


def reverrse_array(arrays):
    reversed = arrays[::-1]
    return reversed


print(reverrse_array([1, 2, 3, 4, 5]))
