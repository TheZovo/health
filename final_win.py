from instr import *
from final_win import *

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout

class FinalWin(QWidget):
    def __init__(self, index, result):
        super().__init__()
        self.index = index
        self.result = result
        self.init_UI()
        self.set_appear()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def init_UI(self):
        self.index_text = QLabel(f"{txt_index} {self.index}")
        self.result_text = QLabel(f"{txt_workheart} {self.result}")
        self.index_text.setAlignment(Qt.AlignCenter)
        self.result_text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index_text)
        self.layout.addWidget(self.result_text)

        self.setLayout(self.layout)


    def connects(self):
        self.btn_next.clicked.connect(self.next_click)