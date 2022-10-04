class Picture:
    def __init__(self, height: int, width: int, color: str):
        self.height = height
        self.width = width
        self.color = color


picture = Picture(50, 30, 'red')
print(picture.__dict__)
