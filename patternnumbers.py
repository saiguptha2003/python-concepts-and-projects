# 8. Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n=9
for i in range(1,10):
     if(i<=(n/2)+1):
          for j in range(1,i+1):
               print("*",end=" ")
     else:
          for j in range(1,n-i+2):
               print("*",end=" ")
     print()
     