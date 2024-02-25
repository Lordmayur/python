#different ways to define a string in python
mystr1='welcome'
print(mystr1)

mystr2="welcome"
print(mystr2)

mystr3='''welcome'''
print(mystr3)

#triple quotes string can extend multiple llines 
mystr4='''welcome 
to the world of programming'''
print(mystr4)

#acessing character in a string
mystr='manjunath'
print(mystr[0])
print(mystr[1])
print(mystr[2])
print(mystr[3])
print(mystr[4])
print(mystr[5])
print(mystr[6])
print(mystr[7])
print(mystr[8])

#concatenation of strings
mystr7='hola'
mystr8='amigo'
print(mystr7+mystr8)

#iterating through string
letter_count = 0
for letters in 'hello world':
    if (letters == 'o'):
        letter_count += 1
    print(letter_count,'times 1 letter has been found')