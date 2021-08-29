def type_logger(func):
    def wrapper(*args):
        for num in args:
            print(f'{func.__name__}({num}: {type(num)})')
    return wrapper

@type_logger
def calc_cube(x):
    return x ** 3

a = calc_cube(2, 3.4, 55, 7.1)