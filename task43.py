class Staff:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Teacher(Staff):
    def __init__(self, subject: str):
        self.subject = subject
        super().__init__('Alex', 40)


print(f'Is Teacher a subclass: {issubclass(Teacher, Staff)}')
