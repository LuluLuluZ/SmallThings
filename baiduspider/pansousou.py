import requests
from bs4 import BeautifulSoup

keyword = '机甲契约'
url = 'http://www.pansoso.com/%s' % keyword

r = requests.get(url)
r.encoding = 'gbk'
soup = BeautifulSoup(r.text, 'lxml')
pss = soup.find_all(attrs={"class": "pss"})
print(pss)