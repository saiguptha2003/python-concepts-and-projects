class circle():
     radius=None
     def __init__(self,s):
          self.radius=s
     def area(self):
          print(3.14*(self.radius**2))
     def perimeter(self):
          print(2*3.14*self.radius)
r=int(input())
d=circle(r)
d.area()
d.perimeter()