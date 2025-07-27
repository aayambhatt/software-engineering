def square(n):
    return n**2

def highfunc(func, nums):
    result = []
    for num in nums:
        result.append(func(num))
    return result

funcCall = highfunc(square, [1,2,3,6])
print(funcCall)
