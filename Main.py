import os 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
import Gui
from pygame import mixer
import json
import jsonpickle
#+ Coulneff 16.03.2024 
# threading - многопоточность, нужна для того чтобы двигать ползунок
from threading import Thread
#- Coulneff 16.03.2024
class Player(QWidget, Gui.Ui_Peach):
    
    def __init__(self):
        super(Player, self).__init__()
        self.setupUi(self)

        self.setFixedSize(self.size())

        # конектим кнопки
        self.pushbutton_play.clicked.connect(self.toggle_sound)
        self.pushbutton_back.clicked.connect(self.back_sound)
        self.pushbutton_next.clicked.connect(self.next_sound)   
        self.pushbutton_add.clicked.connect(self.add_sound)
        self.pushbutton_remove.clicked.connect(self.remove_sound)

        # двойное нажание по треку включит его
        self.listWidget.doubleClicked.connect(self.toggle_sound)


        # устанавливаем громкость по умолчанию
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setValue(50)
        self.horizontalSlider.valueChanged.connect(self.volume_reg)
 
        # нужная нам дериктория загружается в listWidget
        self.dir = ""
        self.sound_mixer = mixer
        self.sound_mixer.init()
        self.is_playing = False

        self.load_music_list() 
        #+ Coulneff 16.03.2024 - запуск многопоточности
        variable = Thread(target=self.switcherNeff, args=(self,))
        variable.start()
        #- Coulneff 16.03.2024


    # предыдущая музыка
    def back_sound(self):
        try:
            row = self.listWidget.currentRow()
            self.listWidget.setCurrentRow(row - 1)
            self.is_playing = False  # Обновляем состояние is_playing перед вызовом toggle_sound()
            self.toggle_sound()
        except TypeError:
            pass

    # следующая музыка
    def next_sound(self):
        try:
            row = self.listWidget.currentRow()
            self.listWidget.setCurrentRow(row + 1)
            self.is_playing = False  # Обновляем состояние is_playing перед вызовом toggle_sound()
            self.toggle_sound()
        except TypeError:
            pass



    # добавить директорию
    def add_sound(self):
        self.sound_mixer.music.stop()
        current_items, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Select Files")
        if current_items:  
            for current_item in current_items:
                if current_item.endswith(".mp3"):
                    file_name = os.path.splitext(os.path.basename(current_item))[0]
                    self.listWidget.addItem(file_name)
            self.dir = os.path.dirname(current_items[-1])
            self.save_music_list(current_items)


    # регулировка громкости
    def volume_reg(self):
        self.sound_mixer.music.set_volume(self.horizontalSlider.value() / 100)

    #загрузить файлы музыки
    def load_music_list(self):
        filename = "music_list.json"
        if os.path.isfile(filename): 
            try:
                with open(filename, 'r') as f:
                    data = json.load(f)
                    for music_data in data:
                        pathInfo = music_data["filename"] 
                        chertochka = pathInfo.rfind("/") #получит индекс ближейшей '/'
                        tochka = pathInfo.rfind(".")  #получит индекс ближайшей '.'
                        name = pathInfo[chertochka+1:tochka] # text[число:число] - позволяет вырезать кусок текста из строки 
                        self.listWidget.addItem(name)
            except FileNotFoundError:
                print(f"Файл '{filename}' не найден.")
            except Exception as e:
                print(f"Произошла ошибка при загрузке списка музыки: {e}")

    # Сохранение списка музыкальных файлов в файл JSON
    def save_music_list(self,current_items):
        filename = "music_list.json"
        music_list = []

        for obj in current_items:       #coulneff: (3) проходим по списку нашей музыки и обрабатываем, добавляя в наш список
            full_path = obj  # добавляем полный путь к файлу  
            music_list.append({"filename": full_path}) #self.listWidget.item(index).text()})

        #coulneff: (4) чтобы у нас не стёрлась музыка которая уже была, то открываем наш файл с музыкой и просто записываем его в массив
        data = []    
        with open(filename, 'r') as f:
            data = json.load(f)
        #coulneff: (5) потом записываем в этот массив нашу новую музыку и сохраняем
        data.extend(music_list)
        try:
            with open(filename, 'w+') as f:
                json.dump(data, f)
        except Exception as e:
            print(f"Произошла ошибка при сохранении списка музыки: {e}")
    #удалить музыку
    def remove_sound(self):
        current_item = self.listWidget.currentItem()
        if current_item:
            row = self.listWidget.currentRow()
            self.listWidget.takeItem(row)
            self.sound_mixer.music.stop()
            self.is_playing = False
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/photo/Photo_on_app/pngwing.com(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushbutton_play.setIcon(icon)
            self.pushbutton_play.setIconSize(QtCore.QSize(13, 13))
            
            filename = "music_list.json"
            music_list = []
            for index in range(self.listWidget.count()):
                music_list.append({"filename": self.listWidget.item(index).text()})
            
            try:
                with open(filename, 'w') as f:
                    json.dump(music_list, f)
            except Exception as e:
                print(f"Произошла ошибка при сохранении списка музыки: {e}")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    player = Player()
    player.show()
    app.exec()