import io
import queue
import threading
import urllib
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import os


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


def getContent():
    while not que.empty():
        global content, count
        global fileName
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        res = que.get()
        url = str(res).split('|')[0]
        title = str(res).split('|')[1]
        number = str(res).split('|')[2]

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
        # print(texts_parse)
        # join content
        content = texts_parse + '\n\n'
        content.encode('utf-8')

        res = title + '\n' + content
        # file output
        fileName = bookName.text + '.txt'

        # 按顺序写入
        if count == int(number) - 1:
            file = io.open(fileName, 'a', encoding='utf-8')
            count = count + 1
            file.write(res)
            file.close()


if __name__ == '__main__':
    example = "https://www.biquge7.top/50043"
    con = input('please input novel url(such as ' + example + '): ')
    # domain parse
    target = urllib.parse.urlparse(con).netloc
    # scheme parse
    scheme = urllib.parse.urlparse(con).scheme

    soup = getSoup(con)

    bookName = soup.find('h1')
    linkList = soup.find('div', attrs={'class', 'list'}).find_all('a')

    que = queue.Queue()
    for i in linkList:
        url = scheme + '://' + target + i['href']
        number = str(i['href']).split('/')[2]
        title = str(i['title']).replace(' ', ' ')
        que.put(url + '|' + title + '|' + number)

    for thread in tqdm(range(100)):
        try:
            t = threading.Thread(target=getContent)
            t.start()
        except Exception as e:
            pass

    # file_size = os.path.getsize('./' + fileName)
    # print("File Size is :", file_size)
    # print('download successful!')
