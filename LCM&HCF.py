x=int(input("Enter num1 : "))
y=int(input("Enter num2 : "))
max_no=max(x,y)
while True:
    if max_no%x==0 and max_no%y==0:
        break   
    max_no=max_no+1 
print(f"{x} and {y} LCM is {max_no}")  