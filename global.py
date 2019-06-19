a = 3

def some_func():
    global a
    a = 5

print(a)
some_func()
print(a)