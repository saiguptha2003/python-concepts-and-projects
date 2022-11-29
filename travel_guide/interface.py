import main as m
def display():
    print("--------Travel Company--------")
    print("1.Plan a Journey")
    print("2.Exit")
display()
comp=m.com()
print("enter the choice:",end="")
choice=int(input())
match choice:
     case 1:
          comp.journey()
          display()
     case 2:
          exit(0)
     case default:
          print("correct choice.....")
          display()



