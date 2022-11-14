from studentdmsinterface import studentdetails
import os
print("\n__________SRM UNIVERSITY___________\n")
def makesearch(name):
     s2=studentdetails()
     match name:
          case 1:
               return s2.displayStundetbyName()
          case 2:
                s2.displayStudentbyRoll()
          case 3:
               return s2.displayStudentbyID()
          case 4:
               os.system('cls')
               pass
          case default:
               return "enter correct index....."

def search():
     i=1
     number=1
     while(number<4):
          print("     Search Operations")
          print("     1.search by name")
          print("     2.search by roll")
          print("     3.search by studentid")
          print("     4.Exit to main Menu")
          number=int(input("Enter the search option  :"))
          makesearch(number)

def makemarks(name):
     s2=studentdetails()
     match name:
          case 1:
               return s2.displayStudent_exam_marks_with_limit()
          case 2:
               return s2.displayStudent_exam_marks_failed()
          case 3:
               os.system('cls')
               pass
          case default:
               return "enter correct option......"

def marks():
     i=1
     number=1
     while(number<3):
          print("     Marks Operations")
          print("     1.limit wise result")
          print("     2.Failed Students")
          print("     3.Exit")
          number=int(input("Enter the opertion index :"))
          makemarks(number)

def makedelete(name):
     s2=studentdetails()
     match name:
          case 1:
               return s2.deleted_A_student()
          case 2:
               return s2.deleteAllStudent()
          case 3:
               os.system('cls')
               pass
          case default:
               return "enter correct option......"
     
def deletes():
     i=1
     number=1
     while(number<3):
          print("     Delete Operations")
          print("     1.Delete Perticular ")
          print("     2.Delete All Records ")
          print("     3.Exit")
          number=int(input("Enter the opertion  :"))
          makedelete(number)

def number_to_choose(choice):
     s1=studentdetails()
     match choice:
          case 1:
               return s1.input_detail()
          case 2:
               return  search()
          case 3:
               return marks()
          case 4:
               return deletes()
          case 5:
               return s1.exportDatatoXls()
          case 6:
               return s1.displayAllStudents()
          case 7:
               os.system('cls')
               return 0
               pass
          case default:
               print("valid choice")
number=1
while number<7:
     print("___DATA BASE OPERATIONS___\n")
     print("   1.INSERT STUDENT DATA")
     print("   2.SEARCH STUDENT")
     print("   3.MARKS")
     print("   4.REMOVE STUDENT")
     print("   5.EXPORT RECORDS")
     print("   6.DISPLAY ALL RECORDS")
     print("   7.EXIT\n")
     number=int(input("Enter the choice:"))
     number_to_choose(number)



