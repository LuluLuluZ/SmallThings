import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from game.arknights import get_material, daily
from game.producer import producer_daily


class Win(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.resize(300, 100)
		self.setWindowTitle('游戏刷刷刷')

		# game1
		lb_arknights = QLabel('明日方舟', self)
		bt1 = QPushButton('刷刷刷', self)
		bt1.clicked.connect(get_material)
		bt2 = QPushButton('杂事一扫光', self)
		bt2.clicked.connect(daily)

		hbox_arknights = QHBoxLayout()
		hbox_arknights.addWidget(bt1)
		hbox_arknights.addWidget(bt2)

		# game2
		lb_nikki = QLabel('闪耀暖暖', self)
		bt3 = QPushButton('每日一套', self)
		bt3.clicked.connect(get_material)
		bt4 = QPushButton('无脑过剧情', self)
		bt4.clicked.connect(daily)

		hbox_nikki = QHBoxLayout()
		hbox_nikki.addWidget(bt3)
		hbox_nikki.addWidget(bt4)

		# game3
		lb_producer = QLabel('恋与制作人', self)
		bt5 = QPushButton('每日一套', self)
		bt5.clicked.connect(producer_daily)
		bt6 = QPushButton('无脑过剧情', self)
		bt6.clicked.connect(producer_daily)

		hbox_producer = QHBoxLayout()
		hbox_producer.addWidget(bt5)
		hbox_producer.addWidget(bt6)

		# 总布局
		vbox = QVBoxLayout()
		vbox.addWidget(lb_arknights)
		vbox.addLayout(hbox_arknights)
		vbox.addWidget(lb_nikki)
		vbox.addLayout(hbox_nikki)
		vbox.addWidget(lb_producer)
		vbox.addLayout(hbox_producer)

		self.setLayout(vbox)

		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Win()
	sys.exit(app.exec_())