from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def say(self):
        pass

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def attak(self):
        pass


class Cat(Animal):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say(self):
        print('Meow')

    def info(self):
        print(f'Hi! I am {self.name}')

    def attak(self):
        print(f'{self.name} will release its claws.')


class Dog(Animal):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say(self):
        print('Rrrr')

    def info(self):
        print(f'Hi! I am {self.name}')

    def attak(self):
        print(f'{self.name} will bite.')


animals = [Cat('alice', 2), Dog('holli', 7)]

for animal in animals:
    animal.say(), animal.info(), animal.attak()
