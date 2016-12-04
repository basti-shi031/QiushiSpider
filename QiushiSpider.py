import requests
from bs4 import BeautifulSoup

# url地址:
# http://www.qiushibaike.com/hot/page/2/?s=4936224
page = 1
originUrl = 'http://www.qiushibaike.com/hot/page/'


def fetch_qiushi_result(page):
    res = requests.get(originUrl + str(page))
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup)
    for qiushi in soup.select('.article'):
        print(qiushi.select('.content')[0].text)


fetch_qiushi_result(1)
