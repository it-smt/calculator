from math import sqrt

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QLabel, QLCDNumber, QPushButton, QHBoxLayout, QVBoxLayout


class MainWindow(QWidget):
    """Калькулятор"""

    def __init__(self):
        """Инициализация."""
        super().__init__()
        self.label = QLabel(self)
        self.lcd = QLCDNumber(self)
        self.button_0 = QPushButton("0", self)
        self.button_1 = QPushButton("1", self)
        self.button_2 = QPushButton("2", self)
        self.button_3 = QPushButton("3", self)
        self.button_4 = QPushButton("4", self)
        self.button_5 = QPushButton("5", self)
        self.button_6 = QPushButton("6", self)
        self.button_7 = QPushButton("7", self)
        self.button_8 = QPushButton("8", self)
        self.button_9 = QPushButton("9", self)
        self.button_dot = QPushButton(".", self)
        self.button_plus = QPushButton("+", self)
        self.button_minus = QPushButton("-", self)
        self.button_mul = QPushButton("*", self)
        self.button_div = QPushButton("/", self)
        self.button_sqr = QPushButton("xⁿ", self)
        self.button_sqr.setToolTip("Комбинация клавиш: shift+^")
        self.button_sqrt = QPushButton("√", self)
        self.button_sqrt.setToolTip("Клавиша: s, запись: число√=")
        self.button_equal = QPushButton("=", self)
        self.button_0.clicked.connect(self.number_click)
        self.button_1.clicked.connect(self.number_click)
        self.button_2.clicked.connect(self.number_click)
        self.button_3.clicked.connect(self.number_click)
        self.button_4.clicked.connect(self.number_click)
        self.button_5.clicked.connect(self.number_click)
        self.button_6.clicked.connect(self.number_click)
        self.button_7.clicked.connect(self.number_click)
        self.button_8.clicked.connect(self.number_click)
        self.button_9.clicked.connect(self.number_click)
        self.button_dot.clicked.connect(self.number_click)
        self.button_plus.clicked.connect(self.operation_click)
        self.button_minus.clicked.connect(self.operation_click)
        self.button_mul.clicked.connect(self.operation_click)
        self.button_div.clicked.connect(self.operation_click)
        self.button_sqr.clicked.connect(self.operation_click)
        self.button_sqrt.clicked.connect(self.operation_click)
        self.button_equal.clicked.connect(self.get_result)
        self.expression = ''
        self.number = ''
        self.number2 = ""
        self.result = ""
        self.init_ui()

    def init_ui(self):
        """UI."""
        self.resize(250, 321)
        self.setWindowTitle("Калькулятор")
        self.setWindowIcon(QIcon(r"calculator\img\caculation.png"))
        self.lcd.setMaximumHeight(300)
        self.label.setMaximumHeight(10)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.lcd, 5)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_0)
        hbox.addWidget(self.button_1)
        hbox.addWidget(self.button_2)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_3)
        hbox.addWidget(self.button_4)
        hbox.addWidget(self.button_5)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_6)
        hbox.addWidget(self.button_7)
        hbox.addWidget(self.button_8)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_plus)
        hbox.addWidget(self.button_9)
        hbox.addWidget(self.button_minus)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_mul)
        hbox.addWidget(self.button_div)
        hbox.addWidget(self.button_dot)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_sqr)
        hbox.addWidget(self.button_sqrt)
        hbox.addWidget(self.button_equal)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def number_click(self):
        """Функция для обработки сигналов нажатия на кнопки с цифрами."""
        sender = self.sender()
        self.use_numbers(sender.text())

    def operation_click(self):
        """Функция для обработки сигналов нажатия на кнопки с действиями."""
        sender = self.sender()
        self.use_operation(sender.text())

    def keyPressEvent(self, event):
        """
        Функция обработчик нажатия клавиши.
        :param event: хранит состояние клавиш.
        """
        if event.key() == Qt.Key.Key_Escape:
            self.close()
        if event.key() == Qt.Key.Key_Backspace:
            self.erase()
            self.lcd.display("0")
        if event.key() == Qt.Key.Key_0:
            self.use_numbers("0")
        elif event.key() == Qt.Key.Key_1:
            self.use_numbers("1")
        elif event.key() == Qt.Key.Key_2:
            self.use_numbers("2")
        elif event.key() == Qt.Key.Key_3:
            self.use_numbers("3")
        elif event.key() == Qt.Key.Key_4:
            self.use_numbers("4")
        elif event.key() == Qt.Key.Key_5:
            self.use_numbers("5")
        elif event.key() == Qt.Key.Key_6:
            self.use_numbers("6")
        elif event.key() == Qt.Key.Key_7:
            self.use_numbers("7")
        elif event.key() == Qt.Key.Key_8:
            self.use_numbers("8")
        elif event.key() == Qt.Key.Key_9:
            self.use_numbers("9")
        elif event.key() == 46:
            self.use_numbers(".")
        elif event.key() == Qt.Key.Key_Plus:
            self.use_operation("+")
        elif event.key() == Qt.Key.Key_Minus:
            self.use_operation("-")
        elif event.key() == 42:
            self.use_operation("*")
        elif event.key() == 47:
            self.use_operation("/")
        elif event.key() == 94 or event.key() == 58:
            self.use_operation("xⁿ")
        elif event.key() == 83 or event.key() == 1067:
            self.use_operation("√")
        elif event.key() == 61:
            self.get_result()

    def get_result(self):
        """Функция вычисления и вывода результата."""
        try:
            if self.expression == "xⁿ":
                self.result = eval(self.number + "**" + self.number2)
            elif self.expression == "√":
                self.result = sqrt(eval(self.number))
            else:
                self.result = eval(self.number + self.expression + self.number2)
        except:
            self.result = "Err"
        self.lcd.display(self.result)
        self.erase()

    def use_operation(self, operation):
        """
        Функция вывода операции.
        :param operation: операция, которую ввел пользователь.
        """
        self.expression = operation
        self.lcd.display("")

    def use_numbers(self, number):
        """
        Функция вывода числа.
        :param number: число, которое ввел пользователь.
        """
        if self.expression != "":
            self.number2 += number
            self.lcd.display(self.number2)
        else:
            self.number += number
            self.lcd.display(self.number)

    def erase(self):
        """Функция обнуления."""
        self.number = ""
        self.number2 = ""
        self.result = ""
        self.expression = ""
