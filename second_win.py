from instr import *
from final_win import *

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()
        self.connects()
        self.show()
        self.set_appear()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def init_UI(self):
        self.btn_next = QPushButton(txt_next, self)
        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.btn_test3 = QPushButton(txt_starttest3, self)
        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)
        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_name = QLineEdit(txt_hintname)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)
        
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        self.r_line.addWidget(self.text_timer, alignment=Qt.AlignCenter)
        self.r_line.addWidget(self.text_name, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.line_name, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.text_age, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.line_age, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.text_test1, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.btn_test1, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.line_test1, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.text_test2, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.btn_test2, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.text_test3, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.btn_test3, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.line_test2, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.line_test3, alignment=Qt.AlignLeft)
        self.r_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)



    def next_click(self):
        self.tw = FinalWin()  # Не забудьте подключить TestWin, когда понадобится
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)