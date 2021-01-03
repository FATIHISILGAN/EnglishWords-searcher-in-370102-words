import sys

from PyQt5.QtWidgets import QLineEdit,QCompleter
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import json
liste=list()
class Main(QWidget):

  

    

    

    def __init__(self):

        
        super().__init__()
        f = open('words.json',) 
  

        data = json.load(f)

  

        for i in data.keys():
            liste.append(i)
             


           
        self.getItems()
        
    def getItems(self):
        lineEd=QLineEdit(self)
        lineEd.setGeometry(100,200,200,35)
        comp=QCompleter(liste)
        lineEd.setCompleter(comp)

        
        

        
    
        

app=QApplication(sys.argv)#Main

form1=Main()
form1.show()

sys.exit(app.exec_())




