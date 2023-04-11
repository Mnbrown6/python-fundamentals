""" Horses """
""" 3 common attributes"""

""" Task 1 """

class Horse:
    def __init__(self, breed: str, coat_color: str, mane_color: str):
        self._breed = breed
        self._coat_color = coat_color
        self._mane_color = mane_color

    @property
    def horse_type(self) -> str:
        return self._breed

    @horse_type.setter
    def horse_type(self, breed: str):
        self._breed = breed

    @property
    def coat_color(self) -> str:
        return self._coat_color

    @coat_color.setter
    def coat_color(self, coat_color: str):
        self._coat_color = coat_color

    @property
    def mane_color(self) -> str:
        return self._mane_color

    @mane_color.setter
    def mane_color(self, mane_color: str):
        self._mane_color = mane_color

""" Task 2 """

def main():
    horse_1 = Horse('Arabian', 'brown', 'dark brown')
    print(horse_1.horse_type)
    print(horse_1.coat_color)
    print(horse_1.mane_color)


if __name__ == '__main__':
    main()