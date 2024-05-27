def greet():
    print('hello Good Morning.')


def greet_someone(name):
    print(f"Hello {name}")


def greet_someone(name):    # name is an argument/ parameter
    return f"Hello {name}"


def message(name, age, pay):
    return f"hello {name} you are {age} years of age and you get $ {pay} as a pay"


y = message('steve', 28, 1500)
a = 'python is easy to learn'
c = len(a)


def message(name, /, *, age, pay):
    # note:- the Keyword arguments should follow the positional arguments else it returns Error
    # The arguments which are RHS of "*" are mandetorly keyword only arguments
    # The arguments which are LHS of "/" are mandetorly positional only arguments
    return f"hello {name} you are {age} years of age and you get $ {pay} as a pay"


def func(name, age=18, pay=1000):
    # Here name is mandetory argument, where age & pay are optional
    return f"hello {name} you are {age} years of age and you get $ {pay} as a pay"


def add(a, b, c=0, d=0, e=0, f=0):
    return a + b + c + d + e + f


def func(a, b, *args):
    # here a, b are mandetory arguments, where args are optional
    # here "*" is responsible to pack all the extra elements to a collection as Tuple
    # Here "*" is used to accept variable number of positional arguments
    res = a + b + sum(args)
    return res


def func1(**kwargs):
    return kwargs


def func2(*args, **kwargs):
    print(args)
    print(kwargs['a'])


def msg(**kwargs):
    return f"hello {kwargs['name']} you are {kwargs['age']} years of age and you get $ {kwargs['pay']} as a pay"


def func(a, b, c):
    return a, b, c


x = (10, 20, 30)
func(*x)


def func1(name, age, pay):
    return f"Hello {name} you are {age} years of age and you get $ {pay} as a pay"
d = {'name': 'steve', 'age': 28, 'pay': 2000}


def func1(name: str, age: int, pay: float, married: bool = False):
    print(f"Hello {name} you are {age} years of age and you get $ {pay} as a pay")
    if married:
        print('Khel Khatam Natak Bundh')
    else:
        print('Still Waiting to get killed')


# Lambda Expression:- Lambda is a keyword which is used to define/ create an ananomous function.
# here variable name is going to act as the function name
x = lambda a, b: a + b
x = lambda a, b: a > b and b + 10 >20
c = lambda a: a ** 3


x = map(lambda a: a ** 3, range(1, 101))

y = ['steve', 'bill', 'anna', 'mark', 'elon', 'jilani', 'milani', 'umani', 'osama', 'bin', 'harami']
res = map(len, y)

def srt(a):
    y = list(a)
    y.sort()
    return ''.join(y)


# Map:- it is a built-in function which is used to execute the function on the given collection
# the resultant variable contains the output of the function
res1 = map(lambda a:''.join((sorted(a))), y)
# filter:- it is a built-in function which is used to execute the function on the given collection
# the resultant variable contains the input of the functio if it returns the output as True else, it will not store any values
res = map(lambda a: a ** 2, filter(lambda a:a % 2 == 0, range(1, 101)))
