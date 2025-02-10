# x=int(input("Enter num1 : "))
# y=int(input("Enter num2 : "))
# max_no=max(x,y)
# while True:
#     if max_no%x==0 and max_no%y==0:
#         break   
#     max_no=max_no+1 
# print(f"{x} and {y} LCM is {max_no}")  


x=6
y=8
z=20
hcf=1
min_no=min(x,y,z)
while min_no>0:
    if (x%min_no==0 and y%min_no==0 and z%min_no):
        hcf=hcf*min_no
        break
    min_no-=1
print("HCF is : ",hcf)        

