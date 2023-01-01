import numpy as np
import math as m
arr=np.array([1,2,3,4,5,6,7,8,9,10])
length=len(arr)
def find_item(data):
    lower=0
    upper=length-1
    mid=-1
    index=0
    while data!=arr[mid]:
        if arr[lower]==arr[upper]:
            break
        else:
            mid=m.ceil(lower+((upper-lower)/(arr[upper]-arr[lower]))*(data-arr[lower]))
            if arr[mid]==data:
                index=mid
            else:
                if arr[mid]<data:
                    lower=mid+1
                else :
                    upper=mid-1
    return index
loc=find_item(5)
print(loc)
                    
                
                
        
        
    