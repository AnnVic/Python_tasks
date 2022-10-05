class Apartment:
    def __init__(self, adress: str, price: int, area: float):
        self.adress = adress
        self.price = price
        self.__area = area

    @property
    def area(self) -> int:
        return self.__area

    @area.setter
    def area(self, area) -> None:
        self.__area = area

    @area.deleter
    def area(self) -> None:
        del self.__area


one = Apartment('Balti', 20000, 53.5)
one.area = 40
print(one.area)
