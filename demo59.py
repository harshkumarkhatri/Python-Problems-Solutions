"""Write a program which accepts a sequence of words separated by whitespace as
input to print the words composed of digits only.
"""
import re
z=input("enter the string")
print(re.findall("\d+", z))