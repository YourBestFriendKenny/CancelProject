import os 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
import GuiMain
from pygame import mixer

class Player(QWidget, GuiMain.Ui_Form):
    
    def __init__(self):
        super(Player, self).__init__()
        self.setupUi(self)

        self.setFixedSize(self.size())

        # конектим кнопки
        self.pushbutton_play.clicked.connect(self.toggle_sound)
        self.pushbutton_back.clicked.connect(self.back_sound)
        self.pushbutton_next.clicked.connect(self.next_sound)   
        self.pushbutton_add.clicked.connect(self.add_sound)

        # двойное нажание по треку включит его
        self.listWidget.doubleClicked.connect(self.toggle_sound)

        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setValue(50)
        self.horizontalSlider.valueChanged.connect(self.volume_reg)

        self.dir = ""
        self.sound_mixer = mixer
        self.sound_mixer.init()
        self.is_playing = False

    def toggle_sound(self):
        if self.is_playing:
            self.sound_mixer.music.stop()
            self.is_playing = False
            self.pushbutton_play.setText("Play")
        else:
            item = self.listWidget.currentItem()
            if item:
                filename = os.path.join(self.dir, item.text())
                self.sound_mixer.music.load(filename)
                self.sound_mixer.music.play()
                self.is_playing = True
                self.pushbutton_play.setText("Stop")

    def back_sound(self):
        try:
            row = self.listWidget.currentRow()
            self.listWidget.setCurrentRow(row - 1)
            self.is_playing = False  # Обновляем состояние is_playing перед вызовом toggle_sound()
            self.toggle_sound()
        except TypeError:
            pass

    def next_sound(self):
        try:
            row = self.listWidget.currentRow()
            self.listWidget.setCurrentRow(row + 1)
            self.is_playing = False  # Обновляем состояние is_playing перед вызовом toggle_sound()
            self.toggle_sound()
        except TypeError:
            pass

    def add_sound(self):
        self.sound_mixer.music.stop()
        dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Direction")
        if dir:
            for filename in os.listdir(dir):
                if filename.endswith(".mp3"):
                    self.listWidget.addItem(os.path.join(filename))
            self.dir = dir

    def volume_reg(self):
        self.sound_mixer.music.set_volume(self.horizontalSlider.value() / 100)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    player = Player()
    player.show()
    app.exec()