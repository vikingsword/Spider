import io
import time
import urllib
import requests
from bs4 import BeautifulSoup


# 笔趣阁小说爬虫
# 6.84 --- 7.49
from tqdm import tqdm


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
    content = ''
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
    texts_parse = texts.text.strip().replace('\xa0', '')
    # join content
    content = texts_parse + '\n\n'
    return content.encode('utf-8')


if __name__ == '__main__':
    t1 = time.time()
    example = "https://www.biquge7.top/50043"
    con = input('please input novel url(such as ' + example + '): ')
    # domain parse
    target = urllib.parse.urlparse(con).netloc
    # scheme parse
    scheme = urllib.parse.urlparse(con).scheme

    soup = getSoup(con)

    bookName = soup.find('h1')
    linkList = soup.find('div', attrs={'class', 'list'}).find_all('a')

    for i in tqdm(linkList):
        url = scheme + '://' + target + i['href']
        title = str(i['title']).replace(' ', ' ')

        cont = getUnitContent()
        res = title + '\n' + str(cont)

        # file output
        fileName = bookName.text + '.txt'

        file = io.open(fileName, 'a', encoding='utf-8')
        file.write(res)
        file.close()
    t2 = time.time()
    print('下载用时' + str(t2 - t1))

    print('download successful!')
