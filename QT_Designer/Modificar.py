# Form implementation generated from reading ui file 'D:\GUI de filtrar\QT_Designer\Modificar.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Modificar(object):
    def setupUi(self, Modificar):
        Modificar.setObjectName("Modificar")
        Modificar.resize(856, 600)
        self.centralwidget = QtWidgets.QWidget(parent=Modificar)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 20, 211, 31))
        self.plainTextEdit.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.Elemento1 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.Elemento1.setGeometry(QtCore.QRect(20, 60, 221, 21))
        self.Elemento1.setEditable(False)
        self.Elemento1.setObjectName("Elemento1")
        self.Elemento1.addItem("")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(20, 110, 211, 31))
        self.plainTextEdit_2.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.Elemento2 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.Elemento2.setGeometry(QtCore.QRect(20, 150, 221, 21))
        self.Elemento2.setObjectName("Elemento2")
        self.Elemento2.addItem("")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(290, 20, 211, 31))
        self.plainTextEdit_3.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.Elemento3 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.Elemento3.setGeometry(QtCore.QRect(290, 60, 221, 21))
        self.Elemento3.setObjectName("Elemento3")
        self.Elemento3.addItem("")
        self.Elemento4 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.Elemento4.setGeometry(QtCore.QRect(290, 150, 221, 21))
        self.Elemento4.setObjectName("Elemento4")
        self.Elemento4.addItem("")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(290, 110, 211, 31))
        self.plainTextEdit_4.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(570, 20, 211, 31))
        self.plainTextEdit_5.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.Elemento5 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.Elemento5.setGeometry(QtCore.QRect(570, 60, 221, 21))
        self.Elemento5.setObjectName("Elemento5")
        self.Elemento5.addItem("")
        self.Elemento6 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.Elemento6.setGeometry(QtCore.QRect(570, 150, 221, 21))
        self.Elemento6.setObjectName("Elemento6")
        self.Elemento6.addItem("")
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(570, 110, 211, 31))
        self.plainTextEdit_6.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.Vista = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.Vista.setGeometry(QtCore.QRect(10, 290, 841, 251))
        self.Vista.setObjectName("Vista")
        self.Vista.setColumnCount(0)
        self.Vista.setRowCount(0)
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_7.setGeometry(QtCore.QRect(20, 200, 421, 21))
        self.plainTextEdit_7.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(470, 200, 371, 21))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 540, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.B_pre = QtWidgets.QPushButton(parent=self.centralwidget)
        self.B_pre.setGeometry(QtCore.QRect(300, 230, 301, 41))
        self.B_pre.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.B_pre.setObjectName("B_pre")
        Modificar.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Modificar)
        self.statusbar.setObjectName("statusbar")
        Modificar.setStatusBar(self.statusbar)

        self.retranslateUi(Modificar)
        QtCore.QMetaObject.connectSlotsByName(Modificar)

    def retranslateUi(self, Modificar):
        _translate = QtCore.QCoreApplication.translate
        Modificar.setWindowTitle(_translate("Modificar", "MainWindow"))
        self.plainTextEdit.setPlainText(_translate("Modificar", "1. Elije el primer componente"))
        self.Elemento1.setItemText(0, _translate("Modificar", "Ninguno"))
        self.plainTextEdit_2.setPlainText(_translate("Modificar", "2. Elije el segundo componente"))
        self.Elemento2.setItemText(0, _translate("Modificar", "Ninguno"))
        self.plainTextEdit_3.setPlainText(_translate("Modificar", "3. Elije el tercer componente"))
        self.Elemento3.setItemText(0, _translate("Modificar", "Ninguno"))
        self.Elemento4.setItemText(0, _translate("Modificar", "Ninguno"))
        self.plainTextEdit_4.setPlainText(_translate("Modificar", "4. Elije el cuarto componente"))
        self.plainTextEdit_5.setPlainText(_translate("Modificar", "5. Elije el quinto componente"))
        self.Elemento5.setItemText(0, _translate("Modificar", "Ninguno"))
        self.Elemento6.setItemText(0, _translate("Modificar", "Ninguno"))
        self.plainTextEdit_6.setPlainText(_translate("Modificar", "6. Elije el sexto componente"))
        self.plainTextEdit_7.setPlainText(_translate("Modificar", "Desde que columna empieza"))
        self.pushButton.setText(_translate("Modificar", "Continuar --->"))
        self.B_pre.setText(_translate("Modificar", "Previsualizar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Modificar = QtWidgets.QMainWindow()
    ui = Ui_Modificar()
    ui.setupUi(Modificar)
    Modificar.show()
    sys.exit(app.exec())
