from math import pi
from functions import res
# Globval Variables
a = 125
b = 225
def func(a, b):# enclosed Variables
    # Local Variables
    a = 10
    b = 20
    c = a + b
    print(c)
    

a = 10
def func():
    b = 20
    c = a + b
    a = 100
    print(c)


a = 100
def func():
    a += 20
    print(a)



a = 100
def func():
    global a
    a += 20
    x = 900
    print(a)





# Globval Variables
a = 125
b = 225
def func(a, b):# enclosed Variables
    # Local Variables
    a = 10
    b = 20
    c = a + b
    print(pi)
print(res)
res = 2500

print(res)
