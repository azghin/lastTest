# second_win.py
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime
from instr import *
from final_win import FinalWin, Experiment

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.name_label = QLabel('Enter your full name:')
        self.name_input = QLineEdit('Full name')
        self.age_label = QLabel('Enter your age:')
        self.age_input = QLineEdit('0')
        self.test1_label = QLabel('Enter the result of the first test:')
        self.test1_input = QLineEdit('0')
        self.test1_button = QPushButton('Start the first test')
        self.test2_label = QLabel('Enter the result of the second test:')
        self.test2_input = QLineEdit('0')
        self.test2_button = QPushButton('Start doing squats')
        self.test3_label = QLabel('Enter the result of the third test:')
        self.test3_input = QLineEdit('0')
        self.test3_button = QPushButton('Start final test')
        self.text_timer = QLabel('00:00:00')
        self.text_timer.setStyleSheet('font-size: 20px;')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.age_label)
        self.layout.addWidget(self.age_input)
        self.layout.addWidget(self.text_timer)
        self.layout.addWidget(self.test1_label)
        self.layout.addWidget(self.test1_input)
        self.layout.addWidget(self.test1_button)
        self.layout.addWidget(self.test2_label)
        self.layout.addWidget(self.test2_input)
        self.layout.addWidget(self.test2_button)
        self.layout.addWidget(self.test3_label)
        self.layout.addWidget(self.test3_input)
        self.layout.addWidget(self.test3_button)
        self.setLayout(self.layout)

    def connects(self):
        self.test1_button.clicked.connect(self.timer_test)
        self.test2_button.clicked.connect(self.timer_squats)
        self.test3_button.clicked.connect(self.timer_final)
        self.test3_button.clicked.connect(self.next_click)

    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setStyleSheet('color: rgb(0, 255, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer_squats(self):
        global time
        time = QTime(0, 0, 45)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1000)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        if time.toString('hh:mm:ss') <= '00:00:59' and time.toString('hh:mm:ss') > '00:00:45':
            self.text_timer.setStyleSheet('color: rgb(0, 255, 0)')
        else:
            self.text_timer.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def next_click(self):
        try:
            age = int(self.age_input.text())
            t1 = int(self.test1_input.text())
            t2 = int(self.test2_input.text())
            t3 = int(self.test3_input.text())
            if age < 7 or t1 <= 0 or t2 <= 0 or t3 <= 0:
                raise ValueError
            self.hide()
            self.fw = FinalWin(Experiment(age, t1, t2, t3))
        except ValueError:
            self.age_input.setText('0')
            self.test1_input.setText('0')
            self.test2_input.setText('0')
            self.test3_input.setText('0')