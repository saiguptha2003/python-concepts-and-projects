class power():
     base=None
     power=None
     def __init__(self,b,p):
          self.base=b
          self.power=p
     def poweri(self):
          return self.base**self.power
b=int(input())
p=int(input())
s=power(b,p)
print(s.poweri())