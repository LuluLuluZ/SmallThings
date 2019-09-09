import requests
from bs4 import BeautifulSoup
from time import sleep


def get_book_content(novel_id, chapter):
    url = 'http://www.jjwxc.net/onebook.php?novelid=%s&chapterid=' % novel_id
    url = url + str(chapter)
    r = requests.get(url)
    r.encoding = 'gbk'
    soup = BeautifulSoup(r.text, 'lxml')
    text = soup.find_all(attrs={'class': 'noveltext'})[0].contents

    chapter_whole = ''

    chapter_title = text[3].contents[0].contents[0]
    chapter_whole += chapter_title

    chapter_whole += '\n'
    i = 6
    while i < len(text) - 14:
        chapter_whole += '    '
        chapter_whole += str(text[i]).strip()
        chapter_whole += '\n'
        i += 2

        writer_words = text[-8].contents[1]
        if type(writer_words) == 'str':
            chapter_whole += writer_words


if __name__ == '__main__':
    file = open('欢迎来到噩梦游戏', 'a')
    page_num = 38
    for i in range(37, page_num):
        try:
            sleep(1)
        except Exception:
            print('第%s章被锁' % i)
            file.write('第%s章被锁' % i)
    file.close()