"""Assuming that we have some email addresses in the "username@companyname.com"
format, please write program to print the user name of a given email address.
Both user names and company names are composed of letters only."""

#1
li=[]
z=[i for i in input("enter the mail address").split('@')]
li.append(z[0])
print(li[0])

#2
import re
demo=input("enter the mail address")
d2="(\w+)@(\w+\.)+(com)"
dq=re.match(d2,demo)
print(dq.group(1))