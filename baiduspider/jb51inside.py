import re
import requests
from bs4 import BeautifulSoup

bookid = 606001
url = 'https://www.jb51.net/books/%d.html' % bookid
r = requests.get(url)
r.encoding = 'gbk'
soup = BeautifulSoup(r.text, 'lxml')
title = str(soup.title.contents[0])
title = title.rstrip(' 电子书 下载-脚本之家')
print(title)

baidulinks_temp = soup.find_all({'a'})
for link in baidulinks_temp:
    link = str(link)
    if 'baidu' in link:
        res = re.findall('<a href=".*?"', link)[0]
        res = res.lstrip('<a href="').rstrip('"')
        print(res)