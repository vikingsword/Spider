import io
import urllib

import requests
from bs4 import BeautifulSoup

# 笔趣阁小说爬虫

def getSoup(target):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    req = requests.get(url=target, headers=headers)
    req.encoding = 'utf-8'
    html = req.text
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def getUnitContent():
    global content
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    req = requests.get(url=url, headers=headers)
    req.encoding = 'utf-8'
    html = req.text
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    # get title
    # title_parse = soup.find('title').text.removesuffix('-新笔趣阁').replace(' ', ' ')
    # get texts
    texts = soup.find('div', attrs={'class', 'text'})
    texts_parse = texts.text.strip().replace('\xa0', '').replace('”嫩嫩的新书，向大家打声招呼，别忘记收藏，请多支持，后面还有章节。', '')
    # join content
    content = texts_parse + '\n\n'
    content.encode('utf-8')


if __name__ == '__main__':
    # con = "https://www.biquge7.top/50043"
    con = input('please input novel url: ')
    # domain parse
    target = urllib.parse.urlparse(con).netloc
    # scheme parse
    scheme = urllib.parse.urlparse(con).scheme

    soup = getSoup(con)

    bookName = soup.find('h1')
    linkList = soup.find('div', attrs={'class', 'list'}).find_all('a')

    for i in linkList:
        url = scheme + '://' + target + i['href']
        title = str(i['title']).replace(' ', ' ')

        getUnitContent()
        res = title + '\n' + content

        # file output
        fileName = bookName.text + '.txt'

        file = io.open(fileName, 'a', encoding='utf-8')
        file.write(res)
        file.close()

    print('download successful!')