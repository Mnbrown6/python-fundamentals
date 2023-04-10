""" Lesson 11 - Encapsulation   """
""" Encapsulation is the concept of bundling data
and methods with one class, but Python has week
Encapsulation as it is not enforced.
"""


class MyClass:
    # protected
    __hi = 'Hello'

    def __init__(self):
        # private
        self.__value = 'World'


class Centimeter:
    """ Constructor method """
    def __init__(self, size: float):
        self._size = size

        """ Method to convert"""
    def to_millimeters(self) -> float:
        return self._size * 10

    """ Property Decorator for size"""
    @property
    def size(self) -> float:
       return self._size

    @size.setter
    def size(self, value):
        print('Setting size')
        self._size = value

class Feet:
    """ This class uses the property function style """
    def __init__(self, length):
        self._length = length

    # getter
    def get_length(self):
        return self._length

    # setter
    def set_length(self, value):
        self._length = value

    # delete
    def del_lenth(self):
        del self._length

    # creating property function
    length = property(get_length, set_length, del_lenth)

    # convert feet to inches
    def to_inches(self):
        return self.get_length() * 12

def example():
    measure = Feet(3)
    print(measure.length)
    print(measure.to_inches())
    measure.length = 32
    print(measure.to_inches())

    # delete
    def del_length(self):
        del self._length


def main():
    """ Starting point """
    # my_class = MyClass()
    # print(my_class._hi)
    #__value will cause an error
    # print(my_class.__value)
    my_measure = Centimeter(2)
    print(my_measure.size)
    print(my_measure.to_millimeters())
    my_measure.size = 4
    print(my_measure.to_millimeters())


if __name__ == '__main__':
   # main()
    example()
