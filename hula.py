#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import ( QMainWindow, QApplication, QPushButton,
QWidget, QAction, QTabWidget,QVBoxLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 Tab Example')
        self.setGeometry(100, 100, 640, 300)
        self.setCentralWidget(MyTabWidget(self))
        self.show()
 
class MyTabWidget(QTabWidget):
 
    def __init__(self, parent):
        super(QTabWidget, self).__init__(parent)
 
        # Enable the ability to move tabs and reorganize them, as well
        # as close them. Setting tabs as closable displays a close button
        # on each tab.
        #
        self.setTabsClosable(True)
        self.setMovable(True)
 
        # Create tabs in tab container
        #
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
 
        # Add tabs
        #
        self.addTab(self.tab1,"Tab 1")
        self.addTab(self.tab2,"Tab 2")
        self.addTab(self.tab3,"Long Tab 3")
        self.addTab(self.tab4,"Longer Tab 4")
        self.addTab(self.tab5,"Longest Tab 5")
        self.currentChanged.connect(self.tabSelected)
        self.tabCloseRequested.connect(self.closeRequest)
 
        # Add test content to a few tabs
        #
        self.tab1.setLayout(QVBoxLayout(self))
        self.tab2.setLayout(QVBoxLayout(self))
        self.pushButton1 = QPushButton("PyQt5 Button 1")
        self.tab1.layout().addWidget(self.pushButton1)
        self.pushButton2 = QPushButton("PyQt5 Button 2")
        self.tab2.layout().addWidget(self.pushButton2)
 
    #@pyqtSlot()
    def tabSelected(self):
        print("Selected tab {0}".format(self.currentIndex()+1))
 
    def closeRequest(self):
        print("Tab close request on tab {0}".format(self.currentIndex()+1))
        if self.count() > 1:
            self.removeTab(self.currentIndex())
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())