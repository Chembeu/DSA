def repeat(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            func(*args, **kwargs)
    return wrapper


@repeat
def say():
    print("Hello")

say()