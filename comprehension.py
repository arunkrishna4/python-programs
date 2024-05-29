# WAP to find the Square of all the numbers from 1 to 10
# x = [i ** 2 for i in range(1, 11)]

##
### WAP to extract all the even numbers from 1 to 10
# res = [i for i in range(1, 11) if i % 2 == 0]

##
### WAP to get the square of all the even numbers from 1 to 10.
##res = [i**2 for i in range(1, 11) if i % 2 == 0]
##
### WAP to reverse the name if the length is odd else add as it is
# names = ['steve', 'bill', 'arun', 'sidharth', 'benjamin', 'adam', 'rajesh', 'tarini', 'mukesh', 'ramesh', 'suresh', 'mahesh', 'ayush','pratesh', 'lucky', 'unlucky', 'verylucky']
##
# res1 = [name if len(name) % 2 == 0 else name[::-1] for name in names]
# print(res1)
##
##
##
##
##
##

a = [10, 20, 30, 40]
b = ['a', 'b', 'c', 'd', 'e']
# res = {}
# for key, value in zip(b, a):
#     res[key] = value

# print(res)

x = {k:v for k, v in zip(a,b)}
print(x)




