# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 21:08:07 2016

@author: tanviranjan
"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():   
   app = QApplication(sys.argv)
   win = QDialog()
   b1 = QPushButton(win)
   b1.setText("Merge reactions")
   b1.move(50,20)
   b1.resize(200,30)
   b1.clicked.connect(b1_clicked)

   b2 = QPushButton(win)
   b2.setText("Merge compartments")
   b2.move(50,50)
   b2.resize(200,30)
   QObject.connect(b2,SIGNAL("clicked()"),b2_clicked)
   
   #win = QWidget()
	
   e1 = QLineEdit()
   e1.setValidator(QIntValidator())
   e1.setMaxLength(4)
   e1.setAlignment(Qt.AlignRight)
   e1.setFont(QFont("Arial",20))
	
   e2 = QLineEdit()
   e2.setValidator(QDoubleValidator(0.99,99.99,2))
	
   flo = QFormLayout()
   flo.addRow("Cell Type", e1)
   #flo.addRow("Double validator",e2)
	
   '''e3 = QLineEdit()
   e3.setInputMask('+99_9999_999999')
   flo.addRow("Input Mask",e3)'''
	
   '''e4 = QLineEdit()
   e4.textChanged.connect(textchanged)
   flo.addRow("Text changed",e4)'''
	
   '''e5 = QLineEdit()
   e5.setEchoMode(QLineEdit.Password)
   flo.addRow("Password",e5)'''
	
   '''e6 = QLineEdit("Hello Python")
   e6.setReadOnly(True)
   flo.addRow("Read Only",e6)'''
	
   #e5.editingFinished.connect(enterPress)
   win.setLayout(flo)
   win.setWindowTitle("Automatic layout into groups")
   win.show()
	
   sys.exit(app.exec_())

def textchanged(text):
   print ("contents of text box: "+text)
	
def enterPress():
   print ("edited")


def b1_clicked():
    mergeForEachCell.py
   #print ("Button 1 clicked")

def b2_clicked():
   mergeGroupInfo.py

if __name__ == '__main__':
   window()