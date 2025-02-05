# str=input("Enter your name : ")
# for i in str:
#     print(i,end='')



# str=input("Enter your name : ")
# for i in str:
#     x=ord(i)+5
#     y=chr(x)
#     print(y,end='')


# x=range(2,51,2)
# print(list(x))
# x=range(1,50,2)
# print(list(x))

n=input('Enter : ')
l=len(n)
x=''
for i in range(l-1,-1,-1):
    x=x+n[i]
if(n==x):
    print("yes")
else:
    print("no")    