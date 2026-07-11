def main_function(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        func(*args, **kwargs)
        print("After the function call")
    return wrapper
@main_function
def child_function(x, y):
    print(f"Inside the child function with arguments: {x}, {y}")
    return x + y
child_function(6,8)