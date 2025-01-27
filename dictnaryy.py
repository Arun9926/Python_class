#  collection of key-value pair 
#  indexing not supported
#  slicing not supported
#  key must be aunique
#  value may be a duplicate
#  mutable in nature
#  represented in {} with comma(,) seperated element
#  syntex-->
#           dict={"key1":"valur","key2":"value","key3":"value"}


d1={"name":"Arun","age":26,"quals":"BE"}
#=========================================
#in-build function
#=========================================
# print(max(d1))
# print(min(d1))
# print(len(d1))
# print(type(d1))
# print(id(d1))


#=========================================
# in-build Methods function
#=========================================
# print(d1.clear())
# print(d1.copy())
# print(d1.fromkeys())
# print(d1.items())
# print(d1.keys())
# print(d1.pop())
# print(d1.popitem())
# print(d1.setdefault())
# print(d1.update())
# print(d1.values())

# l1=['name','email','contect']
# d2=dict.fromkeys(l1,100)
# print(d2)

# print(d1.get('name'))

# print(d1.items())
# print(d1.values())
# print(d1.keys())


# print(d1.popitem())
# print(d1)

# d1.setdefault('from','bhopal')
# print(d1)

d2={}
d1.update(d2)
print(d1)