# a=int(input("Enter 1st num : "))
# b=int(input("Enter 2st num : "))
# c=int(input("Enter 3st num : "))
# if(a>b and a>c):
#     print('a is greater',a)
# else:
#     if(b>a and b>c):
#         print('b is greater',b)
#     else:
#         print('c is greater',c)


a=int(input("Enter 1st num : "))
b=int(input("Enter 2st num : "))
c=int(input("Enter 3st num : "))
if(a>b and a>c):
    print('a is greater',a)
elif(b>a and b>c):
    print('b is greater',b)
elif(c>a and c>b):
    print('c is greater',c)
elif(a==b):
    print(f"a and b are equal")
elif(b==c):
    print(f"b and c are equal")
elif(c==a):
    print(f"c and a are equal")