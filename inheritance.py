# 1. single inheritance  
# class Parent:
#     x=10
#     def home(self):
#         print("parent home")
# class Child(Parent):
#     y=10
#     def car(self):
#         print("child car")
# obj = Child()
# print(Child.x)
# obj.home()
# obj.car()

# // method overriding (use super method)
# class Parent:
#     x=10
#     def home(self):
#         print("parent home")
# class Child(Parent):
#     y=10
#     def home(self):
#         super().home()
#         print("child car")
# obj = Child()
# print(Child.x)
# obj.home()


#===============================================================
#2. multiple inheritance
# class Parent1:
#     def home(self):
#         print('parent1 home')
# class Parent2:
#     def home(self):
#         print('parent2 home')
# class Child(Parent1,Parent2):
#     def car(self):
#         print('child car')
# obj=Child()
# obj.home()

#==================================================================
#3. Multi lavle inheritance
class Grand_parent:
    def home(self):
        print('Grand parent home')
class Parent(Grand_parent):
    def car(self):
        print('parent car')
class Child(Parent):
    def car2(self):
        print('child car2')
obj=Child()
obj.home()
obj.car()
obj.car2()