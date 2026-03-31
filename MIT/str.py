text = 'my sql'
"""
print(text[-1:-7:-1])
print(text[::-1])

print(text.upper())
print(a.count('m'))
print(a.index(' '))
"""


def check_date(date):
    if len(date) == 10:
        if date[4] == '-' and date[7] == '-':
            if int(date[5]) > 1 or int(date[8]) > 3:
                return False
            else:
                return True
        else:
            return False


    if len(date) == 8:
        if int(date[4]) > 1 or int(date[6]) > 3:
            return False
        else:
            return True


    else:
        return False
"""
"""




if check_date("2001-09-24"):
    print("True")
else:
    print("False")


"""
x = 10
n = 0
while x <= 99:
    x = x+1
    n = n+1

print(n)  
"""
