class rectangle():
     __length=None
     __breadth=None
     def __init__(self,l,b):
          self.__breadth=b
          self.__length=l
     def area(self):
          print(self.__length*self.__breadth)
     def perimeter(self):
          print(2*(self.__length+self.__breadth))
l=int(input())
b=int(input())
f=rectangle(l,b)
f.area()
f.perimeter()