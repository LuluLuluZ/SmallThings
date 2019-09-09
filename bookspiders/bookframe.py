import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTableWidget, QLineEdit, QHBoxLayout, \
    QVBoxLayout
from bookspiders.jinjiang.get_book_content import get_book_content
from bookspiders.jinjiang.get_ranking import get_ranking


class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 200, 300, 300)
        self.setWindowTitle('My小说选择器')

        lb1 = QLabel('FROM PAGE')
        lb2 = QLabel('TO PAGE')
        self.page1entry = QLineEdit()
        self.page2entry = QLineEdit()
        self.page1entry.textEdited.connect(self.get_page1)
        self.page2entry.textEdited.connect(self.get_page2)
        hbox_page = QHBoxLayout()
        hbox_page.addWidget(lb1)
        hbox_page.addWidget(self.page1entry)
        hbox_page.addWidget(lb2)
        hbox_page.addWidget(self.page2entry)

        bt1 = QPushButton('按积分选书', self)
        bt1.clicked.connect(self.show_books)
        self.chapter = 1
        bt2 = QPushButton('试看', self)
        bt2.clicked.connect(self.get_content)
        bt3 = QPushButton('下一章', self)
        bt3.clicked.connect(self.next_chapter)
        hbox_button = QHBoxLayout()
        hbox_button.addWidget(bt1)
        hbox_button.addWidget(bt2)
        hbox_button.addWidget(bt3)

        whole_layout = QVBoxLayout()
        whole_layout.addLayout(hbox_page)
        whole_layout.addLayout(hbox_button)

        self.setLayout(whole_layout)
        self.show()

    def get_page1(self):
        try:
            self.page1 = self.page1entry.text()
        except Exception as e:
            print(e)

    def get_page2(self):
        try:
            self.page2 = self.page2entry.text()
        except Exception as e:
            print(e)

    def show_books(self):
        self.table = QTableWidget(self)
        self.table.setSelectionBehavior(1)
        self.table.setRowCount(5)

        try:
            for page in (self.page1, self.page2):
                book_list = get_ranking(page)
                self.table.setColumnCount(len(book_list))
                self.table.setHorizontalHeader('书名', '作者', '简介', 'tag', 'id')
                for i in range(0, len(book_list)):
                    for j in range(0, 5):
                        self.table.setItem(i, j, book_list[i][i])
        except IndexError:
            pass

    def get_novelid(self):
        return 12345

    def get_content(self):
        novelid = self.get_novelid()
        text = get_book_content(novelid, self.chapter)
        self.lb.setText(text)
        self.lb.adjustSize()

    def next_chapter(self):
        self.chapter += 1
        self.get_content()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Win()
    sys.exit(app.exec_())