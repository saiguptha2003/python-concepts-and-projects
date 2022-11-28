class country():
     name=None
     countryCode=None
     isdCode=None
     def __init__(self,name,cc,iscode):
          self.name=name
          self.countryCode=cc
          self.isdCode=iscode
     def printdata(self):
          print("Country Name:{}".format(self.name))
          print("Country Code:{}".format(self.countryCode))
          print("ISD Code:{}".format(self.isdCode))
i=input()
c=input()
cod=input()
csd=country(i,c,cod)
csd.printdata()