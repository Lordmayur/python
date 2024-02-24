#acessing elelment from dictionary 
new={1:"hello",2:"hi",3:"namaste"}
print(new)
print(new[2])
print(new.get(3))

#updating value
new[1]="hey"
print(new)

#adding value
new[4]="hola"
print(new)

#creating a new dictionary
squares = {1:1,2:4,3:9,4:16,5:25}
print(squares)

#remove a particular item 
print(squares.pop(5))
print(squares)

#iteration in dictionary (iteration means one below one)
squares = {1:1,2:4,3:9,4:16,5:25}
for i in squares:
    print(squares[i])

#using built-in function in a dictionary 
squares = {1:1,2:4,3:9,4:16,5:25}
print(len(squares))#prints the length of the dictionary
print(sorted(squares))#prints the dictionary in sorted order

