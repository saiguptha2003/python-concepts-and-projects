def linear_search(arr,x):
     for i in range(0,len(arr)):
          if(arr[i]==x):
               return i
     return -1
listr=[1,2,3,401,43]
x=401
print(linear_search(listr,x))