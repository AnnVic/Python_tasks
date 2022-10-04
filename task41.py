class Teacher:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.__salary = salary


person = Teacher('Alex', 50, 2000)
print(person.name)
