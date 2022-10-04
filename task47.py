class Square:
    def __init__(self, lenght: int):
        self.lenght = lenght

    def get_perimetr(self):
        return self.lenght ** 2

    def get_square(self):
        return self.lenght * 4


one = Square(20)
print(f'Square area: {one.get_square()}')
print(f'Perimetr: {one.get_perimetr()}')
