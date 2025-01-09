from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from QT_Designer.Columnas_filas import Ui_Col_fil
import pandas as pd
from PyQt6.QtCore import pyqtSignal

class Col_fil(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, archivo, hoja):
        super().__init__()
        self.archivo = archivo
        self.hoja = hoja
        self.ui = Ui_Col_fil()
        self.ui.setupUi(self)
        self.df = pd.read_excel(self.archivo , sheet_name= self.hoja)

        self.col , self.ind = self.mod()

        self.ui.lineEdit_3.hide()
        self.ui.Box_fil.hide()

        self.ui.R_si.toggled.connect(self.mostrar)
        self.ui.R_no.toggled.connect(self.esconder)

        self.ui.pushButton.clicked.connect(self.preview)
        self.ui.pushButton_2.clicked.connect(self.conti)

    def mod(self):
        col = None
        ind = None

        return col , ind

    def mostrar(self, checked):
        if checked:
            self.ui.lineEdit_3.show()
            self.ui.Box_fil.show()

    def esconder(self, checked):
        if checked:
            self.ui.lineEdit_3.hide()
            self.ui.Box_fil.hide()

    def preview(self):
        pass

    def conti(self):
        pass                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

