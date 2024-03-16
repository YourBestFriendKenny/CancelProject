from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Peach")
        Form.setEnabled(True)
        Form.resize(1165, 844)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-150, -100, 1321, 1001))
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(130, 90, 1251, 901))
        self.widget_2.setStyleSheet("background-color:      rgb(246,229,213);\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(540, 30, 91, 41))
        self.label.setStyleSheet("QLabel{\n"
"background-color: rgba(254,143,113);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(239,87,51);\n"
"font-weight: 500;\n"
"font-size: 20px;\n"
"}")
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setObjectName("label")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setGeometry(QtCore.QRect(310, 570, 561, 71))
        self.widget_4.setStyleSheet("\n"
"background-color:      rgb(254,143,113);\n"
"border-radius: 20px;\n"
"\n"
"")
        self.widget_4.setObjectName("widget_4")
        self.horizontalSlider = QtWidgets.QSlider(self.widget_4)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 10, 81, 51))
        self.horizontalSlider.setStyleSheet("\n"
"border-radius: 10px;")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.pushbutton_add = QtWidgets.QPushButton(self.widget_4)
        self.pushbutton_add.setGeometry(QtCore.QRect(440, 20, 89, 31))
        self.pushbutton_add.setStyleSheet("QPushButton{\n"
"background-color:      rgb(241,151,116);\n"
"border: 1px solid rgb(0,0,0);\n"
"border-radius: 10px;\n"
"\n"
"\n"
"}")
        self.pushbutton_add.setObjectName("pushbutton_add")
        self.pushbutton_next = QtWidgets.QPushButton(self.widget_4)
        self.pushbutton_next.setGeometry(QtCore.QRect(240, 20, 61, 31))
        self.pushbutton_next.setStyleSheet("QPushButton{\n"
"background-color:      rgb(241,151,116);\n"
"border: 1px solid rgb(0,0,0);\n"
"border-radius: 10px;\n"
"\n"
"\n"
"}")
        self.pushbutton_next.setObjectName("pushbutton_next")
        self.pushbutton_play = QtWidgets.QPushButton(self.widget_4)
        self.pushbutton_play.setGeometry(QtCore.QRect(170, 20, 61, 31))
        self.pushbutton_play.setStyleSheet("QPushButton{\n"
"background-color:      rgb(241,151,116);\n"
"border: 1px solid rgb(0,0,0); \n"
"border-radius: 10px;\n"
"\n"
"\n"
"}\n"
"\n"
"#239,87,51")
        self.pushbutton_play.setIconSize(QtCore.QSize(16, 16))
        self.pushbutton_play.setObjectName("pushbutton_play")
        self.pushbutton_back = QtWidgets.QPushButton(self.widget_4)
        self.pushbutton_back.setGeometry(QtCore.QRect(100, 20, 61, 31))
        self.pushbutton_back.setStyleSheet("QPushButton{\n"
"background-color:      rgb(241,151,116);\n"
"border: 1px solid rgb(0,0,0);\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.pushbutton_back.setObjectName("pushbutton_back")
        self.pushbutton_remove = QtWidgets.QPushButton(self.widget_4)
        self.pushbutton_remove.setGeometry(QtCore.QRect(340, 20, 89, 31))
        self.pushbutton_remove.setStyleSheet("QPushButton{\n"
"background-color:      rgb(241,151,116);\n"
"border: 1px solid rgb(0,0,0);\n"
"border-radius: 10px;\n"
"\n"
"\n"
"}")
        self.pushbutton_remove.setObjectName("pushbutton_remove")
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setGeometry(QtCore.QRect(310, 180, 561, 371))
        self.widget_5.setStyleSheet("border: 2px solid rgb(0,0,0);\n"
"border-radius: 60px;\n"
"background-color: rgb(85,75,76);")
        self.widget_5.setObjectName("widget_5")
        self.widget_3 = QtWidgets.QWidget(self.widget_5)
        self.widget_3.setGeometry(QtCore.QRect(10, 10, 541, 351))
        self.widget_3.setStyleSheet("border: 1px solid rgb(255,255,255);\n"
"background-color:      rgb(255,255,255);\n"
"border-radius: 60px;")
        self.widget_3.setObjectName("widget_3")
        self.listWidget = QtWidgets.QListWidget(self.widget_3)
        self.listWidget.setGeometry(QtCore.QRect(30, 30, 481, 291))
        self.listWidget.setStyleSheet("")
        self.listWidget.setObjectName("listWidget")
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setGeometry(QtCore.QRect(310, 100, 561, 61))
        self.widget_6.setStyleSheet("border:1px solid rgb(0,0,0);\n"
"border-radius: 10px;\n"
"background-color:      rgb(254,143,113);")
        self.widget_6.setObjectName("widget_6")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_6)
        self.lineEdit.setGeometry(QtCore.QRect(30, 10, 401, 41))
        self.lineEdit.setStyleSheet("background-color: rgba(255,255,255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget_6)
        self.pushButton.setGeometry(QtCore.QRect(450, 14, 89, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:      rgb(241,151,116);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", " Peach🍑"))
        self.pushbutton_add.setText(_translate("Form", "Add"))
        self.pushbutton_next.setText(_translate("Form", ">"))
        self.pushbutton_play.setText(_translate("Form", "▶"))
        self.pushbutton_back.setText(_translate("Form", "<"))
        self.pushbutton_remove.setText(_translate("Form", "Remove"))
        self.listWidget.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("Form", "🍑"))


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())