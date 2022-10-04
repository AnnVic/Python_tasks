class Picture:
    def __init__(self, height: int, width: int, color: str):
        self.height = height
        self.width = width
        self.color = color


picture = Picture(25, 10, 'black')
print(picture.__class__.__name__)
