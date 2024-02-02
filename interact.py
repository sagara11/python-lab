import sys

from exceptiongroup import ExceptionGroup


for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


def this_fails():
    x = 1/0


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:  # Original exception
        if b == 0:
            raise ValueError("Division by zero")  # New exception
        else:
            raise  # Re-raise the original exception


try:
    divide(10, 0)
except ValueError as e:
    print(e)  # Output: ValueError: Division by zero


# def func():
#     raise ConnectionError


# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc


# try:
#     open('database.sqlite')
# except OSError as exc:
#     raise RuntimeError from exc


with open("myfile.txt") as f:
    for line in f:
        print(line, end="")


def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )


# try:
#     f()
# except* OSError as e:
#     print("There were OSErrors")
# except* SystemError as e:
#     print("There were SystemErrors")


def f():
    raise OSError('operation failed')


excs = []
for i in range(3):
    try:
        f()
    except Exception as e:
        e.add_note(f'Happened in Iteration {i+1}')
        excs.append(e)

raise ExceptionGroup('We have some problems', excs)
