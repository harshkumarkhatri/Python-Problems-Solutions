"""Write a program that accepts a sentence and calculate the number of letters and
digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3"""
z=input("enter the string")
demo={"digit": 0,'letters':0}
for c in z:
    if c.isdigit():
        demo["digit"]+=1
    elif c.isalpha():
        demo['letters']+=1
print(demo)