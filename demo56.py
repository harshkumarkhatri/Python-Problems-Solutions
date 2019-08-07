"""Write a function to compute 5/0 and use try/except to catch the exceptions."""


def throw():
    return 5/0
try:
    throw()
except ZeroDivisionError:
    print("galat hai")
