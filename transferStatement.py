#break -> exit from loop
#continue -> skip current iteration
#pass -> skip current block

# i=1
# while i<=10:
#     if i==6:
#         break
#     print(i)
#     i+=1
# print('hello')    


# i=1
# while i<=10:
#     if i==6:
#         i+=1
#         continue
#     print(i)
#     i=i+1
# print("hello")

# x=eval(input('enter value : '))
# print(x)
# print(type(x))
# for i in x:
#     print(i)



# *    
# **   
# ***
# ****
# *****
# n=5
# i=1
# while i<=n:
#     print(i*'*'+' '*(n-i))
#     i+=1

#--------------------------------------------------------------------------
#     *
#    **
#   ***
#  ****
# *****
# n=5
# i=1
# while i<=n:
#     print(' '*(n-i)+'*'*i)
#     i+=1

#--------------------------------------------------------------------------- 
# *        *
# **      **
# ***    ***
# ****  ****
# **********   
# n=5
# i=1
# while i<=n:
#     print(i*'*'+' '*(n-i)+' '*(n-i)+'*'*i)
#     i+=1
#--------------------------------------------------------------------------- 
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# n=5
# i=1
# while i<=n:
#     print(' '*(n-i)+' *'*i)
#     i+=1
 #-------------------------------------------------------------
# *****
# ****
# ***
# **
# *
n=1
i=5
while i>=n:
    print(i*'*'+' '*(n-i))
    i-=1
#---------------------------------------------------------------------
# *****
#  ****
#   ***
#    **
#     *
# n=5
# i=0
# while i<n:
#     print(' '*i+'*'*(n-i))
#     i+=1
#------------------------------------------------------------------------
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
# n=5
# i=0
# while i<n:
#     print(' '*i+' *'*(n-i))
#     i+=1    
#-------------------------------------------------------------------------

# *    
# **   
# ***  
# **** 
# *****
# ****
# ***
# **
# *
# n=5
# i=1
# while i<=n:
#     print(i*'*'+' '*(n-i))
#     i+=1

# n=1    
# i=4
# while i>=n:
#     print(i*'*'+' '*(n-i))
#     i-=1

#--------------------------------------------------------------------------
#     *
#    **
#   ***
#  ****
# *****
# ****
# ***
# **
# *
# n=5
# i=1
# while i<=n:
#     print(' '*(n-i)+'*'*i)
#     i+=1    
# n=0
# i=4
# while i>=n:
#     print(' '*(n-i)+'*'*i)
#     i-=1    
#--------------------------------------------------------------
# *
# **
# ***
# ****
# *****
#  ****
#   ***
#    **
#     *

# n=5
# i=1
# while i<=n:
#     print(i*'*')
#     i+=1    
# n=5
# i=1
# while i<=n:
#     print(' '*i+'*'*(n-i))
#     i+=1 

 #-----------------------------------------------------------------------
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
   
# n=5
# i=1
# while i<=n:
#     print(' '*(n-i)+' *'*i)
#     i+=1  
# n=5
# i=1
# while i<=n:
#     print(' '*i+' *'*(n-i))
#     i+=1       