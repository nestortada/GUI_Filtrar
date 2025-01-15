from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from QT_Designer.Relacionar import Ui_Relacionar
import pandas as pd
from PyQt6.QtCore import pyqtSignal
from tkinter import filedialog
from macro import Macro

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
        if name != "":
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
        N_col = self.ui.T_col.text()
        if N_col == "":
            N_col = self.ui.Box_buscar.currentText()
        try:
            
            relacionar = self.nd.merge(
                self.nuevo[[self.ui.Box_colN.currentText(), self.ui.Box_buscar.currentText()]].rename(columns = {self.ui.Box_buscar.currentText(): N_col}),
                left_on=self.ui.Box_colA.currentText(),
                right_on=self.ui.Box_colN.currentText(),
                how="left"
            )

            
            relacionar = relacionar.drop(columns=[self.ui.Box_colN.currentText()])

           
            self.ui.Vista.clearContents()
            self.ui.Vista.setRowCount(relacionar.shape[0])
            self.ui.Vista.setColumnCount(relacionar.shape[1])
            self.ui.Vista.setHorizontalHeaderLabels(relacionar.columns.tolist())

            
            for row_idx, row in relacionar.iterrows():
                for col_idx, value in enumerate(row):
                    self.ui.Vista.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

            
            self.df = relacionar

        except KeyError as e:
            print(f"Error de clave: {e}")
            QMessageBox.critical(self, "Error", f"Clave no encontrada: {e}")
        except AttributeError as e:
            print(f"Error de atributo: {e}")
            QMessageBox.critical(self, "Error", f"Error de atributo: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
            QMessageBox.critical(self, "Error", f"Se produjo un error: {e}")    



    def conti(self):
        Macro(self.hoja).tabla_rel(T_col= self.ui.T_col.text(), Box_buscar= self.ui.Box_buscar.currentText(), 
                                   nuevo= self.nuevo, Box_colN= self.ui.Box_colN.currentText(), Box_colA= self.ui.Box_colA.currentText())
        try:
            self.df.insert(0, "Indice", self.ind.values)
            self.df.to_excel(self.archivo , index = False , sheet_name = self.hoja)
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error" , f"Ocurrio un error : {e}")

    def closeEvent(self, event):
        self.closed.emit()  
        super().closeEvent(event)

        