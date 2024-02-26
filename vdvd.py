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

        self.pushbutton_play.clicked.connect(self.play_sound)
        self.pushbutton_back.clicked.connect(self.back_sound)
        self.pushbutton_next.clicked.connect(self.next_sound)   
        self.pushbutton_add.clicked.connect(self.add_sound)
        self.listWidget.doubleClicked.connect(self.play_sound)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setValue(50)
        self.horizontalSlider.valueChanged.connect(self.volume_reg)

        self.dir = ""
        self.sound_mixer = mixer
        self.sound_mixer.init()

        # Загрузка музыкальных файлов из сохраненного списка при запуске
        self.load_music_files()

    def load_music_files(self):
        # Проверяем, существует ли файл со списком музыкальных файлов
        if os.path.exists("music_list.txt"):
            with open("music_list.txt", "r") as file:
                music_files = file.readlines()
                self.listWidget.addItems(music_files)

    def save_music_files(self):
        # Сохраняем список музыкальных файлов в текстовый файл
        with open("music_list.txt", "w") as file:
            for i in range(self.listWidget.count()):
                file.write(self.listWidget.item(i).text() + "\n")

    def play_sound(self):
        item = self.listWidget.currentItem()
        
        if item:
            filename = os.path.join(self.dir, item.text())
            self.sound_mixer.music.load(filename)
        else:
            self.listWidget.setCurrentRow(0)
        self.sound_mixer.music.play()

    def back_sound(self):
        row = self.listWidget.currentRow() - 1
        if row >= 0:
            self.listWidget.setCurrentRow(row)
            self.play_sound()

    def next_sound(self):
        row = self.listWidget.currentRow() + 1
        if row < self.listWidget.count():
            self.listWidget.setCurrentRow(row)
            self.play_sound()

    def add_sound(self):
        self.listWidget.clear()
        dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Direction")

        if dir:
            music_files = [filename for filename in os.listdir(dir) if filename.endswith(".mp3")]
            self.listWidget.addItems(music_files)
            self.dir = dir
            # Сохраняем обновленный список музыкальных файлов
            self.save_music_files()

    def volume_reg(self):
        self.sound_mixer.music.set_volume(self.horizontalSlider.value() / 100)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    player = Player()
    player.show()
    app.exec()