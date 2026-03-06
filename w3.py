
def myF():
    x = str(3)
    y = int(3)
    z = float(3)
    print(type(x))
    print(type(y))
    print(type(z))

#myF()

a = [1,2,3]
x,y,z = a
print(x,y,z)
print(x+y+z)


def myY():
    global x;  #without global it just creates a new local variable x
    x = 2

myY()
print(x)
