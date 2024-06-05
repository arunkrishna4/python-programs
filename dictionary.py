# WAP to make the list into dict keep the key as the 'list item' and values as 'length of key' 

# a =['banana','mango','apple','pear','cherry']
# res={}
# i=0
# while i<len(a):
#     res[a[i]] = len(a[i])
#     i+=1
# print(res)


# WAP to make the list into dict keep the key as the list item and values as (length of key , reverse of key)

# a =['banana','mango','apple','pear','cherry']
# res={}
# i=0
# while i<len(a):
#     res[a[i]] = (len(a[i]),a[i][::-1])
#     i+=1
# print(res)

# WAP  to group the words wrt length.

# a =['banana','mango','apple','pear','cherry']
# res ={}
# i=0
# while i<len(a):
#     if len(a[i]) not in res:
#         res[len(a[i])]=[a[i],]
#     else:
#         res[len(a[i])] += [a[i]]
#     i+=1
# print(res)

# WAP to group the words wrt the first letter
# a=input( "Enter the words :")
# b=a.split()

# res={}
# i=0
# while i<len(b):#0<2
#     if b[i][0] not in res:# if b[0][0] - a not in res 
#         res[b[i][0]]=[b[i]]
#     else:
#         res[b[i][0]]+=[b[i]]#{'a':'arun'}
# print(res)

#default dict
# from collections import defaultdict
# a =['banana','mango','apple','pear','cherry']
# res = defaultdict(list)
# i=0
# while i<len(res):
#    res[len(a[i])] += [a[i]]
#    i+=1

#WAP to 

# from collections import defaultdict
# a =['banana','mango','apple','pear','cherry','pear']
# res=defaultdict(int)
# i=0
# while i<len(res):
#     res[a[i]] += 1
#     i+=1


#method 2
# a =['banana','mango','apple','pear','cherry','pear','apple','pear','apple']
# res={}
# j=0
# i=0
# while i<len(a):
#     if a[i] in res:
        
#         res[a[i]] =  j
#         j+=1
        
#     else:
#         res[a[i]] = 1
        
#     i+=1

# print(res)

#WAP To count the number of char in a string and show the output with that number

# a = 'aaavvawwasa'

# A=a.count('a')
# V = a.count('v')
# W = a.count('w')
# S = a.count('s')

# print(f'a{A}v{V}w{W}s{S}')

#method 2

# a = 'aaavvawwasa'
# res=''
# i=0
# while i<len(a):
#     if a[i] not in res:
#         res+=a[i]+str(a.count(a[i]))
#     i+=1
# print(res)


# users = [{'un':'arun','pw':'krishna'},{'un':'maha','pw':'boa'},{'un':'jinga','pw':'dinga'}]

# username=input("Enter username : ")
# if username in users['un']:
#     password=input("Enter password :")
# else:
#     print('invalid username')
    