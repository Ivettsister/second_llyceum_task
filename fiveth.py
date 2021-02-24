import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPainterPath
import random

DRAW_CIRCLE = 1
DRAW_RECTANGLE = 2
DRAW_TRIANGLE = 3


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.qp = QPainter()
        self.flag = False

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
        if self.paint_id == DRAW_CIRCLE:
            self.drawCircle()
        elif self.paint_id == DRAW_RECTANGLE:
            self.drawRectangle()
        elif self.paint_id == DRAW_TRIANGLE:
            self.drawTriangle()

    def drawRectangle(self):
        self.qp.drawRect(*self.coords, *self.getRandomSize())

    def drawCircle(self):
        self.qp.drawEllipse(*self.coords, *self.getRandomSize())

    def drawTriangle(self):
        path = QPainterPath()
        x, y = self.coords
        size = self.getRandomSize()
        offset_x, offset_y = size

        coords = [(x, y), (x - offset_x, y + offset_y), (x + offset_y, y + offset_y)]
        path.moveTo(*coords[0])
        path.lineTo(*coords[1])
        path.lineTo(*coords[2])
        path.lineTo(*coords[0])
        self.qp.fillPath(path, self.getRandomColor())
        pass

    def mousePressEvent(self, event):
        self.coords = [event.x(), event.y()]
        button = event.button()
        if button == Qt.LeftButton:
            self.paint_id = DRAW_CIRCLE
        elif button == Qt.RightButton:
            self.paint_id = DRAW_RECTANGLE
        self.runDraw()

    def mouseMoveEvent(self, event):
        self.coords = [event.x(), event.y()]

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Space:
            self.paint_id = DRAW_TRIANGLE
            self.runDraw()



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
