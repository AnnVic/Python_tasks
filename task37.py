class Students:
    def __init__(self, name: str, age: int, grade: int):
        self.name = name
        self.age = age
        self.grade = grade


person = Students('Alex', 18, 12)
print(person.name)
