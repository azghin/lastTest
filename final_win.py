# final_win.py
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from instr import *

class Experiment:
    def __init__(self, age, t1, t2, t3):
        self.age = age
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.index = self.results()
        self.index_text = QLabel(txt_index + str(self.index))
        self.work_text = QLabel(txt_workheart + self.get_performance())
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index_text)
        self.layout.addWidget(self.work_text)
        self.setLayout(self.layout)

    def results(self):
        return (4 * (self.exp.t1 + self.exp.t2 + self.exp.t3) - 200) / 10

    def get_performance(self):
        index = self.index
        age = self.exp.age
        if age >= 15:
            if index >= 15:
                return txt_res1
            elif 11 <= index < 15:
                return txt_res2
            elif 6 <= index < 11:
                return txt_res3
            elif 0.5 <= index < 6:
                return txt_res4
            else:
                return txt_res5
        elif 13 <= age <= 14:
            if index >= 16.5:
                return txt_res1
            elif 12.5 <= index < 16.5:
                return txt_res2
            elif 7.5 <= index < 12.5:
                return txt_res3
            elif 2 <= index < 7.5:
                return txt_res4
            else:
                return txt_res5
        elif 11 <= age <= 12:
            if index >= 18:
                return txt_res1
            elif 14 <= index < 18:
                return txt_res2
            elif 9 <= index < 14:
                return txt_res3
            elif 3.5 <= index < 9:
                return txt_res4
            else:
                return txt_res5
        elif 9 <= age <= 10:
            if index >= 19.5:
                return txt_res1
            elif 15.5 <= index < 19.5:
                return txt_res2
            elif 10.5 <= index < 15.5:
                return txt_res3
            elif 5 <= index < 10.5:
                return txt_res4
            else:
                return txt_res5
        else:  # Age 7-8
            if index >= 21:
                return txt_res1
            elif 17 <= index < 21:
                return txt_res2
            elif 12 <= index < 17:
                return txt_res3
            elif 6.5 <= index < 12:
                return txt_res4
            else:
                return txt_res5