# str1 = 'Arun'
# print('n' in str1)


x=10
y=20
print(x is y)



x=10
print(id(x))
y=10
print(id(y))
print(x is y)



x=[10]
print(id(x))
y=[10]
print(id(y))
print(x is y)#false


x=[10]
y=[10]
print(x == y)#true


