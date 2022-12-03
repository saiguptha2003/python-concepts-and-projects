def feb(n):
     if(n<=1):
          return n
     else:
          return feb(n-1)+feb(n-2)
n=111
for i in range(n):
     pass
print(feb(i))