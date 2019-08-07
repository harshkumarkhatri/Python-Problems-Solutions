"""Write a program which accepts a string as input to print "Yes" if the string is
"yes" or "YES" or "Yes", otherwise print "No". """
z=input("enter the string")
list=["yes","YES","Yes"]
if z in list:
    print("yes")
else:
    print("No")