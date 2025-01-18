# x=10
# y=10
# print(id(x))
# print(id(y))

# Python is a call by object refrence 

# Immutable Nature(same memory address)
#====================================================================
# Integer
# x=10
# y=10
# print(id(x),id(y))

# String
# x="arun"
# y="arun"
# print(id(x),id(y))

# Tuple
# x=(10,20,30,"arun")
# y=(10,20,30,"arun")
# print(id(x),id(y))

#Mutable Nature (Diffrent memory address)
#==================================================================
#List
# x=[10,20,30,"arun"]
# y=[10,20,30,"arun"]
# print(id(x),id(y))

#Dictionary
# d1={"name":"arun","age":"26"}
# d2={"name":"arun","age":"26"}
# print(id(d1),id(d2))

#Set
# s1={10,20,"arun",30}
# s2={10,20,"arun",30}
# print(id(s1),id(s2))

#frozonSet
# f1=frozenset({10,20,"arun",30})
# f2=frozenset({10,20,"arun",30})
# print(id(f1),id(f2))
