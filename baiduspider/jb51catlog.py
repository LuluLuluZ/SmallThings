import re
from time import sleep
import requests
from bs4 import BeautifulSoup

for i in range(1, 14):
    url = 'https://www.jb51.net/books/list476_%d.html' % i
    r = requests.get(url)
    r.encoding = 'gbk'
    soup = BeautifulSoup(r.text, 'lxml')
    lis = soup.find_all('li')

    for li in lis:
        li = str(li)
        if 'class="tit"' in li:
            title = re.findall('href="/book.*?html', li)
            intro = re.findall('desc">.*?<', li)
            bookid = re.findall('blank">.*?</a>', li)
            try:
                title = title[0].lstrip('href="/books/').rstrip('.html')
                intro = intro[0].lstrip('desc">').rstrip('<')
                bookid = bookid[0].lstrip('blank">').rstrip('</a>')
            except IndexError:
                print('IndexError')
            print(title + ':' + str(bookid))

    sleep(2)