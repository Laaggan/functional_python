def Square(x):
    return x*x

Square2 = lambda x: x * x

x = [1, 2, 3, 4, 5]

print(list(map(Square, x)))
print(list(map(Square2, x)))