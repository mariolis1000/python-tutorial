# to exit the python interpreter
# >>>
# type exit()

"""
+  addition
-  subtraction
*  multiplication
** power
/  division (FLOATING-POINT) 
// division (INTEGER)
%  remainder (of integer division)
"""
""" parenthesis -> power -> multiplication -> addition -> leftToRight """
#operators in python

"""
is
is not

0 == 0.0  #True
0 is 0.0 #False

Essentially, they check if the two values are
equal in BOTH value AND type
"""
#is and is not , preferably use only with None and Booleans

"""
max()
min()
"""
#to get min or max value (works even in strings)

def exampleConcat():
    string1 = '...'
    string2 = '/...'
    string3 = string1 + string2
    print(string3)
#to concat two strings


def exampleType():
    type(variable)
#to get the data type of a variable


def exampleIntToFloat():
    i = 42
    f = float(i)
    print(type(f))
#to convert an int to a float


def exampleStrToInt():
    stri = '119'
    inte = int(stri)
    print(inte+1)
#to convert a string into an int


def exampleIf():
    x = 10
    if x < 10:
        print("Smaller")
    elif x > 10 :
        print("Larger")
    else :
        print("Finished")
#if statements in python



def exampleWhile():
    n = 0
    while n < 10:
        print(n)
        n = n + 1
        if n == 4 :
            continue  #continue stops the current iteration and goes back to the top
        if n == 5 :
            break     #break exits the current loop
    print("Finished for real")    
#while loops in python

def exampleFor():
    x = [0,1,2,3,4]
    largest = None
    for i in x:
        if largest is None:
            largest = i
        elif largest < i:
            largest = i
    print(i)  
#for loops in python , the use of None is very useful   



def inputExample():
    x = input('Give me a number: ')
    y = input('Give me another number: ')
    if x > y:
        print(x)
    else :
        print(y)
#to get user input in python



def exampleExceptions():
    hel = 'This is a string'
    try :
        int(hel)
    except :
        hel = -1
    print(hel)
    her = '987'
    try :
        int(her)
    except :
        her = -1
    print(her)
#exception or error handling


def myFunc():
    print("Something")
#function creation   --I can also do my_func()
# myFunc()
#function calling



def myAdd(fir,sec):
    result = fir + sec
    return result
#function with parameters/arguments that returning a value
"""
x = float(input())
y = float(input())
s = myAdd(x,y)
print(s)
"""

















li = [3,41,12,9,74,15]

def myLargest():
    mymax = 0
    for i in li:
        if mymax < i :
            mymax = i
    return mymax
def mySize():
    count = 0
    for i in li:
        count = count + 1
    return count
def mySum():
    s = 0
    for i in li:
        s = s + i
    return s
def myAvg():
    result = mySum() / mySize()
    return result
#examples using for loops





def europeAmericaFloors():
    location = input('Are you in Europe or America? ')
    if location == 'America':
        a = int(input('Type what American floor you are in: '))
        print("In Europe this woud be floor number ", (a - 1))
    elif location == 'Europe':
        e = int(input('Type what European floor you are in: '))
        print("In America this woud be floor number ", (e + 1))
    else : 
        print("Error")
#example with input


def milesToKm():
    ratio = 1.609
    conversion = input("To convert miles to km, type 'Miles', otherwise type 'Km' ")
    data = float(input("Give me the number to convert "))
    if conversion == 'Miles':
        print(data*ratio)
    elif conversion == 'Km':
        print(data/ratio)
    else : 
        print("Error") 
#another exmple that converts miles to km and vice versa



