import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://www.gongzicp.com/novel-20626.html'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
temp = soup.find_all('b')
length = str(temp[4].contents[0])
score = str(temp[5].contents[0])
if '万' in length:
    length = int(float(length.rstrip('万')) * 10000)
if '万' in score:
    score = int(float(score.rstrip('万')) * 10000)

print('字数：%d' % length)
print('人气：%d' % score)
print('-'*30)

intro = soup.find_all('p')
for i in intro[:-3]:
    i = str(i)
    if re.search('<p>.*?</p>', i) is not None:
        i = i.lstrip('<p>').rstrip('</p>')
        if len(i) == 1:
            print('')
            continue
        print(i)


print('-'*30)
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='../../chromedriver')
driver.get(url)

linkids_temp = re.findall('><a href="/read-.*?"><span', driver.page_source)
linkids = []
print('-'*30)
for linkid in linkids_temp[1:]:
    linkid = linkid.lstrip('><a href="').rstrip('"><span')
    linkids.append(linkid)
print(linkids)
print('共%s章' % len(linkids))
driver.close()