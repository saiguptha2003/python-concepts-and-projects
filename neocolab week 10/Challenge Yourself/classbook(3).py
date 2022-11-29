class book():
     __title=None
     __author=None
     def get_title(self):
          self.__title=input()
          return("Title: "+self.__title)
     def get__author(self):
          self.__author=input()
          return ("Author: "+self.__author)
s=book()
print(s.get_title())
print(s.get__author())