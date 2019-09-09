import pickle
from time import sleep
from tkinter import *
from selenium import webdriver
from ticket.cookie_set import cookie_set


class BuyTicket:
    def __init__(self, url, time, price, ticket_num):
        self.driver = webdriver.Chrome(executable_path='../chromedriver')
        self.url = url
        self.driver.get(self.url)
        self.driver.implicitly_wait(0.5)
        self.set_cookie()
        self.driver.refresh()
        self.title = self.driver.title
        self.time = time
        self.price = price
        self.ticket_num = ticket_num

    def set_cookie(self):
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            cookie_dict = {
                'domain': '.damai.cn',
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                "expires": "",
                'path': '/',
                'httpOnly': False,
                'HostOnly': False,
                'Secure': False}
            self.driver.add_cookie(cookie_dict)

    def select_time(self):
        try:
            self.driver.find_elements_by_class_name('select_right_list_item')[self.time-1].click()
        except Exception as e:
            print(e)

    def select_price(self):
        try:
            self.driver.find_elements_by_class_name('skuname')[self.price-1].click()
        except Exception as e:
            print(e)

    def plus_tickets(self):
        self.ticket_bt = self.driver.find_element_by_class_name('cafe-c-input-number-input')
        self.ticket_bt.click()
        self.ticket_bt.clear()
        self.ticket_bt.send_keys(self.ticket_num)

    def buy(self):
        if self.time != 1:
            self.select_time()
        if self.price != 1:
            self.select_price()
        if self.ticket_num != 1:
            self.plus_tickets()
        while self.driver.title == self.title:
            self.driver.find_element_by_class_name('buybtn').click()
            sleep(0.5)

    def choose_seat(self):
        if self.driver.title == '选座购买':
            # 启动手选模式
            while 1:
                if self.driver.title == '确认订单':
                    break

    def ship_info(self):
        try:
            checkbox = self.driver.find_element_by_css_selector('input[type=checkbox]')
            if not checkbox.is_selected():
                checkbox.click()
            sleep(2)
            self.driver.find_elements_by_tag_name('button')[-1].click()
            if self.driver.title == '支付宝 - 网上支付':
                print('购票成功')
        except Exception as e:
            print(e)