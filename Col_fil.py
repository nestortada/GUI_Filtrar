from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from QT_Designer.Columnas_filas import Ui_Col_fil
import pandas as pd
from PyQt6.QtCore import pyqtSignal
from macro import Macro


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
        try:
            indice = self.df["Indice"]
            self.df = self.df.drop(columns = "Indice")
            columnas = [str(col) for col in self.df.columns.tolist()]
            columnas.insert(0, "Ninguno")

            self.ui.Box_col.clear()
            self.ui.Box_col.addItems(columnas)

            return self.df.copy().astype(str), indice
        except Exception as e: 
            QMessageBox.critical(self, "Erroe" , f"Ocurrio un error {e}")
            return self.df.copy().astype(str), indice


        

    def mostrar(self, checked):
        if checked:
            self.ui.lineEdit_3.show()
            self.ui.Box_fil.show()

            index = self.ui.Box_col.currentText()

            if index != "Ninguno":
                Eli = self.ui.Box_col.currentText()
                try:
                    indice = self.col.columns.get_loc(Eli)  
                    nuevo = self.col.iloc[:, indice + 1 :]
                    valores = pd.unique(nuevo.values.ravel())  
                    self.ui.Box_fil.clear()
                    self.ui.Box_fil.addItems(map(str, valores))  
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Ocurrió un error: {e}")
            else:
                try:
                    self.ui.Box_fil.clear()
                    valores =  pd.unique(self.col.values.ravel()) 
                    self.ui.Box_fil.addItems(map(str, valores))  
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Ocurrió un error: {e}")


    def esconder(self, checked):
        if checked:
            self.ui.lineEdit_3.hide()
            self.ui.Box_fil.hide()

    def preview(self):
        if self.ui.N_columna.text() and self.ui.N_valor.text():
            try:
                if self.ui.R_si.isChecked() and self.ui.Box_col.currentText() != "Ninguno":
                    Eli = self.ui.Box_col.currentText()
                    indice = self.col.columns.get_loc(Eli)
                    recuperar = self.col.iloc[:, :indice + 1]
                    filtrar = (self.col.melt(id_vars=recuperar.columns.tolist(), var_name=self.ui.N_columna.text(), 
                                            value_name=self.ui.N_valor.text())
                            .query(f"`{self.ui.N_valor.text()}` == @self.ui.Box_fil.currentText()")
                            .reset_index(drop=True))
                    
                elif self.ui.R_no.isChecked() and self.ui.Box_col.currentText == "Ninguno":
                    filtrar = (self.col.melt(var_name=self.ui.N_columna.text(), value_name=self.ui.N_valor.text())
                            .reset_index(drop=True))
                    
                elif self.ui.R_si.isChecked() and self.ui.Box_col.currentText == "Ninguno":
                    filtrar = (self.col.melt(var_name = self.ui.N_columna.text(), value_name = self.ui.N_valor.text())
                               .query(f"`{self.ui.N_valor.text()}` == @self.ui.Box_fil.currentText()")
                               .reset_index(drop = True))
                    
                elif self.ui.R_no.isChecked() and self.ui.Box_col.currentText() != "Ninguno":
                    Eli = self.ui.Box_col.currentText()
                    indice = self.col.columns.get_loc(Eli)
                    recuperar = self.col.iloc[:,: indice +1]
                    filtrar = (self.col.melt(id_vars = recuperar.columns.tolist(), var_name = self.ui.N_columna.text() , value_name = self.ui.N_valor.text())
                               .reset_index(drop = True))
                else:
                    filtrar = self.col.copy()

                
                
                self.ui.tableWidget.clearContents()
                self.ui.tableWidget.setRowCount(filtrar.shape[0])
                self.ui.tableWidget.setColumnCount(filtrar.shape[1])
                self.ui.tableWidget.setHorizontalHeaderLabels(filtrar.columns.tolist())

                for row_idx, row in filtrar.iterrows():
                    for col_idx, value in enumerate(row):
                        self.ui.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

                self.df = filtrar
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ocurrió un error al previsualizar: {e}")
        else:
            QMessageBox.information(self, "Falta información", "Debes proporcionar nombres para las columnas y valores.")

    def conti(self):
        Macro(self.hoja).col_fil(N_columna= self.ui.N_columna.text(), N_valor= self.ui.N_valor.text(),R_si= self.ui.R_si.isChecked(), 
                                 Box_col= self.ui.Box_col.currentText(), Box_fil= self.ui.Box_fil.currentText(), R_no= self.ui.R_no.isChecked())
        try: 
            self.df.to_excel(self.archivo , index = False , sheet_name = self.hoja)
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Occurio un error: {e}")

    def closeEvent(self, event):
        self.closed.emit()  
        super().closeEvent(event)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

