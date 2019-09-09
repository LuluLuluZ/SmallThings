from time import sleep
from selenium import webdriver

driver = webdriver.Chrome(executable_path='../../chromedriver')
url = 'https://www.gongzicp.com/read-287784.html'
driver.get(url)
link = driver.find_element_by_xpath('//*[@id="cpReadSetting"]/a[3]/p[1]')
sleep(5)
link.click()