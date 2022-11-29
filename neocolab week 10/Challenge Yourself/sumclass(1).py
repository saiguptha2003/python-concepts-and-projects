
from collections import OrderedDict
class sum():
     def sumofthree(self,arr, n):
          l=[]
          arr = list(dict.fromkeys(arr))
          arr=list(arr)
          arr=sorted(arr)
          n=len(arr)
          found = False
          for i in range(0, n-2):
               for j in range(i+1, n-1):
                    for k in range(j+1, n):
                         if (arr[i] + arr[j] + arr[k] == 0):
                              l.append([arr[i], arr[j], arr[k]])
          s=tuple(l)
          l=list(s)
          return l
s=[int(item) for item in input().split()]
n = len(s)
d=sum()
print(d.sumofthree(s, n))