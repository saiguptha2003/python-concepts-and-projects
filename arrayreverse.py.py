import numpy as np
import math
arr=np.array([1,2,3,4,5,6,7,8,9,10])
length=len(arr)
def find_index(data):
     lower=0
     upper=length-1
     index=0
     while lower<=upper:
          mid=math.ceil(lower+(upper-lower)/2)
          if arr[mid]==data:
               index=mid
               break
          else:
               if arr[mid]<data:
                    lower=mid+1
               else:
                    upper=mid-1 
     return index
loc=find_index(4)
print(loc)
