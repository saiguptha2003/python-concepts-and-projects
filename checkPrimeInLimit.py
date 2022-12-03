def checkprime(num):
     if(num==0 or num==1):
          return False
     for i in range(2,num):
          if(num%2==0):
               return False
     return True
n=int(input())
limit=int(input())
for i in range(1,limit):
     if(checkprime(i)==True):
          print(i)
