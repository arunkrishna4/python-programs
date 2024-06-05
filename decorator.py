from time import sleep
import time
from collections import defaultdict
# a is pointing to a memory location where an integer object has been stored
a = 25
# x is pointing to a memory location where "a" is pointing to
x = a

# b is pointing to a memory location where a float object has been stored
b = 25.9
# y is pointing to a memory location where "b" is pointing to
y = b

# c is pointing to a memory location where a list object has been stored
c = [10, 20, 20]
# z is pointing to a memory location where "c" is pointing to
z = c


# Add is pointing to a memory location where set of instructions has been stored
def add(a, b):
    c = a + b
    return c

# "a" is pointing to a memory location where add i pointing
a = add


def sub(a, b):
    c = a - b
    return c

s = sub


def mul(a, b):
    c = a * b
    return c

m = mul

def div(a, b):
    c = a / b
    return c

d = div

i = []
i.append(a)
i.append(s)
i.append(m)
i.append(x)
i.append(y)
i.append(z)


for j in i:
    if callable(j):
        print(j.__name__)

# Using elif pattern
def calculator(opcode, a, b):
    if opcode == 'add':
        return add(a, b)
    elif opcode == 'sub':
        return sub(a, b)
    elif opcode == 'mul':
        return mul(a, b)
    elif opcode == 'div':
        return div(a, b)
    else:
        print('invalid operation')

# using Dictionary method
operations = {
    'add':add,
    'sub':sub,
    'mul':mul,
    'div':div
    }

def cal(opcode, a, b):
    if opcode in operations:
        return operations[opcode](a, b)
    else:
        print('invalid operation')


def add(a, b):
    c = a + b
    return c

def sub(a, b, c):
    d = a - b - c
    return d

def mul(a, b, c, d):
    e = a * b * c * d
    return e

def div(a, b, c, d, e):
    f = a / b/ c/d/e
    return f


operations = {
    'add':add,
    'sub':sub,
    'mul':mul,
    'div':div
    }

def cal(opcode, *args):
    if opcode in operations:
        return operations[opcode](*args)
    else:
        print('invalid operation')
def add(a, b):
    c = a + b
    sleep(2)
    return c

def sub(a, b, c):
    d = a - b - c
    sleep(2)
    return d

def mul(a, b, c, d):
    e = a * b * c * d
    sleep(2)
    return e

def div(a, b, c, d, e):
    f = a / b/ c/d/e
    sleep(2)
    return f


# delay decotaror
def delay(func):
    def wrapper(*args):
        sleep(5)
        return func(*args)
    return wrapper
        
##x = delay(add)
##
##y = delay(sub)

@delay
def add(a, b):
    c = a + b
    return c
@delay
def sub(a, b, c):
    d = a - b - c
    return d

@delay
def mul(a, b, c, d):
    e = a * b * c * d
    return e

@delay
def div(a, b, c, d, e):
    f = a / b/ c/d/e
    return f


# timer Decorator
def timer(func):
    def wrapper(*args):
        start = time.time()
        x = func(*args)
        end = time.time()
        print(f"The time taken to execute the function is {end-start}")
        return x
    return wrapper



@timer
def add(a, b):
    sleep(1)
    c = a + b
    return c
@timer
def sub(a, b, c):
    d = a - b - c
    return d

@timer
def mul(a, b, c, d):
    e = a * b * c * d
    return e

@timer
def div(a, b, c, d, e):
    f = a / b/ c/d/e
    return f


d = defaultdict(int)
def counter(func):
    def wrapper(*args):
        x = func(*args)
        d[func.__name__] += 1
        return x
    return wrapper

@counter
def add(a, b):
    c = a + b
    return c
@counter
def sub(a, b, c):
    d = a - b - c
    return d

@counter
def mul(a, b, c, d):
    e = a * b * c * d
    return e

@counter
def div(a, b, c, d, e):
    f = a / b/ c/d/e
    return f


d = defaultdict(int)
def count(func):
    def wrapper(*args):
        if d[func.__name__] < 3:
            x = func(*args)
            d[func.__name__] += 1
            return x
        return f"The Function {func.__name__} executed morethen 3 time"
    return wrapper

@count
def add(a, b):
    c = a + b
    return c
@count
def sub(a, b, c):
    d = a - b - c
    return d

@count
def mul(a, b, c, d):
    e = a * b * c * d
    return e

@count
def div(a, b, c, d, e):
    f = a / b/ c/d/e
    return f












