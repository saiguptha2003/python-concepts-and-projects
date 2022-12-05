def selection_sort(arr):
     for  i in range(0,len(arr)):
          mid=i
          for j in range(i+1,len(arr)):
               if(arr[j]>arr[mid]):
                    mid=j
          arr[i],arr[mid]=arr[mid],arr[i]
arr=[-2, 45, 0, 11, -9,88,-97,-202,747]
selection_sort(arr)
print(arr)
          
               