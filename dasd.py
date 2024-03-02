import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    app.setStyleSheet(
    QListWidget:item:selected:!active {
        background: lightBlue;
        color: black;
    })
    items = ['2020-11-27'] * 6
    x = QListWidget(); x.addItems(items)
    y = QListWidget(); y.addItems(items)
    window = QWidget()
    hbox = QHBoxLayout(window)
    hbox.addWidget(x); hbox.addWidget(y)
    window.show()
    sys.exit(app.exec_())
