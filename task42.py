class Country:
    def __init__(self, name: str, language: str, population: int):
        self.name = name
        self.language = language
        self.population = population

    def __add__(self, other):
        return self.population + other.population

    def __gt__(self, other):
        return self.population > other.population


usa = Country('USA', 'english', 8500000)
greece = Country('Greece', 'greek', 3000000)
print(usa + greece)
print(greece > usa)
