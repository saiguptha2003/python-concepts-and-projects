class Reverse():
     s=None
     def __init__(self,s):
          self.s=s
     def Reverses(self):
          self.s=self.s[::-1]
          print(self.s)
s=input()
f=Reverse(s)
f.Reverses()