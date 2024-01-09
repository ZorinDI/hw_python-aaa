from datetime import datetime
import sys

original_write = sys.stdout.write


def my_write(string_text):
    if string_text != '\n':
        time = f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]: '
        original_write(f'{time}{string_text}')
    else:
        original_write(f'{string_text}')


sys.stdout.write = my_write

print('1, 2')

sys.stdout.write = original_write
