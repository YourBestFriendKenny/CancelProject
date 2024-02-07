import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QOpenGLWidget
from PyQt5.QtGui import QOpenGLShader, QOpenGLShaderProgram
from PyQt5.QtCore import Qt
from OpenGL.GL import *


class OpenGLWidget(QOpenGLWidget):
    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(1, 1, 1)
        glBegin(GL_TRIANGLES)
        glVertex3f(-0.5, -0.5, 0)
        glVertex3f(0.5, -0.5, 0)
        glVertex3f(0, 0.5, 0)
        glEnd()

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 OpenGL Example")
        self.setGeometry(100, 100, 800, 600)

        self.opengl_widget = OpenGLWidget(self)
        self.setCentralWidget(self.opengl_widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()