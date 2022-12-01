from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class UI(QMainWindow):
    def init(self):
        super(UI, self).init()

        uic.loadUi("tugas1.ui", self)

        #definisi widget
        self.button = self.findChild(QPushButton, "btnInsert")
        self.label = self.findChild(QLabel, "img1")
        self.button.clicked.connect(self.clicker)
        self.show()

    def clicker(self):
        fname = QFileDialog.getOpenFileName(self, "Insert Gambar", "/home/ikantongkol/Downloads", "All File (*);; PNG File (*png)", "Jpg File (*jpg)", )

        #Buka Gambar
        self.pixmap = QPixmap(fname[0])
        self.label.setPixmap(self.pixmap)

app = QApplication(sys.argv)
UIWindow = UI()
app.exec()
