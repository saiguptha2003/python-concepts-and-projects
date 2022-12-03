def sum(num,i):
     if(num==0):
          return i
     else:
          return sum(num-1,i+num)
i=int(input())
print(sum(i,0))