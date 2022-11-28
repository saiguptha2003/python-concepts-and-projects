class employee():   
     emp1=None
     emp2=None
     def __init__(self,n,f):
          self.emp1=n
          self.emp2=f
     def email(self):
        print(self.emp1.lower()+'.'+self.emp2.lower()+"@company.com")
n=input()
s=input()
e=employee(n,s)
e.email()
     