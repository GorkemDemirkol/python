x=lambda a:a+10
print(x(5))

y=lambda a,b:a*b
print(y(5,6))

def myfunc(n):
    return lambda a:a*n
triple=myfunc(3)
print(triple(10))
