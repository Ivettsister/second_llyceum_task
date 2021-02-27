import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPainterPath
import random

DRAW_CIRCLE = 1
DRAW_RECTANGLE = 2
DRAW_TRIANGLE = 3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('push_form.ui', self)  # Загружаем дизайн
        self.qp = QPainter()
        self.pushButton.clicked.connect(self.initUI)

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Суперматизм')
        self.setMouseTracking(True)
        self.show()

    def runDraw(self):
        self.flag = True
        self.repaint()

    def getRandomSize(self):
        size = random.randint(20, 100)
        return size, size

    def getRandomColor(self):
        return QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.qp.setBrush(self.getRandomColor())
            self.draw()
            self.qp.end()
            self.flag = False
            self.paint_id = 0

    def draw(self):
        self.drawCircle()

    def drawCircle(self):
        self.qp.drawEllipse(*self.coords, *self.getRandomSize())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
