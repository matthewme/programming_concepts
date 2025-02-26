# Base Class
class Parent:
    # Class attribute. Affects base class and Inheritance classes.
    speaks = ["English"]

    def __init__(self, name: str, age: int):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound: str):
        return f"{self.name} says {sound}"


class Child(Parent):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

        # Instance method

    def description(self):
        return f"{self.name} is {self.age} years of age."
