class calculator():
     a = None
     b = None
     def __init__(self,a,b):
          self.a=a
          self.b=b
     def add(self):
          print(self.a+self.b)
     def sub(self):
          print(self.a-self.b)
     def mul(self):
          print(self.a*self.b)
     def div(self):
          print(self.a/self.b)
a=int(input())
b=int(input())
ff=int(input())
s=calculator(a,b)
if(ff==1):
    s.add()
elif(ff==2):
    s.sub()
elif(ff==3):
    s.mul()
elif(ff==4):
    s.div()
elif(ff==5):
    print("Invalid choice")