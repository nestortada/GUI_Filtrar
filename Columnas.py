from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from QT_Designer.Modificar import Ui_Modificar
import pandas as pd
from PyQt6.QtCore import pyqtSignal
from macro import Macro


class Modificar(QMainWindow):
    closed = pyqtSignal()

    def __init__(self, archivo, hoja):
        super(Modificar, self).__init__()
        self.archivo = archivo
        self.hoja = hoja
        self.ui = Ui_Modificar()
        self.ui.setupUi(self)
        self.df = pd.read_excel(self.archivo, sheet_name=self.hoja)
       
        self.col , self.ind = self.mod()

        self.ui.B_pre.clicked.connect(self.pre)

        self.ui.pushButton.clicked.connect(self.continuar)
        
        self.listaop = None
        self.Eli = None

        


    def mod(self):
        try:

            indice = self.df["Indice"]
            self.df = self.df.drop(columns = "Indice")
            filas = [str(idx +1) for idx in self.df.index.tolist()] 
            columnas = [str(col) for col in self.df.columns.tolist()] 
            filas.insert(0, None) 
            

            self.ui.Elemento1.clear()
            self.ui.Elemento1.addItems(filas)

            self.ui.Elemento2.clear()
            self.ui.Elemento2.addItems(filas)

            self.ui.Elemento3.clear()
            self.ui.Elemento3.addItems(filas)

            self.ui.Elemento4.clear()
            self.ui.Elemento4.addItems(filas)

            self.ui.Elemento5.clear()
            self.ui.Elemento5.addItems(filas)

            self.ui.Elemento6.clear()
            self.ui.Elemento6.addItems(filas)

            self.ui.comboBox.clear()
            self.ui.comboBox.addItems(columnas)

            return self.df.copy() , indice
        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            return self.df.copy() , indice

    def pre(self):

        try: 
            op1 = self.ui.Elemento1.currentText()
            op2 = self.ui.Elemento2.currentText()
            op3 = self.ui.Elemento3.currentText()
            op4 = self.ui.Elemento4.currentText()
            op5 = self.ui.Elemento5.currentText()
            op6 = self.ui.Elemento6.currentText()

            opciones = [op1, op2 , op3 , op4 , op5 ,op6]
            
            self.listaop = [int(op) - 1 for op in opciones if op and op.isdigit()]

            self.Eli = self.ui.comboBox.currentText()


            indice = self.df.columns.get_loc(self.Eli)

            recupera = self.df.iloc[:,:indice +1]

            nueva = self.df.iloc[:, indice + 1 :]
            
            filas = []
            for esc in self.listaop:
                fila = nueva.iloc[esc].tolist()
                nueva_fila = [str(elemento).replace(" 00:00:00", "") for elemento in fila]
                filas.append(nueva_fila)

            columnas = [" ".join(map(str,valores)) for valores in zip(*filas)]

            nueva.columns = columnas


            for i , (col , val) in enumerate(recupera.items()):
                nueva.insert(i,col,val)

            

            nueva= nueva.drop(index = self.listaop)

            self.ind = self.ind.drop(index = self.listaop)

            nueva = nueva.reset_index(drop=True) 
            
            
            

            self.ui.Vista.clear()
            self.ui.Vista.setRowCount(nueva.shape[0])  
            self.ui.Vista.setColumnCount(nueva.shape[1])  
            self.ui.Vista.setHorizontalHeaderLabels(nueva.columns)  

            for row_idx, row in nueva.iterrows():
                for col_idx, value in enumerate(row):
                    self.ui.Vista.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

            self.col = nueva

            

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrio un Error: {e}")

    
    def continuar(self):
        Macro(self.hoja).columnas(listaop= self.listaop,Eli= self.Eli)
        try:
            self.col.insert(0,"Indice",self.ind.values)
            self.col.to_excel(self.archivo, index=False, sheet_name=self.hoja)
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Occurio un error: {e}")

    def closeEvent(self, event):
        self.closed.emit()  
        super().closeEvent(event)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    archivo = r"c:\Users\gunda\Downloads\Prueba 1.xlsx"  # Cambia esto por la ruta de tu archivo
    hoja = "Hoja1"  # Cambia esto por el nombre de tu hoja
    window = Modificar(archivo, hoja)
    window.show()
    sys.exit(app.exec())
