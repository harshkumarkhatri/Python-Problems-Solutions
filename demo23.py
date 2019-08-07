"""Define a class with a generator which can iterate the numbers, which are
divisible by 7, between a given range 0 and n."""

def iterate(n):
    z=int(n)
    for i in range(0,z):
        if i%7==0:
            print(i)
iterate(710)