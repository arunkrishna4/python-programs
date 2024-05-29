### WAP to find the Square of all the numbers from 1 to 10
##x = [i ** 2 for i in range(1, 11)]
##
### WAP to extract all the even numbers from 1 to 10
##res = [i for i in range(1, 11) if i % 2 == 0]
##
### WAP to get the square of all the even numbers from 1 to 10.
##res = [i**2 for i in range(1, 11) if i % 2 == 0]
##
### WAP to reverse the name if the length is odd else add as it is
##names = ['steve', 'bill', 'arun', 'sidharth', 'benjamin', 'adam', 'rajesh', 'tarini', 'mukesh', 'ramesh', 'suresh', 'mahesh', 'ayush','pratesh', 'lucky', 'unlucky', 'verylucky']
##
##res1 = [name if len(name) % 2 == 0 else name[::-1] for name in names]

a = [10, 20, 30, 40]
b = ['a', 'b', 'c', 'd', 'e']
res = {}
for key, value in zip(b, a):
    res[key] = value
x = {k:v for k, v in zip(b,a)}

#           OR

a=[10,20,30,40]
b=['a','b','c']
res ={}

if len(a)>len(b):
    a.pop()
else:
    b.pop    

i=0
j=0
while i<len(a):
    res[b[i]] = a[j]
    i+=1
    j+=1
    
print(res)




