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

