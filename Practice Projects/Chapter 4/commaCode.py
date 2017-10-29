def commaCode(lst):
    lst.insert(-1, 'and')
    newString = ''
    for i in lst:
        if i == 'and':
            newString = newString + i + ' '
        elif i == lst[-1]:
            newString = newString + i
        else:
            newString = newString + i + ', '
    return newString

spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs', 'salmon']
print(commaCode(spam))
