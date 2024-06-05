class prime:
    movies = 800
    series = 400
    tv_shows=900
    
    def __init__(self,name):
        self.name=name
        pwd = input('enter the password: ')
        rpwd = input('enter the passsword again: ')
        if pwd == rpwd:
            print(f'Welcome {name}')
        else:
           print('Wrong credentials')
    
    def details(self):
        print(self.name)
        print(f"{self.series}")
        print(f"{self.movies}")
        
    
    def watching(self,mname):
        print(f"you are watching {mname}")    # doubt
    
    def addtoqueue(self,*args):
        print(f"items added to queue : {args}")
        
    @classmethod
    def addmovies(cls,num):
        cls.movies+=num
            
            
            
c1=prime("Akash")
c1.details()
c1.watching('The Big Bang Theory')
c1.addtoqueue('hi','hello')
prime.addmovies(20)
print(prime.movies)
print(c1.movies)