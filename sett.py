# collection of unique elements
# unordered collection
# indexing not supported
# alicing not supported 
# mutable in nature
# reprented in {} with comma (,) seperated elements

# mySet={'Arun',10,20,'Patel',30,40,'Aman'}
# print(mySet)
# print(type(mySet))

#=======================================================
# functions in set
#=======================================================
# s1={'Arun','patel','aman','patel'}
# s2={10,20,30,40,50}
# print(max(s1),max(s2))
# print(min(s1),min(s2))
# print(type(s1),type(s2))
# print(id(s1),id(s2))
# print(len(s1),len(s2))
# print(sum(s2))

#======================================================
# methods in set
#======================================================
# s1.clear()
# print(s1)
# s1.add(50) #add single element
# print(s1)
# l1=[1,2,3,4,5] # add multiple element
# s1.update(l1)
# print(s1)

# s1.pop()
# print(s1)
# s2.remove(50)
# print(s2)
# s2.discard(50)
# print(s2)
# s2.discard(50)
# print(s2)

# a={1,2,3,4,5}
# b={7,3,6,5}
# print(a.union(b))
# print(a)
# print(b)
a={1,2,3,4,5}
b={7,3,6,5}
print(a.intersection(b))
print(a)
print(b)
a.intersection_update(b)
print(a)
