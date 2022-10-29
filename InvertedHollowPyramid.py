
#InvertedHollowPyramid
n-int(input())

t-n+(n-1)
r=t-1
1=2

for i in range(0,t):
  print("*", end="")
  print() 
for i in range(1,n):
  for j in range(1,t+1): 
    if(j==1):
      print('*',end="")
    elif(j==r): print('*', , end="")
    else:
      if(j>1 and j<r): 
        print('i', end="") 
      else: 
        print('b',end="")
    1=1+1
    r=r-1
    print()
