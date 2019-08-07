"""Write a program which accepts a sequence of comma separated 4 digit binary
numbers as its input and then check whether they are divisible by 5 or not. The
numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
Hints:
In case of input data being supplied to the question, it should be assumed to be
a console input."""
loop=True
while loop:
    list=[]
    list2=[]
    loop=False
z=[i for i in input("enter the numbers with comma in between").split(',')]
list.append(z)
print(list)

"""Print a unicode string "hello world".
Hints:
Use u'strings' format to define unicode string.
"""
unicodeString = u"hello world!"
print(unicodeString)



"""Write a program to read an ASCII string and to convert it to a unicode string
encoded by utf-8.
Hints:
Use unicode() function to convert.
"""

s =input()
u = unicode( s ,"utf-8")
print(u)





"""A website requires the users to input username and password to register. Write a
program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will
check them according to the above criteria. Passwords that match the criteria
are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
Hints:
In case of input data being supplied to the question, it should be assumed to be
a console input."""
#demo21
import re
list=[]
z=[i for i in input("enter the text with comma sequence").split(',')]
for j in z:
    if len(j)<6 and len(j)>12:
        continue
    else:
        pass
    if not re.search('[a-z]',j):
        continue
    elif not re.search('[0-9]',j):
        continue
    elif not re.search('[A-Z]',j):
        continue
    elif not  re.search('[$#@]',j):
        continue
    elif re.search('\s',j):
        continue
    else:
        pass

    list.append(j)
    print(list)
print(','.join(list))




"""A robot moves in a plane starting from the original point (0,0). The robot can
move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot
movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡
The numbers after the direction are steps. Please write a program to compute the
distance from current position after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
Hints:
In case of input data being supplied to the question, it should be assumed to be
a console input.
"""
#demo24


"""Write a program which can filter even numbers in a list by using filter
function. The list is: [1,2,3,4,5,6,7,8,9,10].
Hints:
Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.
"""
#demo46
lno= [1,2,3,4,5,6,7,8,9,10]
evenNumber =filter(lambda x: x%2==0,no)
print(evenNumber)



"""Define a class named American and its subclass NewYorker. """
#demo53
class american():
    print("class am")
    pass
class newyork(american):
    pass
demo1=american()
demo2=newyork()
print(demo1)
print(demo2)



"""Please write a program to compress and decompress the string "hello world!hello
world!hello world!hello world!".
Hints:
Use zlib.compress() and zlib.decompress() to compress and decompress a string.
"""
import zlib
s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))





"""Please write a program to print the running time of execution of "1+1" for 100
times.
Hints:
Use timeit() function to measure the running time.
"""
from timeit import Timer
t = Timer("for i in range(100):1+1")
print(t.timeit())
#if we are running this code than the output
# is not coming 2 rather it comes1.some decimal value





