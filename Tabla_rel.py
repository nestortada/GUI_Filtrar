from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from QT_Designer.Relacionar import Ui_Relacionar
import pandas as pd
from PyQt6.QtCore import pyqtSignal
from tkinter import filedialog

class Tabla_rel(QMainWindow):
    closed = pyqtSignal()
    def __init__(self, archivo, hoja):
        super().__init__()
        self.archivo = archivo
        self.hoja = hoja
        self.ui = Ui_Relacionar()
        self.ui.setupUi(self)
        
        self.archi = ""

        self.df = pd.read_excel(self.archivo , sheet_name= self.hoja)
        self.nuevo = None

        self.nd , self.ind = self.mod()

        self.ui.B_abrir.clicked.connect(self.excel)

        self.ui.B_previsalizar.clicked.connect(self.preview)

        self.ui.pushButton_3.clicked.connect(self.conti)

        self.ui.comboBox.currentTextChanged.connect(self.coln)

    def mod(self):
        try:
            self.ui.lineEdit_2.setText(self.archivo)
            indice = self.df["Indice"]
            self.df = self.df.drop(columns = "Indice")
            columnas = [str(col) for col in self.df.columns.tolist()]
            self.ui.Box_colA.clear()
            self.ui.Box_colA.addItems(columnas)

            return self.df.copy() , indice

        except Exception as e:
            QMessageBox.critical(self, "Error", "Ocurrio un error: {e}")

            return self.df.copy() , indice
        
    def excel(self):
        self.archi = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if self.archi:
            try:
                self.nuevo = pd.read_excel(self.archi, sheet_name=None)
                hojas = list(self.nuevo.keys())
                self.ui.comboBox.clear()
                self.ui.comboBox.addItems(hojas)
                self.ui.lineEdit.setText(self.archi)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo leer el archivo.\nDetalles: {e}")
    
    def coln(self):
        name = self.ui.comboBox.currentText()
        if name != "" or name != None:
            try:
                self.nuevo = pd.read_excel(self.archi , sheet_name= name)
                columnas = [str(col) for col in self.nuevo.columns.tolist()]
                self.ui.Box_colN.clear()
                self.ui.Box_buscar.clear()
                self.ui.Box_colN.addItems(columnas)
                self.ui.Box_buscar.addItems(columnas)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ocurrio un error: {e}")
        
    def preview(self):
        pass

    def conti(self):
        pass

        