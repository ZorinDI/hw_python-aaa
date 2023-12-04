# Task 1
from abc import abstractmethod, ABC


class ComputerColor(ABC):
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __rmul__(self, other):
        pass


class Color(ComputerColor):
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red: int, green: int, blue: int):
        self._red = self.checker(red)
        self._green = self.checker(green)
        self._blue = self.checker(blue)

    def __repr__(self):
        return f'{self.START};{self.red};{self.green};{self.blue}{self.MOD}●{self.END}{self.MOD}'

    @property
    def red(self):
        return self._red

    @property
    def green(self):
        return self._green

    @property
    def blue(self):
        return self._blue

    @red.setter
    def red(self, value):
        self._red = self.checker(value)

    @green.setter
    def green(self, value):
        self._green = self.checker(value)

    @blue.setter
    def blue(self, value):
        self._blue = self.checker(value)

    def checker(self, value):
        return max(0, min(255, value))

    def __eq__(self, other):
        if not isinstance(other, Color):
            raise ValueError('Разные типы(')
        return (self.red == other.red) and \
               (self.green == other.green) and (self.blue == other.blue)

    def __add__(self, other):
        new_color = Color(self.red + other.red, self.green + other.green, self.blue + other.blue)
        return new_color

    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    def __mul__(self, c):
        cl = -256 * (1 - c)
        f = 259 * (cl + 255) / (255 * (259 - cl))
        red = int(f * (self.red - 128) + 128)
        green = int(f * (self.green - 128) + 128)
        blue = int(f * (self.blue - 128) + 128)
        return Color(red, green, blue)

    def __rmul__(self, c):
        return self.__mul__(c)


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]
    for row in a_matrix: print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':
    red = Color(255, 0, 0)
    print(red)
    print_a(red)
