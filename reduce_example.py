from functools import reduce

data = [1, 2, 3, 4]
expr = lambda x, y: x*y

prod = reduce(expr, data)
print(prod)

prod2 = 1
for x in data:
    prod2 *= x

print(prod2)