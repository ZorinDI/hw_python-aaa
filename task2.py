from datetime import datetime
import sys


def my_write(string_text):
    if string_text != '\n':
        time = f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]: '
        original_write(f'{time}{string_text}')
    else:
        original_write(f'{string_text}')


original_write = sys.stdout.write


def timed_output(function):
    def wrapper(name):
        sys.stdout.write = my_write
        function(name)
        sys.stdout.write = original_write

    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


print_greeting("Nikita")
