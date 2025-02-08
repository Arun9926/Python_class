# while True:
#     print("1. Add\n 2. Sub\n 3. Multi\n 4. Div\n 5.Off")
#     n=int(input("Enter your choise : "))
#     if n==1:
#         x=int(input("Enter num1 : "))
#         y=int(input("Enter num2 : "))
#         z=x+y
#         print(f"{x}+{y}={z}")
#     elif n==2:
#         x=int(input("Enter num1 : "))
#         y=int(input("Enter num2 : "))
#         z=x-y
#         print(f"{x}-{y}={z}")
#     elif n==3:
#         x=int(input("Enter num1 : "))
#         y=int(input("Enter num2 : "))
#         z=x*y
#         print(f"{x}*{y}={z}")
#     elif n==4:
#         x=int(input("Enter num1 : "))
#         y=int(input("Enter num2 : "))
#         z=x//y
#         print(f"{x}//{y}={z}")
#     elif n==5:
#         break
#     else:
#         print("Enetr valid input")
#==========================================================================
while True:
    print("1. Add\n2. Sub\n3. Multi\n4. Div\n5.Off")
    n=int(input("Enter your choise : "))
    p=(1,2,3,4)
    if n in p:
        x=int(input("Enter num1 : "))
        y=int(input("Enter num2 : "))
        if n==1:
            z=x+y
            print(f"{x}+{y}={z}")
        elif n==2:
            z=x-y
            print(f"{x}-{y}={z}")
        elif n==3:
            z=x*y
            print(f"{x}*{y}={z}")
        elif n==4:
            z=x//y
            print(f"{x}//{y}={z}")
    elif n==5:
        break
    else:
        print("Enetr valid input")