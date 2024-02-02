class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self) -> None:
        self.y = 100
        print("Initiated")

    def f(self):
        return 'hello world'


def test_class():
    print("Additional method")


a = MyClass()
a.new_function = test_class


class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)
