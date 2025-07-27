def myfun(n):
    return lambda a : a*n

double = myfun(2)
print(double(10))

triple = myfun(3)
print(triple(10))