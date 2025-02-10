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
def add(x,y):
    "this function is add two valus"
    return x+y

z=add(y=4,x=5)
print(z)
print(add.__doc__)
print(dir(add))