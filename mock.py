# #wap to find the number of word in the given string. no builtin fun
a=input('enter a string')
count=1
i=0
while i<len(a):
    if a[i]==' ' and a[i+1].isalnum():
        count+=1
    i+=1

print(count) 

# #wap to extract all the perfect numbers in btw user entered limits

# a = int(input('enter the starting range'))
# b=int(input('enter the ending range'))

# s=0
# res=[]
# j=1
# for i in range(a,b+1):
#     while j<i:
#         if i%j==0:
#             res.append(j)
#         j+=1
#     j=1
    
#     if sum(res)== i:
#         print(f'{i} is a perfect number')
#     res.clear()





# #wap to create a class which consist of 5 class method , 5 object method, and 2 ststic method
# class cars:
#     wheels=4
#     seats=5
#     airbags=4
#     color = 'black'
#     top = 'no top'
    
#     def display(self):
#         print(self.airbags)
#         print(self.wheels)
#         print(self.seats)
#         print(self.color)
#         print(self.top)
        
#     def __init__(self,name,color,seats):
#         self.name=name
#         self.color=color
#         self.seats=seats
    
#     def cardetails(self):
#         print(self.name)    
#         print(self.color)
#         print(self.seats)
        
#     def ch_name(self,new):
#         self.name = new 
#         print(self.name) 
        
#     def ch_seats(self,new):
#         self.seats=new
#         print(self.seats) 
             
#     @classmethod
#     def ch_airbags(self,new):
#         airbags = new
#         print(self.airbags)
        
#     @classmethod
#     def ch_seats(self,new):
#         seats = new
#         print(self.seats)
    
#     @classmethod
#     def ch_wheels(self,new):
#         wheels = new
#         print(self.wheels)
        
#     @classmethod
#     def ch_airbags(self,new):
#         color = new
#         print(self.color)
        
#     @staticmethod
#     def message():
#         print("it is a good car")
        
#     @classmethod
#     def ch_top(self,new):
#         top = new
#         print(self.top)
    
#     @staticmethod
#     def repair():
#         print('your car needs to be servised')
    
    
# c1=cars()
# c1.message()
# c1.display()
        

# WAP to group the words with respect to the first char of the word
# a = input('enter a string').split()
# res ={}

# for i in a :
#     if i[0] in res:
#         res[i[0]]+=[i]
#     else:
#         res[i[0]]=[i]
# print(res)
