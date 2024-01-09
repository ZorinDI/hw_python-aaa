from datetime import datetime
from os import system
import sys


def redirect_output(filepath):
    def decorator(func):
        def wrapper(*args):
            with open(filepath, 'w') as file_name:
                original = sys.stdout
                sys.stdout = file_name
                func(*args)
                sys.stdout = original

        return wrapper

    return decorator


@redirect_output('./function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == "__main__":
    calculate()
    system("function_output.txt")
