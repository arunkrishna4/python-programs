class demo:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a # a.a + b.a

    def __sub__(self, other):
        return self.a - other.a

    def __mul__(self, other):
        return self.a * other.a
    

a = demo(10)
b = demo(20)

