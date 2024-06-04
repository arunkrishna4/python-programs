 # #WAP to print first n natural numbers
 # n= int(input('enter a number: '))
 # i=1
 # while i<=n:
 #     print(i,end= '\t')
 #     i+=1 
    
 #WAP to print all the odd numbers in between 

 # s=int(input('enter a no1'))
 # x = int(input('enter a no2'))
 # i=s
 # while i==x:
 #     if i%2 != 0:
 #         print(i)
 #     i+=1

# #WAP to print all the 3 digit numbers which are divisible by 9 & 3

# a=100
# b=999
# i=a
# while i<=999:
#     if i%3==0 and i%9==0:
#         print(i)
#     i+=1

#WAP to print all the uppercase alphabet in the sring
# a= input('enter a string')
# i=0
# while i<len(a):
#     if 'A'<=a[i]<='Z':
#         print(a[i])
#     i+=1
    
#WAP to print all the alphabets that are present in the even index position
# a= input('enter a string')
# i=0
# while i<len(a):
#     if 'A'<=a[i]<='Z' and i%2==0:
#         print(a[i])
#     i+=1
    
#WAP to extract all the vwel charaters from the give string 
# a= input('enter a string')
# i=0
# res= ' '
# while i<len(a):
#     if a[i] in 'aeiouAEIOU':
#         res+=a[i]
    
#     i+=1
# print(res)

#WAP to print multiplacation table of user given number

# a = int(input('enter a number'))
# i=1
# while i<=10:
#     print(f'{a} * {i} = {a*i}')
#     i+=1
    

# WAP to replace the space in the given string to underscore

# a= input("enter a string")
# res=''
# i=0
# while i<len(a):
#     if a[i] == ' ':
#         res=res + '_'
#     else:
#         res+=a[i]
#     i+=1
# print(res)

# print(ord('z'))

 #WAP to toggle a string
# a= input('enter the string')

# i=0
# while i<len(a):
#     if 'A'<=a[i]<='Z':
#         print(chr(ord(a[i])+32))
#     elif 'a'<=a[i]<='z':
#         print(chr(ord(a[i])-32) )
#     i+=1

# #WAP to check wheater a string is pallindrome or not 
#----------method 1-------------
# a= input('enter a sting')
# res = a[::-1]

# if res == a:
#     print('pallindrome')
# else:
#     print('not a pallindrome')

#-------------method 2-----------
# a= input('enter a string')
# res =''
# i=0
# while i<len(a):
#     res = a[i]+res
#     i+=1
#     if res==a:
#         print('pallindrome')
#     else:
#         print('not pallindrome')
        
#-------method 3-----------
# a= input('enter a string')
# res =''
# i=len(a) -1
# while i<len(a):
#     res += a[i]
#     i-=1
#     if res==a:
#         print('pallindrome')
#     else:
#         print('not pallindrome')        


#WAP to find the sum of first n natural numbers
# n=int(input('enter a number'))
# res =0

# i=0
# while i<=n:
#     res+=i
#     i+=1

# print(res)

#wap to find the factorial of a number
# n=int(input('enter a number'))
# res =1
# i=1
# while i<=n:
#     res*=i
#     i+=1
# print(res)

#WAP to find the sum of all int numbers in the given list
# a=[10,221,2.3,'java','steve', 26+9j,[10,20,30]]
# res=0 
# i=0
# while i<len(a):
#     if isinstance(a[i],int):
#         res+=a[i]
#     i+=1
# print(res)

#WAP to seperate the char acc to their catogery

# a = input('enter a string')
# uc,lc,nc,sc = '','','',''

# i=0
# while i<len(a):
#     if 'A'<=a[i]<='Z':
#         uc+=a[i]
#     elif 'a'<= a[i]<='z':
#         lc +=a[i]
#     elif '0'<=a[i]<='9':
#         nc+=a[i]
#     else:
#         sc+=a[i]
#     i+=1
# print(f'uppercase :{uc}')
# print(f'lowercase :{lc}')
# print(f'numeric :{nc}')
# print(f'uppercase : {sc}')

#WAP to remove the duplicate char from yhe given string wihtout using typecasting 

# a=input('enter a string')
# res=''
# i=0
# while i<len(a):
#     if a[i] not in res:
#         res+=a[i]
#     i+=1
# print(res)

#WAP to find sum of all individual digits of a given int number without using typecasting

# a= int(input('enter a number'))

# res = 0
# while a>0:
#     ld=a%10
#     res+=ld
#     a//=10
# print(res)

# WAP to reverse the given integer number without using without using typecasting

# a= int(input('enter a number'))

# res = 0
# while a>0:
#     ld=a%10
#     res=res*10+ld
#     a//=10
# print(res)


# WAP to get all the divisors of a given number

 # a=int(input('enter a number'))
# res=[]
# i=1
# while i<a:
#     if a%i ==0:
#         res.append(i)
#     i+=1
# print(res)


#prime number

# a=int(input('enter a number'))
# res=[]
# i=1
# while i<a:
#     if a%i ==0:
#         res.append(i)
#     i+=1
# if len(res) ==1:
#     print('It is a Prime Number')
# else:
#     print('It is not a prime Number')
 
    
#amicable 

# a=int(input('enter a number1'))
# b = int(input('enter a number2'))
# res1,res2 = [],[]
# i=1
# while i<a:
#     if a%i ==0:
#         res1.append(i)
#     i+=1   
# j=1
# while j<b:
#     if b%j ==0:
#         res2.append(j)
#     j+=1
# s1=sum(res1)
# s2 =sum(res2)
# if s2 == a and s1 == b:
#     print('it is a amicable number')
# else:
#     print('Not a amicable number')


#perfect (sum of divisors)

# a=int(input('enter a number'))
# res=[]
# i=1
# while i<a:
#     if a%i ==0:
#         res.append(i)
#     i+=1
# s=sum(res)
# if s == a:
#     print('it is a perfect number')
# else:
#     print('Not a perfect number')


# strong  (product of divisors)

# a=int(input('enter a number'))
# mul = 1
# i=1
# while i<a:
#     if a%i ==0:
#         mul*=i
#     i+=1
# if mul == a:
#     print('it is a Strong number')
# else:
#     print('Not a Strong number')


# spy (sum and product of divisors should be same as the number)

# a=int(input('enter a number'))
# res=[]
# mul =1
# i=1
# while i<a:
#     if a%i ==0:
#         res.append(i)
#     i+=1 
# s=sum(res)
# j=0
# while j<len(res):
#     mul = mul *res[j]
#     j+=1
# if s == a and mul == a:
#     print('is a spy number')
# else:
#     print('not a spy number')


# WAP to check whether the number is armstrong number or not 
# a= int(input('enter a number'))
# l=0
# i=a
# while i>0:
#     l+=1
#     i//=10
# sum=0
# j=a
# while j>0:
#     ld=j%10
#     sum+=ld**l
#     j//=10
    
# if sum==a:
#     print('it is a armstrong number')
# else:
#     print('it is not a armstrong number')
    
# fibonacci series

# a =int(input('enter a number'))
# n1,n2=0,1
# i=0
# while i<a:
#     print(n1,end='\t')
#     sum=n1+n2
#     n1=n2
#     n2=sum
#     i+=1

#wap to convert the Hash in the input to number.

# a = ['#cars','##suv','##xuv','##hatchback','##sedan','#bikes','##sports','##naked','##adv','##cruise']
# ch=0    
# tp=0 
# i=0
# while i<len(a):
#     if a[i][1] !='#':  
#         ch+=1    
#         tp=0 
#         print(f'{ch}.{a[i][1:]}')        
           
#     elif a[i][1] =='#': 
#         tp+=1
#         print(f'{ch}.{tp}.{a[i][2:]}')  
#     i+=1


# WAP to check wheater the list is homogeneous elements without using builtin fun()

a= [19,12,7,532]
dt =type(a[0])
flag =0
i=0
while i<len(a):
    if  not (isinstance(a[i],dt)):
        flag +=1
    i+=1

if flag == 1:
    print('heterogeneous')
else:
    print('homogeneous')
    
