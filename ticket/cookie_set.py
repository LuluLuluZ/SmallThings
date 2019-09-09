import pickle
from selenium import webdriver


def cookie_set():
    login_url='https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F'

    driver = webdriver.Chrome(executable_path='../chromedriver')
    driver.implicitly_wait(0.3)
    driver.get(login_url)
    iframe = driver.find_element_by_id('alibaba-login-box')
    driver.switch_to.frame(iframe)
    driver.find_elements_by_class_name('login-tabs-tab')[2].click()
    while 1:
        if driver.title == '大麦网-全球演出赛事官方购票平台-100%正品、先付先抢、在线选座！':
            pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
            break
    driver.quit()