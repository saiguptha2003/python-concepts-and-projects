def bubble_sort(arr):
     n=len(arr)
     for i in range(0,n):
          for j in range(0,n-i-1):
               if(arr[j]>arr[j+1]):
                    arr[j],arr[j+1]=arr[j+1],arr[j]
l=[95,440,43,21,42]
bubble_sort(l)
print(l)