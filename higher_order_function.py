from functools import reduce
import numpy

def Summation(nums):
    return sum(nums)

def Product(nums):
    expr = lambda x, y: x*y
    return reduce(expr, nums)

# Pretty meaningless but it works
def Factorial(n):
    return Product(numpy.arange(1, n+1))

def Action(func, nums):
    return func(nums)

print(Action(Summation, [1, 2, 3, 4]))
print(Factorial(5))