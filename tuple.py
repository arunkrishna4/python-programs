# 1.wap to print all the values in a tuple to another tuple

# a=("apple","banana", "cherry")
# print(a)

# 2.wap to print all the values in a tuple to another list.

# a =(1,2,3,4,5)
# print(list(a))

# 3.wap to print all the even digits in a tuple to another tuple.

# a = (12,334,35,43,2,54,23,5,3,6,43)
# b=[]
# i=0
# while i<len(a):
#     if a[i]%2==0:
#         b.append(a[i])
#     i+=1
# print(tuple(b))
# c=tuple(b)

# 4.wap to print all the even digits in a tuple to another list.

# a= (12,24,43,4,23,34,57,34,378)
# b=[]
# i=0
# while  i < len(a):
#     if a[i] % 2 == 0 :
#         b.append(a[i])
#     i+=1
# print(b)

# 5.wap to print all the odd digits in a tuple to another tuple

# a=(12,45,73,89,21,8,143)
# b=[]
# i=0
# while i<len(a):
#     if  a[i] % 2 != 0 :
#         b.append(a[i])
#     i +=1
# print(tuple(b))

# 6.wap to print all the odd digits in a tuple to another list.

# a = (12,45,32,6,78,2,135)
# b=[]
# i=0
# while i<len(a):
#     if a[i]% 2 !=0:
#         b.append(a[i])
#     i+=1
# print(b)

# 7.wap to extract all the alphabets in a tuple.

# a = ('arun','kri2s3','na$24522')
# b=[]
# i=0
# j=0
# while i<len(a):
#     while j<len(a[i]):
#         if 'A'<=a[i][j] <='Z' or 'a'<=a[i][j]<='z':
#             b.append(a[i][j])
#         j+=1
#     i+=1
# print(b)

# method 2

# a=('dwda',32,82.9,'adwa',"Aawda")
# b=[]
# i=0
# while i<len(a):
#     if isinstance(a[i],str):
#         b.append(a[i])
#     i+=1
# print(b)

# 8. wap to extract all the numbers in a tuple

# a = (32,'awdwaa',23.5,7+32j,'arunkrishna',42,6512312312)
# i=0
# while i<len(a):
#     if isinstance(a[i],(int,float)):
#         print(a[i])
#     i+=1

# 9. WAP to extract all the special characters in tuple

# a=('%#@@', '@$$##%^&*()_+=-',123,65,4,3)
# i=0
# while i<len(a):
#     if isinstance(a[i],str):
#         print(a[i])
#     i+=1

# method 2


# 10.wap to convert the al uppercase alphabets to lower case alphabets.

# a='AWDwdadaFHRohr'
# b=''

# i=0
# while i<len(a):
#     if 'A'<=a[i]<='Z':
#         b+=a[i].lower()
#     else:
#         b+=a[i].upper()
#     i+=1
# print(b)

# method 2

# a= 'adwdawaWDWGHDABDSNW'
# b=''
# i=0
# while i<len(a):
#     if 'A'<=a[i]<='Z':
#         c=ord(a[i])+32
#         b+=chr(c)
#     else:
#         b+=chr(ord(a[i])-32)
#     i+=1
# print(b)

# 12.wap to find the length of the tuple

# a =(12,54,23.54,'adsad')
# print(len(a))

# 13.wap to find the length of the tuple without using Len function.     doubt

# a =  (12,54,23.54,'adsad')
# count = 0
# i=0
# while i<10:
#     if a[i] !=None:
#         count+=1
#     i+=1
# print(f'the length of tuple is {count}')

# 14.wap to find the number of alphabets in a tuple.

# a= ('aw','ad',24,3,'a',56789,'dsds')
# aph = 0
# i=0
# while i < len(a):
#     if isinstance(a[i],str):
#         aph += len(a[i])
#     i+=1
# print('alphabets are ',aph)

# 15.wap to find the number of numbers in a tuple.

# a= (12,211,'ad','arunw','@$@!') 
# tnum=0
# i=0
# while i<len(a):
#     if isinstance(a[i],int):
#         tnum+=1
#     i+=1
# print("Number of integers in the Tuple : ",tnum)

# 16.wap to find the number of special characters in a tuple.      doubt

# a=(21,458,'$','arun')
# sn=0
# i=0
# while i<len(a):
#     if not 'A'<=str(a[i])<='Z' or 'a'<=str(a[i])<='z' or  '0'<=str(a[i])<='9':
#         sn+=1
#     i+=1
# print(sn)

# 17.wap to reverse a tuple.

# a=(12,47,98,356)
# print(tuple(reversed(a)))

# 18.wap to reverse a tuple w/o using slicing

# a=(12,47,98,356)
# rev=[]
# i=-1
# while i<len(a):
#     rev.append(a[i])
#     i-=1
# print(rev)

# sum=0
# while True:
#     b=int(input('enter a number'))
#     sum+=b
#     if b==0:
#         print(sum)


# wap to seperate the types of char from a string
# spl=''
# num=''
# uc=''
# lc=''
# a='adwasd42393#FFS'
# for i in a:
#     if i.isupper():
#         uc+=i
#     elif i.isnumeric():
#         num+=i
#     elif i.islower():
#         lc+=i
#     else:
#         spl+=i    
# print(uc)
# print(lc)
# print(num)
# print(spl)

# find the char in odd position and is uppercase

# a='ABFRYEJSNJD'

# for i in a:
#     if i.index() %2==1 and i.isupper():
#         print(i)
        
        
# wap to find length of string
# a='adawawdwad'
# b=0
# for i in a:
#     b+=1
# print(b)

# WAP to reverse a string

# a='fsawrhgdfaw'
# b=reversed(a)
# print(b)

#  WAP to take a list of username and check wheather the username and password are correct