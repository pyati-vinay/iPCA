import sys
from PyQt5 import QtWidgets, QtGui


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)
    l2 = QtWidgets.QLabel(w)
    l1.setText('Hello World')
    w.setWindowTitle('PyQt 1')
    w.setGeometry(100, 100, 300, 200)
    l1.move(100, 20)
    l2.move(120, 90)
    w.show()
    sys.exit(app.exec_())


window()