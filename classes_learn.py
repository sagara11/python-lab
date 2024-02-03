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


class Person:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self._age = age  # Signaled as "private"

    def get_age(self):
        return self._age  # Method can access "private" attribute


person = Person("Alice", 30)
print(person.name)  # Accessible
print(person._age)  # Accessible, but convention suggests avoiding direct access
print(person.get_age())  # Recommended way to access "private" data

# Function defined outside the class


def f1(self, x, y):
    return min(x, x+y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


c = C()
print(c.f(10, 5))
print(c.g())
print(c.h())


class Base1:
    def method1(self):
        print("Base 1 method 1")


class Base2:
    def method2(self):
        print("Base 2 method 2")


class Derived(Base1, Base2):
    def my_method(self):
        super().method1()  # Calls method1 from Base1 as the first step
        # MRO can dynamically adjust for subsequent super() calls


instance = Derived()
# Output: Base 1 method 1
print(instance.my_method())


class Base1:
    def method1(self):
        print("Base 1 method 1")


class Base2:
    def method2(self):
        print("Base 2 method 2")


class MixedClass(Base1, Base2):
    def combined_method(self):
        super().method1()  # Calls Base 1 first
        # Since Base 2 doesn't override method1, calling super() wouldn't reach Base 2 here
        super().method2()  # Now calls Base 2


instance = MixedClass()
# Output: Base 1 method 1, Base 2 method 2
print(instance.combined_method())


class Animal:
    def make_sound(self):
        print("Generic animal sound")


class Mammal(Animal):
    def give_birth(self):
        print("Giving birth to live young")


class Bird(Animal):
    def fly(self):
        print("Flying")


class Bat(Mammal, Bird):
    def make_sound(self):
        print("Squeaking")


bat = Bat()
bat.make_sound()
print(Bat.__mro__)


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


a = MappingSubclass({"name": "tommas", "age": 20})
a.update("film", "peaky blinders")
print(a.items_list)


class MyClass:
    value = 10

    def change_value(self):
        exec("value = 20")  # Doesn't change the class attribute


instance = MyClass()
instance.change_value()
print(instance.value)  # Output: 10 (unchanged)
my_list = [1, 2, 3]

print(instance.change_value.__self__)
print(instance.change_value.__func__)


class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev = Reverse('spam')
print(iter(rev))
for char in rev:
    print(char)


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


print(reverse("gold").__dir__)

for char in reverse('golf'):
    print(char)
