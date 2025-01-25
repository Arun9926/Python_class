# collection of objects
#            1.Homogeneous (same datatype)
#            2.Heterogeneous (different datatype)

# ordered collection
# indexing supported
# sliceing supported
# mutable in nature
# represented in [] with comma(,) sepreted objects.

# max(),sum(),min() same datatype par nikalta hai


# l1=[10,10.5,"Arun",2,4,8]
#============================================
#python functions
#============================================
# print(len(l1))
# print(id(l1))
# print(type(l1))

#=============================================
#List methods
#=============================================
# print(l1.append())#add one object at last position
# print(l1.sort())#arrenge assending form
# print(l1.extend())#add multiple object in last position
# print(l1.remove())#remove one object from required position 
# print(l1.reverse())#to arrenge in reverse order
# print(l1.clear())# remove all object from list
# print(l1.pop())#remove one object from last position 
# print(l1.insert())#add one object from required position
# print(l1.copy())# create another object with same content
# print(l1.count())# frequeny
# print(l1.index())# object position

# l1=[10,20,20.5,2,8,6,1]
# l1.sort()
# print(l1)

# l1=[10,20,20.5,2,8,6,1]
# l1.reverse()
# print(l1)

# l1=[10,20,20.5,2,8,6,1]
# l1.sort(reverse=True)
# print(l1)


# l1=[10,20,20.5,2,8,6,1]
# l1.pop()
# print(l1)


# l1=[10,20,20.5,2,8,6,1]
# l1.remove(20.5)
# print(l1)



# l1=[10,20,20.5,2,8,6,1]
# l1.clear()
# print(l1)


# l1=[10,20,20.5,2,8,6,1]
# l2=l1.copy()
# print(l1)
# print(l2)
# print(id(l1))
# print(id(l2))


# l1=[10,20,20.5,2,8,6,10]
# print(l1.count(10))


l1=[10,20,20.5,2,8,6,10]
print(l1.index(1,2))