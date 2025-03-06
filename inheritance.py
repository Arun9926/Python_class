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
# class Grand_parent:
#     def home(self):
#         print('Grand parent home')
# class Parent(Grand_parent):
#     def car(self):
#         print('parent car')
# class Child(Parent):
#     def car2(self):
#         print('child car2')
# obj=Child()
# obj.home()
# obj.car()
# obj.car2()

#=================================================================
#4. Herarichical inheritance
# class Parent:
#     def home(self):
#         print("parent class")
# class Child1(Parent):
#     def home1(self):
#         print("child1 class")
# class Child2(Parent):
#     def home2(self):
#         print("child2 class")
# obj = Child1()
# obj.home()
# obj1 = Child2()
# obj1.home()


class Parent:
    def home(self):
        print("parent class")
class Child1(Parent):
    def home(self):
        # print("child1 class")
        super().home()
class Child2(Parent):
    def home(self):
        print("child2 class")
obj = Child1()
obj.home()
obj1 = Child2()
obj1.home()


#=====================================================================
# 5.Hybrid inheritance
# class Parent:
#     def home(self):
#         print("parent class")
# class Child1(Parent):
#     def home(self):
#         print("child1 class")
# class Child2(Parent):
#     def home(self):
#         print("child2 class")
# class Child3(Child1,Child2):
#     def new(self):
#         print("child3 class")
# obj = Child3()
# obj.home()
# print(Child3.__mro__)
