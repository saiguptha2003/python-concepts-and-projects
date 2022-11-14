import mysql.connector
import pandas as p
from texttable import Texttable
from prettytable import PrettyTable
from pymysql import *
import xlwt
import pandas.io.sql as sql


mydb = mysql.connector.connect(
    host="enter your data base host",
    user="enter your user name in my sql",
    password="enter your password of sql workbench server",
    database="enter your data base "
    #create a table as studentdetail in database
    #import the given csv file or data.xls file to studentdetail table
    #click here to know how to import csv or xls file to database 
    #make sure that columns names are same as given in the bellow tuple
    #aur,studentname,roll,email,codechef,marks,state,interest
    #create same columns 
    https://www.sqlshack.com/importing-and-working-with-csv-files-in-sql-server/
    https://blog.skyvia.com/3-easy-ways-to-import-csv-file-to-sql-server/
    https://www.c-sharpcorner.com/article/import-csv-file-into-sql-server-using-sql-server-management-studio/

)
d = mydb.cursor()
class studentdetails:
    __name = None
    __roll = None
    __aur = None
    __state = None
    __interest = None
    __codechef = None
    __marks = None
    __email = None

    def input_detail(self):
        print("Enter the New Student details")
        print("-----------------------------")
        n = input("Student Name :")
        self.__name = n
        rol = int(input("Roll Number in range(900,1500):"))
        self.__roll = rol
        print()
        stat = input("State:")
        self.__state = stat
        print()
        rank = int(input("All University Rank (0,10000):"))
        self.__aur = rank
        print()
        marks = int(input("Total Marks out of 400 :"))
        if (marks > 400):
            print("Please enter the marks within range:")
            marks = int(input("Total Marks out of 400 :"))
        self.__marks = marks
        print()
        inter = input("Interest Feild :")
        self.__interest = inter
        print()
        code = int(input("Codechef Ranking : "))
        self.__codechef = code
        print()
        email = input("Enter Email Address :")
        self.__email = email
        print()
        d.execute("use studentdb")
        query = "insert into studentdetail(aur,studentname,roll,email,codechef,marks,state,interest) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (self.__aur, self.__name, self.__roll, self.__email,
               self.__codechef, self.__marks, self.__state, self.__interest)
        d.execute(query, val)
        mydb.commit()
        print()
        print(d.rowcount, "record inserted.")
        print("Total Records:", d.lastrowid)


    def displayAllStudents(self):
        d.execute("select * from studentdetail")
        mydata = d.fetchall()
        h=['university rank', 'name', 'roll', 'email','codechef rank', 'marks', 'state', 'interest', 'id']
        table=PrettyTable(h)
        for x in mydata:
            table.add_row(x)
        print(table)

            


    def displaystudent(self,query,namei):
        d.execute(query,namei)
        sr = ('university rank', 'name', 'roll', 'email','codechef rank', 'marks', 'state', 'interest', 'id')
        s=d.fetchone()
        t=0
        if s ==None:
         print("\nno record found.....")
         return 0
        print("\n.......details........")
        for i in  s :
            print(sr[t],"=",i,end="\n")
            t=t+1
    def displayStudentsByConstraints(self,query,name):
        d.execute(query,name)
        sr=d.fetchall()
        h=['university rank', 'name', 'roll', 'email','codechef rank', 'marks', 'state', 'interest', 'id']
        table=PrettyTable(h)
        for x in sr:
            table.add_row(x)
        print(table)
        print("total students above ",name[0]," count is ",len(sr))


    def displayStundetbyName(self):
      name=input("Enter name of the student :")
      query="select * from studentdetail where studentname= %s"
      names=(name,)
      self.displaystudent(query,names)

    def displayStudentbyRoll(self):
        rolli=int(input("Enter Roll number of the student :"))
        query="select * from studentdetail where roll=%s"
        names=(rolli,)
        self.displaystudent(query,names)
    
    def displayStudentbyID(self):
        id=int(input("Enter Student ID :"))
        query="select * from studentdetail where id=%s order by %s"
        name=(id,id,)
        self.displaystudent(query,name)

    def displayStudents_who_Intrested_in(self):
        interestin=input("Get Interested Students in  : ")
        query="select * from studentdetail where interest=%s order by id"
        name=(interestin,)
        self.displayStudentsByConstraints(query,name)

    def displayStudent_exam_marks_with_limit(self):
        print("\nEnter the lower limit marks to get students")
        print("-------------------------------------------")
        uplimit=int(input("Upper Limit :"))
        print("table of students above ",uplimit,"\n")
        query="select id,studentname,roll,marks from studentdetail where marks>= %s order by marks desc"
        name=(uplimit,)
        d.execute(query,name)
        h=d.fetchall()
        head=["id","name","roll","marks"]
        table=PrettyTable(head)
        for x in h:
            table.add_row(x)
        print(table)
        print("total students above ",name[0]," count is ",len(h))

    def displayStudent_exam_marks_failed(self):
        print("\nFail Marks is 150")
        print("-------------------")
        print("Failed Students in Sem : ")
        d.execute("select id,studentname,roll,marks from studentdetail where marks < 150 order by marks ")
        h=d.fetchall()
        head=["id","name","roll","marks"]
        table=PrettyTable(head)
        for x in h:
            table.add_row(x)
        print(table)
        print("total students failed in sem count is ",len(h))

    def deleted_A_student(self):
        print()
        name=input("Enter the student name to delete:")
        confirm=input("COMFIRM OR NOT (yes or no) :")
        if(confirm=='yes' or 'YES'):
            w="select * from studentdetail where studentname=%s"
            p="delete from studentdetail where studentname=%s"
            names=[name,]
            d.execute(w,names)
            s=d.fetchone()
            if s is None:
                print("record not deleted......")
                return
            head = ['university rank', 'name', 'roll', 'email','codechef rank', 'marks', 'state', 'interest', 'id']
            print(s)
            table=PrettyTable(head)
            table.add_row(s)
            d.execute(p,names)
            mydb.commit()
            print()
            print(d.rowcount, "record(s) deleted")
        else:
            pass
    def deleteAllStudent(self):
        confirm=input("COMFIRM OR NOT (yes or no) :")
        if(confirm=='yes' or 'YES'):
            p="delete from studentdetail"
            w="select * from studentdetail"
            d.execute(p)
            mydb.commit()
            d.execute(w)
            s=d.fetchall()
            if s is None:
                print("Deleted all records........")
                print()
                print("total records present is ",d.rowcount)
            else:
                print("records not deleted........")
        else:
           pass

    def exportDatatoXls(self):
        con = connect(user="root", password="Pandusai@2003",
        host="localhost", database="studentdb")
        print("Exporting data from sql database")
        name=input("Enter the file name to be created (file name with .xls extension) :")
        d = sql.read_sql('select * from studentdetail', con)
        print(d)
        d.to_excel(name)
        print("file created check in same folder file name as  ",name)
