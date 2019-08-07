"""Please write a program which count and print the numbers of each character in a
string input by console.
Example:
If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1"""
z=input("enter a string")
li={}
for i in z:
    li[i]=li.get(i,0)+1
print(li.items())
#in it he arguments which are passed in
# the li.get(a,b) are as follows
#a=the item which is to be searched in it
#b=the default or the starting value from
# which counting of the elements will take place
#the use of +1 is to either increase the value/count of
# the searched element or to shift to next element