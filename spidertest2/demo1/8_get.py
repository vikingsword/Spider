import io

import requests
from bs4 import BeautifulSoup


def getUnitContent():
    global content
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    req = requests.get(url=target, headers=headers)
    req.encoding = 'utf-8'
    html = req.text
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    # get title
    title_parse = soup.find('title').text.removesuffix('-新笔趣阁').replace(' ', ' ')
    # get texts
    texts = soup.find('div', attrs={'class', 'text'})
    texts_parse = texts.text.strip().replace('\xa0', '').replace('”嫩嫩的新书，向大家打声招呼，别忘记收藏，请多支持，后面还有章节。', '')
    # join content
    content = title_parse + '\n' + texts_parse + '\n\n'
    content.encode('utf-8')


if __name__ == '__main__':
    # 1 - 1155
    con = "https://www.biquge7.top/50043/"
    for i in range(1, 1156):
        target = con + (str(i))

        # get novel chapter content
        getUnitContent()

        # file output
        file = io.open('深空彼岸.txt', 'a', encoding='utf-8')
        file.write(content)
        file.close()
