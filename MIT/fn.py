"""
handy trick to 
"""

def myDoub(x):
    return (x*2.0)

n = float(input())
m = myDoub(n)


if m == n*2:
    print(m)
elif n == m:
    print(-1)
else:
    print(0)

