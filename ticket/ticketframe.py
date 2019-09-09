import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QListWidget
from ticket.buyticket import BuyTicket
from ticket.new_concert import new_concert
from ticket.cookie_set import cookie_set


class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(500, 230)
        self.setWindowTitle('欧皇附体，顺利抢票')

        bt1 = QPushButton('有无上新', self)
        bt1.clicked.connect(self.show_new_concert)
        bt2 = QPushButton('事前准备', self)
        bt2.clicked.connect(cookie_set)
        bt3 = QPushButton('开始抢票', self)
        bt3.clicked.connect(self.buy_ticket)

        lb1 = QLabel("网站：", self)
        lb2 = QLabel("日期：", self)
        lb3 = QLabel("价位：", self)
        lb4 = QLabel("票数：", self)
        le1 = QLineEdit()
        le1.textEdited.connect(self.set_url)
        le2 = QLineEdit()
        le2.setMaxLength(2)
        le2.textEdited.connect(self.set_date)
        le3 = QLineEdit()
        le3.setMaxLength(2)
        le3.textEdited.connect(self.set_price)
        le4 = QLineEdit()
        le4.setMaxLength(2)
        le4.textEdited.connect(self.set_ticket_num)

        lb5 = QLabel("ATTENTION", self)
        lb6 = QLabel("1. 选座要手选", self)
        lb7 = QLabel("2. 日期价位填序号", self)

        hbox_warning = QHBoxLayout()
        hbox_warning.addWidget(lb5)
        hbox_warning.addWidget(lb6)
        hbox_warning.addWidget(lb7)

        grid = QGridLayout()
        grid.addWidget(lb1, 1, 1)
        grid.addWidget(le1, 1, 2)
        grid.addWidget(lb2, 1, 3)
        grid.addWidget(le2, 1, 4)
        grid.addWidget(lb3, 2, 1)
        grid.addWidget(le3, 2, 2)
        grid.addWidget(lb4, 2, 3)
        grid.addWidget(le4, 2, 4)

        hbox_bt = QHBoxLayout()
        hbox_bt.addWidget(bt1)
        hbox_bt.addWidget(bt2)
        hbox_bt.addWidget(bt3)

        vbox_whole = QVBoxLayout()
        vbox_whole.addLayout(hbox_warning)
        vbox_whole.addLayout(grid)
        vbox_whole.addLayout(hbox_bt)

        self.setLayout(vbox_whole)
        self.show()

    def show_new_concert(self):
        concert_list = new_concert()
        concert_list_win = QListWidget(self)
        concert_list_win.addItems(concert_list)

    def set_url(self):
        self.url = self.le1.text()

    def set_date(self):
        self.date = self.le1.text()

    def set_price(self):
        self.price = self.le1.text()

    def set_ticket_num(self):
        self.ticket_num = self.le1.text()

    def buy_ticket(self):
        buytic = BuyTicket(self.url, self.time, self.price, self.ticket_num)
        buytic.buy()
        buytic.choose_seat()
        buytic.ship_info()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Win()
    sys.exit(app.exec_())