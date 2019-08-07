#take a string remove characters except for vowels from it and save it in dictionary
x=input("enter a string")
vowels=['a','e','i','o','u']
string_vowel=[]
cons_vowel=[]
nary={}
loop=True
while loop:
    list=[]
    loop=False
z=len(x)
for i in range(1,z+1):
    temp=x[i-1]
    list.append(temp)
print(list)
for element in list:
    if element in vowels:
        string_vowel.append(element)
    else:
        cons_vowel.append(element)
if len(string_vowel)==0 and len(cons_vowel)==0:
    print("you dont have any characters in the string")
elif len(string_vowel)==0 and len(cons_vowel)!=0:
    print("no vowels present")
    print(cons_vowel)
elif len(string_vowel)!=0 and len(cons_vowel)==0:
    print(string_vowel)
    print("no consonants are present")
else:
    print("vowels present are")
    print(''.join([string_vowel[i] for i in range (0,len(string_vowel))]))
    print("consonants are")
    print(''.join([cons_vowel[i] for i in range(0,len(cons_vowel))]))

nary['vowels']=string_vowel

nary['consonants']=cons_vowel
print(nary.items())