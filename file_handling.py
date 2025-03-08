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
#==============================================================
# Write mode
#==============================================================
f=open('n1.txt','a')
data=['Hi\n','Hello\n','Welcome\n']
f.writelines(data)
f.close()
#==============================================================
#  Read mode // defalut mode is read
#==============================================================
# 1.read()
# 2.read(n)
# 3.readline() //single line data
# 4.readlines() //multi lines of data
#--------------------------------------------------------------
# f=open('n1.txt','r')
# data=f.read()
# print(data)
#--------------------------------------------------------------
# f=open('n1.txt','r')
# data=f.read(5)
# print(data)
# print(f.tell()) #tell method give a curser current position
#--------------------------------------------------------------
# f=open('n1.txt','r')
# data=f.readline()
# print(data)
#--------------------------------------------------------------
# f=open('n1.txt','r')
# data=f.readlines()
# print(data)
#=============================================================
# tell() method give a curser current position
# seek() method use to movement our curser
# seek(where we move, from move)
#=============================================================
# f=open('n.txt','x+')
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f=open('n.txt','a+')
# print(f.readable())
# print(f.writable())
# print(f.closed)



#=============================================================
# Binary File 
#=============================================================
# 1. Emage/Audio/Video (Byte-stream)
# text-data to byte code (picking(serialzation))
import pickle
# f=open('first.dat','ab')
# data=[10,20,30,'Arun']
# pickle.dump(data,f)
# f.close()
#-------------------------------------------------------------
f=open('first.dat','rb')
data=pickle.load(f)
print(data)