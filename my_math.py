def myPow():
    x = 4
    y = 0.5
    myPow = x**y
    print(myPow)
# powers and (sq)roots in python



def myQuadratic():
    a = input()
    b = input()
    c = input()
    try :
        a = float(a)
        b = float(b)
        c = float(c)    
        r1= ((-1) * b + (((b**2) - (4 * a * c)) ** 0.5)) / (2 * a)
        r2= ((-1) * b - (((b**2) - (4 * a * c)) ** 0.5)) / (2 * a)
        print(r1, " ", r2 )
    except :
        print('Error')
#quadratic formula in python

myQuadratic()
