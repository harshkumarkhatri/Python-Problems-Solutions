#accepting words with comma sequence and printiong the same in sorted format
items=[i for i in input("enter the word with comma in between").split(',')]
print(''.join(sorted(items)))