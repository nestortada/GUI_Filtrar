from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from QT_Designer.Modificar import Ui_Modificar
import pandas as pd


class Modificar(QMainWindow):
    def __init__(self, archivo, hoja):
        super(Modificar, self).__init__()
        self.archivo = archivo
        self.hoja = hoja
        self.ui = Ui_Modificar()
        self.ui.setupUi(self)
        self.df = pd.read_excel(self.archivo, sheet_name=self.hoja)
       
        self.mod()

        self.ui.B_pre.clicked.connect(self.pre)

        


    def mod(self):
        try:
      
            
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
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def pre(self):
 
        op1 = self.ui.Elemento1.currentText()
        op2 = self.ui.Elemento2.currentText()
        op3 = self.ui.Elemento3.currentText()
        op4 = self.ui.Elemento4.currentText()
        op5 = self.ui.Elemento5.currentText()
        op6 = self.ui.Elemento6.currentText()

        opciones = [op1, op2 , op3 , op4 , op5 ,op6]
        
        listaop = [op for op in opciones if op != ""]

        filas = [self.df.iloc[esc] for esc in listaop]

        columnas = [" ".join(map(str,valores)) for valores in zip(*filas)]

        





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    archivo = r"c:\Users\gunda\Downloads\Prueba 1.xlsx"  # Cambia esto por la ruta de tu archivo
    hoja = "Hoja1"  # Cambia esto por el nombre de tu hoja
    window = Modificar(archivo, hoja)
    window.show()
    sys.exit(app.exec())
