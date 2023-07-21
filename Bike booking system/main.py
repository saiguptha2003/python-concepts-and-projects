from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QModelIndex
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('userportal.ui', self)
        self.button1 = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.button1.clicked.connect(self.buttonpressed)
        self.rd1 = self.findChild(QtWidgets.QLineEdit,'ridername')
        self.age1=self.findChild(QtWidgets.QLineEdit,'age')
        
        self.dil1=self.findChild(QtWidgets.QLineEdit,'dilicence')
        #self.idnum=self.findChild(QtWidgets.QLineEdit,'idnumberi')
        self.idr1=self.findChild(QtWidgets.QLineEdit,'idnumber')
        self.date1=self.findChild(QtWidgets.QDateTimeEdit,'dateTimeEdit')
        self.wantedbike1=self.findChild(QtWidgets.QLabel,'bikewanted')
        self.address1=self.findChild(QtWidgets.QTextEdit,'address')



        self.list=self.findChild(QtWidgets.QListView,'listView')
        self.model = QStandardItemModel()
        self.list.setModel(self.model)
        self.list.setObjectName("listView-1")
        values=open('bikelist.txt','r').readline().split(',')
        for i in values:
            self.model.appendRow(QStandardItem(i))
        self.show()
        self.list.clicked[QModelIndex].connect(self.onclicked)
        self.wantedbike1.setText("Select a bike")
    def onclicked(self,index):
        item=self.model.itemFromIndex(index)
        print(item.text())
        if(item.text().__eq__('Economy Class(800/day)')):
            self.wantedbike1.setText("800Rs")
        if(item.text().__eq__('Commerial Class(5000/day)')):
            self.wantedbike1.setText("5000Rs")
        if(item.text().__eq__('Sport Class(3000/day)')):
            self.wantedbike1.setText("3000Rs")
        if(item.text().__eq__('Emergency Class(400/hr)')):
            self.wantedbike1.setText("400Rs")
           
    def buttonpressed(self):
        ridername=self.rd1.text()
        age=self.age1.text()
        ide=self.idr1.text()
        dil=self.dil1.text()
        date=self.date1.text()   
        wantedbike=self.wantedbike1.text()
        addressi=self.address1.toPlainText()
        open('data.txt','w').write(f'{ridername},{age},{ide},{dil},{date},{wantedbike},{addressi}\n')
        self.window = userportal()
        self.window.show()


class userportal(QtWidgets.QMainWindow):
    def __init__(self):
        super(userportal, self).__init__()
        uic.loadUi('bookingportal.ui', self)
        self.ridername=self.findChild(QtWidgets.QLabel,'ridername')
        self.dil=self.findChild(QtWidgets.QLabel,'dilicence')
        self.date=self.findChild(QtWidgets.QLabel,'dateTimeEdit')
        self.wantedbike=self.findChild(QtWidgets.QLabel,'bikewanted')
        self.address=self.findChild(QtWidgets.QLabel,'address')
        self.cost=self.findChild(QtWidgets.QLabel,'cost')
        er=open('data.txt','r').readline()
        er=er.split(',')
        print(er)
        self.ridername.setText(er[0])
        self.dil.setText(er[3])
        self.wantedbike.setText(er[5])
        self.address.setText(er[6])
        self.cost.setText('1000RS')
        self.close=self.findChild(QtWidgets.QPushButton,'close')
        self.close.clicked.connect(self.close1)
        self.show()
    def close1(self):
        self.close()
        exit()

    
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()