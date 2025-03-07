# Permanet data storage
# Type of file 
# Text file - string data
# Binary file - list ,tuple, set ,dict
# csv file - key-value
# f=open('n2.txt','r')
# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.closed)
# print(f.readable())

f=open('n1.txt','a')
data=['Hi\n','Hello\n','Welcome\n']
f.writelines(data)
f.close()
