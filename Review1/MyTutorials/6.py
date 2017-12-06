import sys
from PyQt5.QtWidgets import (QLabel, QCheckBox, QPushButton, QVBoxLayout, QApplication, QWidget)


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel()
        self.chx = QCheckBox('Check 1')
        self.btn = QPushButton('Press')

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.chx)
        layout.addWidget(self.btn)

        self.setLayout(layout)

        self.btn.clicked.connect(lambda: self.btn_clk(self.chx.isChecked(), self.lbl))

        self.show()

    def btn_clk(self, chk, lbl):
        if chk:
            lbl.setText('Checked')
        else:
            lbl.setText('Unchecked')


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())