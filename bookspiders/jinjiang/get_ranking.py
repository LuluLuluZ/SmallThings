import requests
from bs4 import BeautifulSoup
import re


def get_ranking(page):
    this_page = []
    url = 'http://www.jjwxc.net/bookbase_slave.php?booktype=&opt=&page=%d&endstr=true&orderstr=1' % page
    r = requests.get(url)
    r.encoding = 'gbk'
    soup = BeautifulSoup(r.text, 'lxml')
    infos = soup.find_all('tr')

    for info in infos:
        info = str(info)

        if '纯爱' in info and '原创' in info and '悲剧' not in info:
            length_score = re.findall('right">.*?</td>', info)
            score = length_score[1].lstrip('right">').rstrip('</td>')
            score = int(score)

            if score < 100000000:
                continue
            else:
                writer_title = re.findall('_blank">.*?</a>', info)
                writer = writer_title[0].lstrip('_blank">').rstrip('</a>')
                title = writer_title[1].lstrip('_blank">').rstrip('</a>')

                try:
                    intro = re.findall('rel=".*?&lt', info)[0]
                    intro = intro.lstrip('rel="').rstrip('&lt')
                except IndexError:
                    intro = ''

                try:
                    tag = re.findall('标签：.*?"', info)[0]
                    tag = tag.lstrip('标签：').rstrip('"')
                except IndexError:
                    tag = ''

                id = re.findall('"tooltip" href=".*?"', info)[0]
                id = id.lstrip('"tooltip" href="onebook.php?novelid=').rstrip('"')
                id = int(id)

                this_book = [title, writer, intro, tag, id]
                this_page.append(this_book)

    return this_page


if __name__ == '__main__':
    for page in range(30, 41):
        books = get_ranking(page)
        print(books)