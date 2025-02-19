# block of reuseble of code

# def function_name(parameters):
#     "doc string"
#     function body
#     return

# function colled
# var=function_name(argument)

#positional arguments
# def add(x,y):
#     return x+y

# z=add(4,5)
# print(z)
#========================================================
#key-word arguments
# def add(x,y):
#     "this function is add two valus"
#     return x+y

# z=add(y=4,x=5)
# print(z)
# print(add.__doc__)
# print(dir(add))

# def fun(x=0,y=0):
#     p=x+y
#     print('hi')
#     return p
# a=fun(5)
# print(a)  

# def add(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# x=add(1,2,3,4,5)    
# print(x)    

# def add(*args):
#     sum=0
#     for i in args:
#         for j in i:
#             sum=sum+j
#         return sum
# p=eval(input('Enter any number : '))    
# x=add(p)    
# print(x)

#============================================================
# use single star(*) in argumenets to hold any type of values
#============================================================

# def add(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum    
# p=eval(input('Enter any number : '))    
# x=add(*p)    
# print(x)











#=========================================================
# map
#=========================================================

# def squar(x):
#     return x**2
# l1 = eval(input("Enter any numeric collection : "))
# res=map(squar,l1)
# print(list(res))


# def add(x):
#     if x%2==0:
#         return x+1
#     else:
#         return x+2
# l1 = eval(input("Enter any numeric collection : "))
# res=map(add,l1)
# print(list(res))


# def add(x,y,z):
#     return x+y+z
# l1 = eval(input("Enter any numeric collection : "))
# l2 = eval(input("Enter any numeric collection : "))
# l3 = eval(input("Enter any numeric collection : "))
# res=map(add,l1,l2,l3)
# print(list(res))


#====================================================
# Filter
#====================================================
# l1=[-1,2,3,-4,5,6,-7,8]
# def fun(x):
#     if x%2==0:
#         return x
# res=filter(fun,l1)
# print(list(res))    


# def fun(x):
#     if x%2!=0:
#         return x
# res=filter(fun,l1)
# print(list(res))  


# def fun(x):
#     if x>=0:
#         return x
# res=filter(fun,l1)
# print(list(res))  


# def fun(x):
#     if x<0:
#         return x
# res=filter(fun,l1)
# print(list(res))        


# def fun(x):
#     if x%2==0:
#         return 'even'
#     else:
#         return 'odd'
# res=map(fun,l1)
# print(list(res)) 


# s=['arun','aman','raj','jai','rb']
# def threeWord(x):
#     if len(x)<=3:
#         return x
# res=filter(threeWord,s)     
# print(list(res))   


#=================================================
# Reduce
#=================================================
import functools
l1=[2,15,6,18,10]
def my_max(x,y):
    if x>y:
        return x
    else:
        return y
res=functools.reduce(my_max,l1)
print("max=",res)

def my_min(x,y):
    if x<y:
        return x
    else:
        return y
res=functools.reduce(my_min,l1)
print("min=",res)


def my_sum(x,y):
    return x+y
res=functools.reduce(my_sum,l1)
print("sum=",res)