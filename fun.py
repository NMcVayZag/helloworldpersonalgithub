import math


# this is a one line comment in python
# a comment is "code" that is ignored by python 
# we use comments to document our code

""" Tripple double quotes is known as a 
block
comment
which is not executable code
It will not print"""

print("hello world")

#variables
x = 5.9 #read this as x is assigned 5 or x stores 5
#Not x equals 5
#variables store values
#a value has a data type - a data type houses a specific range of values
#integers stores whole numbers
print(type(x))
print(x)
#float data type is short for floating point number
x= int(x)
print(x)
# a string is a sequence of characters
# elinter is a spell check program in the editor

#OPERATORS
#pemdas
print(35*20000000/2)
# / is known as floating point division
# // is known as integer division which will return an integer that will be rounded down to the nearest whole number
# truncate is chopping off fractional segments
# ** is known as exponiation or power
print(2**4) # if multiple use of ** the statement will evaluate right to left not right to left
#a .py file will also be known as a module or a script
print(math.sqrt(16))
print(math.pow(2,4)) #pow will create a float result vesurs when we use ** we receive a integer

#GETTING USER INPUT

#input nonsense

#Formating decimal numbers
#few ways to do this
# C style method
print(math.pi)
print("%.2f" %(math.pi))
#pythonic way
print("{:.3f}".format(math.pi))
#use built in funtion round 
print(round(math.pi,2))
print(18//4)
print(2**2**3*3)
print("test")
print("hope this shoes on github")
# negation or negativity has the secondary priority in pemdas or operation precedence ex. x= -4 / 8 *(32/2)
#exersize:
#m=int(input("enter an integer> "))
#n=int(input("enter an integer> "))
#m= m+5
#n= 3*n
#print("m =", m, "\nn =", n)  #\n can be used within a str to spawn a new line

#else keyword for conditionals
if x==6:
    print("x is 6")
else:
    print("x is not 6")
#elif is used to test a number of if statements to test in a row #if elif elif then else.
x = 5
if x<0:
    print("x is negative")
elif x>0:
    print("x is positive")
else:
    print("x is zero")

#LOOPs
# for loops and while loops 
for character in "gonzaga":
    print(character,end="*")
print("\n")

#range example
#range(9) generates a sequence [0,9) #9 isn't called into the loop
for i  in range(0,9):
    print(i, end=" ")
print("\n")
for i in range(2,42,2):
    if i==40:
        print(i)
    else:
        print(i,end=", ")
print("\n")
for i in range(8,3,-2):
    print(i, end=" ")

#while loop structure
k = 2
while k <= 40:
    print(k,end=", ")
    k +=2
print(k)

#funtions are a named sequence of statements  
#write it once use it manytimes
#helps with code organization
#no funtions used for DA1
