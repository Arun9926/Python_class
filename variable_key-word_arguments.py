# def show_my_detail(name="guest",age=None,quali=None):
#     print("Name is : ",name)
#     print("age is : ",age)
#     print("Quali is : ",quali)
# show_my_detail("Arun",26,"B.E")    

#==========================================================
#double star (**) kwargs Data-type=dict
#==========================================================
# def show_my_detail(**n):
#     print(n)
#     print(type(n))
# show_my_detail(name="Arun",age=26,quali="B.E")    

# def show_my_detail(**n):
#     print(n)
#     print(type(n))
# x=eval(input("Enter any dict : "))        
# show_my_detail(**x)    

# x=10
# def add():
#     global x
#     print(x)
#     x=20
#     print(x)
# add()
# print(x)
x=10
def add():
    x=20
    print(globals()['x'])
    print(x)
add()
print(x)