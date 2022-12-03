# 9.Write a Python program to print following matrix.
# 1 0 1 0
# 0 1 0 1
# 1 0 1 0
# 0 1 0 1
for i in range(1,5):
     if(i%2==0):
          for j in range(1,5):
               if(j%2==0):
                    print(1,end=" ")
               else:
                    print(0,end=" ")
     else:
          for j in range(1,5):
               if(j%2==0):
                    print(0,end=" ")
               else:
                    print(1,end=" ")
     print()