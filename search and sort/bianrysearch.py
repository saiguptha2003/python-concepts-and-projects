def bianry_search(arr, low,high,x):
     if(low<=high):
          mid=(low+high)//2
          if(arr[mid]==x):
               return mid
          elif(arr[mid]>x):
               return bianry_search(arr,low,mid+1,x)
          else:
               return bianry_search(arr,mid+1,high,x)
     else:
          return -1
l=[1,2,3,4,5,6,7]
x=7
print(bianry_search(l,0,len(l)-1,x))