"""Assuming that we have some email addresses in the "username@companyname.com"
format, please write program to print the company name of a given email address.
Both user names and company names are composed of letters only.
"""

#1
li=[]
li2=[]
z=[i for i in input("enter the mail address").split('@')]
li.append(z[1])
z1=li[0]
z2=z1.split('.')
li2.append(z2[0])
print(li2[0])

#2
import re
emailAddress = input("enter email")
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print(r2.group(2))
