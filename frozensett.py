# collection of unique element
# unordered 
# indexing not suppoeted
# slicing not supported
# immutable in nature

# s='Arun'
# l=[10,20,30,40,50]
# t=(10,20,30,40,50)
# d={'Arun','patel','aman'}
# s1={'arun','aman','milan'}
# x=frozenset(s)
# print(x)
# print(type(x))

a={2,4,6,8}
b={1,3,5,7,6,8}
x=frozenset(a)
y=frozenset(b)
# print(x.union(y))
# print(x.intersection(y))
# print(x.difference(y))
# print(x.symmetric_difference(y))


print(x.isdisjoint(y)) #common elements are present that's by output is false
print(x.issubset(y)) # x ke sare element y main present hai
print(x.issuperset(y)) 

