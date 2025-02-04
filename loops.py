# x=int(input("Enter number : "))
# i=1
# while i<=x:
#     print(i,end=',')
#     i+=1
    
# print(i,x)

# n=int(input("Enter number : "))
# i=1
# while i<=n:
#     x=2*i
#     # print(f'2 x {i} = {x}')
#     print(x)
#     i+=1


# n=int(input("Enter number : "))
# i=1
# while i<=n:
#     if i<n:
#         print(i,end=',')
#     else:
#         print(i)    
#     i+=1    
# print('Hello')    

#=========================================================
# Armstring Number
#=========================================================
# n=int(input("Enter number : "))
# x=y=n
# digit=0
# sum=0
# while n>0:
#     digit=digit+1
#     n=n//10    
# sum=0
# while y>0:
#     last_digit=y%10
#     sum=sum+last_digit**digit
#     y//=10
# print(sum)    
# if(x==sum):
#     print(f'{x} is armstong number')
# else:
#     print(f'{x} is not armstong number')


#=========================================================
# palindrom Number
#=========================================================    
n=int(input("Enter number : "))
y=n
rev_digit=0
while n>0:
    x=n%10
    rev_digit=rev_digit*10+x
    n//=10
print(rev_digit)
if(y==rev_digit):
    print(f'{rev_digit} is a palindrom')    
else:
    print(f'{rev_digit} is not a palindrom')