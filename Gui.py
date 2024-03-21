from PyQt5 import QtCore, QtGui, QtWidgets
from res_rc import *
import os
import json #+ coulneff 21.03

class Ui_Form(object):
        def setupUi(self, Form):
                Form.setObjectName("Form")
                Form.resize(475, 463)
                Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(46, 43, 52, 255), stop:1 rgba(101, 92, 85, 255));")
                self.pushbutton_play = QtWidgets.QPushButton(Form)
                self.pushbutton_play.setGeometry(QtCore.QRect(210, 370, 51, 51))
                font = QtGui.QFont()
                font.setFamily("Ubuntu Light")
                font.setPointSize(15)
                font.setBold(False)
                font.setItalic(False)
                font.setUnderline(False)
                font.setWeight(50)
                font.setStrikeOut(False)
                font.setKerning(True)
                self.pushbutton_play.setFont(font)
                self.pushbutton_play.setMouseTracking(False)
                self.pushbutton_play.setStyleSheet("\n"
        "    background-color: rgb(94, 92, 100);\n"
        "    color: rgb(250,181,143);\n"
        "    border-radius: 25px;\n"
        "")
                self.pushbutton_play.setText("")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/photo/Photo_on_app/pngwing.com(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.pushbutton_play.setIcon(icon)
                self.pushbutton_play.setIconSize(QtCore.QSize(13, 13))
                self.pushbutton_play.setCheckable(False)
                self.pushbutton_play.setAutoRepeat(True)
                self.pushbutton_play.setAutoExclusive(False)
                self.pushbutton_play.setAutoDefault(False)
                self.pushbutton_play.setDefault(False)
                self.pushbutton_play.setFlat(False)
                self.pushbutton_play.setObjectName("pushbutton_play")
                self.horizontalSlider_3 = QtWidgets.QSlider(Form)
                self.horizontalSlider_3.setGeometry(QtCore.QRect(70, 430, 341, 20))
                self.horizontalSlider_3.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border-radius: 1px;       \n"
        "    height: 7px;              \n"
        "    margin: -1px 0;           \n"
        "}\n"
        "QSlider::handle:horizontal {\n"
        "    background-color: rgb(246,172,137);\n"
        "    border: 2px solid #f6ac89;\n"
        "    height: 14px;     \n"
        "    width: 12px;\n"
        "    margin: -4px 0;     \n"
        "    border-radius: 7px  ;\n"
        "    padding: -4px 0px;  \n"
        "}\n"
        "QSlider::add-page:horizontal {\n"
        "   background-color: rgb(231,221,222);\n"
        "}\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: #fbac8b;\n"
        "}\n"
        "QSlider{\n"
        "background: rgb()\n"
        "}")
                self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
                self.horizontalSlider_3.setObjectName("horizontalSlider_3")
                self.listWidget = QtWidgets.QListWidget(Form)
                self.listWidget.setGeometry(QtCore.QRect(60, 40, 361, 321))
                self.listWidget.setStyleSheet("background-color: rgb(231,221,222);\n"
        "border-radius: 10px;")
                self.listWidget.setObjectName("listWidget")
                self.horizontalSlider = QtWidgets.QSlider(Form)
                self.horizontalSlider.setGeometry(QtCore.QRect(60, 379, 81, 31))
                self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
        "    border-radius: 1px;       \n"
        "    height: 7px;              \n"
        "    margin: -1px 0;           \n"
        "}\n"
        "QSlider::handle:horizontal {\n"
        "    \n"
        "    background-color: rgb(246,172,137);\n"
        "    border: 2px solid #f6ac89;\n"
        "    height: 14px;     \n"
        "    width: 12px;\n"
        "    margin: -4px 0;     \n"
        "    border-radius: 7px  ;\n"
        "    padding: -4px 0px;  \n"
        "}\n"
        "QSlider::add-page:horizontal {\n"
        "   background-color: rgb(231,221,222);\n"
        "\n"
        "}\n"
        "QSlider::sub-page:horizontal {\n"
        "    background: #fbac8b;\n"
        "}\n"
        "QSlider{\n"
        "background: rgb()\n"
        "}")
                self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
                self.horizontalSlider.setObjectName("horizontalSlider")
                self.label = QtWidgets.QLabel(Form)
                self.label.setGeometry(QtCore.QRect(190, 0, 131, 31))
                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setStyleSheet("background-color: rgb();\n"
        "color: rgb(246,172,137);")
                self.label.setObjectName("label")
                self.pushbutton_add = QtWidgets.QPushButton(Form)
                self.pushbutton_add.setGeometry(QtCore.QRect(330, 370, 41, 41))
                font = QtGui.QFont()
                font.setFamily("URW Bookman [urw]")
                font.setPointSize(20)
                self.pushbutton_add.setFont(font)
                self.pushbutton_add.setStyleSheet("background-color: rgb(94, 92, 100);\n"
        "    color: rgb();\n"
        "    border-radius: 10px;\n"
        "    border: 2px solid rgb(#f6ac89);")
                self.pushbutton_add.setObjectName("pushbutton_add")
                self.pushbutton_remove = QtWidgets.QPushButton(Form)
                self.pushbutton_remove.setGeometry(QtCore.QRect(380, 370, 41, 41))
                font = QtGui.QFont()
                font.setFamily("URW Bookman [urw]")
                font.setPointSize(20)
                self.pushbutton_remove.setFont(font)
                self.pushbutton_remove.setStyleSheet("background-color: rgb(94, 92, 100);\n"
        "    color: rgb();\n"
        "    border-radius: 10px;\n"
        "    border: 2px solid rgb(#f6ac89);")
                self.pushbutton_remove.setObjectName("pushbutton_remove")
                self.pushbutton_next = QtWidgets.QPushButton(Form)
                self.pushbutton_next.setGeometry(QtCore.QRect(270, 380, 41, 31))
                font = QtGui.QFont()
                font.setFamily("URW Bookman [urw]")
                font.setPointSize(15)
                self.pushbutton_next.setFont(font)
                self.pushbutton_next.setStyleSheet("background-color: rgb(94, 92, 100);\n"
        "    color: rgb();\n"
        "    border-radius: 5px;\n"
        "    border: 2px solid rgb(#f6ac89);")
                self.pushbutton_next.setObjectName("pushbutton_next")
                self.pushbutton_back = QtWidgets.QPushButton(Form)
                self.pushbutton_back.setGeometry(QtCore.QRect(160, 380, 41, 31))
                font = QtGui.QFont()
                font.setFamily("URW Bookman [urw]")
                font.setPointSize(15)
                self.pushbutton_back.setFont(font)
                self.pushbutton_back.setStyleSheet("background-color: rgb(94, 92, 100);\n"
        "    color: rgb();\n"
        "    border-radius: 5px;\n"
        "    border: 2px solid rgb(#f6ac89);")
                self.pushbutton_back.setObjectName("pushbutton_back")

                self.retranslateUi(Form)
                QtCore.QMetaObject.connectSlotsByName(Form)

        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "Peach🍑"))
                self.label.setText(_translate("Form", "Peach🍑"))
                self.pushbutton_add.setText(_translate("Form", "+"))
                self.pushbutton_remove.setText(_translate("Form", "-"))
                self.pushbutton_next.setText(_translate("Form", ">"))
                self.pushbutton_back.setText(_translate("Form", "<"))


        def toggle_sound(self):
                if self.is_playing:
                        self.is_playing = False
                        self.sound_mixer.music.stop()


                        icon = QtGui.QIcon()
                        icon.addPixmap(QtGui.QPixmap(":/photo/Photo_on_app/pngwing.com(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        self.pushbutton_play.setIcon(icon)
                        self.pushbutton_play.setIconSize(QtCore.QSize(13, 13))
                        
                else:
                        #+ coulneff 21.03
                        data = []    
                        with open("music_list.json", 'r') as f:
                                data = json.load(f)
                        #- coulneff 21.03
                        item = self.listWidget.currentItem()
                        if item:
                                filename = ""
                                for itm in data:
                                    pathInfo = str(itm["filename"])
                                    textItem = item.text()
                                    print(pathInfo.find(textItem))
                                    if pathInfo.find(textItem) != -1:
                                            filename = pathInfo
                                            break
                                    else:
                                            continue
                                #- Coulneff 21.03    
                                #file_name = item.text() + ".mp3"  # Добавляем расширение .mp3
                                #filename = os.path.join(self.dir, file_name)
                                self.sound_mixer.music.load(filename)
                                self.sound_mixer.music.play()
                                self.is_playing = True

                                
                                icon2 = QtGui.QIcon()
                                icon2.addPixmap(QtGui.QPixmap(":/photo/Photo_on_app/pngwing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                                self.pushbutton_play.setIconSize(QtCore.QSize(16, 16))
                                self.pushbutton_play.setIcon(icon2)



if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())