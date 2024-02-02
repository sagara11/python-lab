import sys
from my_labs import fib
from my_labs import fib2
# Path to a directory containing multiple modules
# module_dir = "/home/thong/python_lab/my_labs"
# sys.path.append(module_dir)
# from my_labs import *

# Now you can import any module within that directory
# import lab_1
# import lab_2

fib(10)
print(fib2(100))


class B(Exception):
    x = 10


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except D:
        print("D")
    except C:
        print("C")

# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))    # the exception type
#     print(inst.args)     # arguments stored in .args
#     print(inst)          # __str__ allows args to be printed directly,
#     # but may be overridden in exception subclasses
#     x, y = inst.args     # unpack args
#     print('x =', x)
#     print('y =', y)


# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise

# def my_function(data="hello"):
#     x = 10  # Local variable in the function's namespace

#     def inner_function():
#         x = 20  # Local variable in inner_function's namespace
#         print(x)  # Output: 20

#     inner_function()

#     # y is not accessible here because it's in inner_function's namespace
#     print(x)  # Output: 10


# my_function()

# print(dir(my_function.__dict__))


# Module namespace (global scope outside functions)
x = 10


def my_function():
    # Function's local namespace
    y = 20

    class MyClass:
        # Class namespace
        z = 30

        def my_method(self):
            # Method's local scope (accesses class namespace)
            print(self.z)  # Accesses z from the class namespace

    my_class = MyClass()
    print(my_class.my_method())


my_function()  # Creates temporary function and class namespaces


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
