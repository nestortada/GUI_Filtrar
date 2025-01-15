from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from QT_Designer.macro import Ui_Macro                                           
import pandas as pd
from PyQt6.QtCore import pyqtSignal
from tkinter import filedialog

class Macro(QMainWindow):
    def __init__(self, archvio, hoja):
        super().__init__()
        self.archivo = archvio
        self.hoja = hoja

        self.ui = Ui_Macro()
        self.ui.setupUi(self)

        self.ui.B_abrir.clicked.connect(self.exceles)
        self.bandera = 0

        self.archivos = None

    def exceles(self):
        self.archivos = filedialog.askopenfilenames( title="Selecciona archivos de Excel", filetypes=[("Archivos de Excel", "*.xlsx *.xls")])
        if self.archivos:
            for archivo in self.archivos:
                self.ui.Lista_excel.addItem(archivo)
                self.ui.Lista_estado.addItem("Importado")
    
    def eliminar_col(self , columnas):
        if self.archivos:
            for archivo in self.archivos:
                df = pd.read_excel(archivo , self.hoja)
                column_ac = df.columns.tolist()
                elim_col = [elemento for elemento in column_ac if elemento not in columnas]
                df = df.drop(columns = elim_col)
                df.to_excel(archivo , sheet_name = self.hoja)

    def eliminar_fil(self, filas):
        if self.archivo:
            for archivo in self.archivos:
                df = pd.read_excel(archivo , self.hoja)
                fil_ac = df.index.tolist()
                elim_fil = [elemento for elemento in fil_ac if elemento not in filas]
                df = df.drop(index = elim_fil)
                df.to_excel(archivo , self.hoja)
                



            


