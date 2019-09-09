from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_proxy():
    ip_list = []
    url = 'https://www.xicidaili.com/'

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path='../chromedriver', chrome_options=chrome_options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    results = soup.find_all(attrs={'class': 'odd'})
    for result in results:
        content = result.contents
        ip_temp = content[3]
        ip = str(ip_temp).lstrip('<td>').rstrip('</td>')
        ip_list.append(ip)

    driver.close()
    driver.quit()
    return ip_list


if __name__ == '__main__':
    proxies = get_proxy()
    print(proxies)
