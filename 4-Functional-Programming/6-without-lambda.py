def myfun(n):
    def mulfun(a):
        return a*n
    return mulfun

multiply = myfun(2)
print(multiply(5))

