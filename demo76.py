"""Please write a program to generate all sentences where subject is in ["I",
"You"] and verb is in ["Play", "Love"] and the object is in
["Hockey","Football"].
Hints:
Use list[index] notation to get a element from a list"""
sub=["i",'you']
verbs=["play","love"]
object=["hockey",'football']
for i in range(len(sub)):
    for i in range(len(verbs)):
        for i in range(len(object)):
            s=sub[i]+verbs[i]+object[i]
            print(s)