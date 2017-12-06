import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget)


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel('Select a answer')
        self.dog = QRadioButton('A')
        self.cat = QRadioButton('B')
        self.btn = QPushButton('Select')

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.dog)
        layout.addWidget(self.cat)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 Lesson 10')

        self.btn.clicked.connect(lambda: self.btn_clk(self.dog.isChecked(), self.lbl))

        self.show()

    def btn_clk(self, chk, lbl):
        if chk:
            lbl.setText('A is your answer')
        else:
            lbl.setText('B is your answer')

app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())