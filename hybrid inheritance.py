class fourwheelers:
    wheels=4
    seats=5
    
    
class cars(fourwheelers):
    engine = 250
    mileage = 18

    def sound(self):
        print('zooooooooom')
    
class supercars(fourwheelers):
    engine = 900
    mileage = 6
    
    def supercarsound(self):
        print("vroom vroom")
    
# porsche = supercars()
# print(porsche.wheels)
# porsche.supercarsound()

class bmw(supercars):
    engine = 1500
    mileage = 15
    
    def s_quality(self):
        print("It's interior, eyes and hoursepower is the speciality" )

class creta(cars):
    engine = 500
    mileage = 30

    def s_quality(self):
        print("It's known for comfort and exteriors.")
        

c1 = supercars()
c1.supercarsound()
c2=bmw()
c2.s_quality()