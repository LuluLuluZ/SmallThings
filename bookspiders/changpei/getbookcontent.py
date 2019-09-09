from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chapter_id = '/read-287784.html'
url = 'https://www.gongzicp.com' + chapter_id

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='../../chromedriver')
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
tag_ps = soup.find_all('p')
for tag_p in tag_ps[1:]:
    tag_p_content = tag_p.contents[0]
    if 'VIP' in tag_p_content:
        break
    print(tag_p_content)

file = open('你的虎牙很适合咬我的腺体ABO.txt,', 'a')
file.write('1')
file.close()