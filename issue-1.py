import json
import keyword


def json_parser(json_object):
    return json.loads(json_object)


class Advert:
    def __init__(self, json_object: dict, flag=0):
        if self.flag == 0 and 'title' not in json_object.items():
            raise ValueError('Нет названия объявления', self.flag)
        self._price = 0
        for key, value in json_object.items():
            if keyword.iskeyword(key):
                key += '_'
            if isinstance(value, dict):
                value = Advert(value, flag=1)
                self.__setattr__(key, value)
            else:
                self.__setattr__(key, value)

    def __getattr__(self, item):
        return self.__dict__.get(item)

    def __setattr__(self, key, value):
        if key != 'price':
            self.__dict__[key] = value
        else:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError('Цена должна быть числом')
            if value < 0:
                raise ValueError('Цена должна быть неотрицательной')
            self._price = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: int) -> None:
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError('Цена должна быть числом')
        if value < 0:
            raise ValueError('Цена должна быть неотрицательной')
        self._price = value


if __name__ == "__main__":
    dog_str = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs",
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
        }
    }"""
    dog = json_parser(dog_str)
    dog_ad = Advert(dog)
    print(dog_ad.price)
    print(dog_ad.class_)
    print(dog_ad.location.address)
    dog_ad.price = -1
