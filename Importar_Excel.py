from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from QT_Designer.Seleccionar_Hoja import Ui_Importar_Archivo
from tkinter import filedialog
import pandas as pd
from tkinter import *
from Mostrar_Excel import Tables



class Import(QMainWindow):
    def __init__(self):
        super(Import, self).__init__()
        self.ui = Ui_Importar_Archivo()
        self.ui.setupUi(self)

        self.ui.Boton_insert.clicked.connect(self.importar)
        self.ui.Boton_conti.clicked.connect(self.continuar)

        self.archivo_seleccionado = ""
        self.hoja_seleccionada = ""

    def importar(self): 
        archivo = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if archivo:
            try:
                excel_file = pd.ExcelFile(archivo)
                hojas = excel_file.sheet_names
                self.ui.Caja_Archivo.clear()
                self.ui.Caja_Archivo.addItems(hojas)
                self.ui.lineEdit.setText(archivo)
                self.archivo_seleccionado = archivo  
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo leer el archivo.\nDetalles: {e}")

    def continuar(self):
        self.hoja_seleccionada = self.ui.Caja_Archivo.currentText()
        if self.hoja_seleccionada == "Seleccione Hoja" or not self.hoja_seleccionada:
            QMessageBox.warning(self, "Advertencia", "Por favor, seleccione una hoja.")
        else:
            QMessageBox.information(self, "Hoja Seleccionada", f"Has seleccionado la hoja: {self.hoja_seleccionada}")
            self.abrir_tabla()

    def abrir_tabla(self):
        self.tabla = Tables(self.archivo_seleccionado, self.hoja_seleccionada)
        self.tabla.mainloop()



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ventana = Import()
    ventana.show()
    sys.exit(app.exec())