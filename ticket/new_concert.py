import re
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def new_concert():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path='../chromedriver', chrome_options=chrome_options)
    concert_list = []

    names = ['周杰伦', '陈奕迅', '吴亦凡', 'tfboys', '蔡徐坤', '吴亦凡', 'EXO']
    for name in names:
        sleep(2)
        url = 'https://search.damai.cn/search.html?keyword=%s&spm=a2oeg.search_category.searchtxt.dsearchbtn' % name
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        results = soup.find_all(attrs={"class": "items__txt__title"})
        if len(results) == 0:
            continue
        else:
            for result in results:
                try:
                    title = re.findall('"c4">.*?</a>', str(result))[0]
                    title = str(title).lstrip('"c4">').rstrip('</a>').replace('</span>', '///')
                    concert_list.append(title)
                    print(title)
                except IndexError:
                    print('网页结构可能发生改变')
                driver.close()

    driver.quit()
    return concert_list
