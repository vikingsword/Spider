import io

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 1 - 1155
    target = "https://www.biquge7.top/50043/1"
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
    content = title_parse + '\n' + texts_parse
    content.encode('utf-8')

    # file output
    file = io.open('novel.txt', 'w', encoding='utf-8')
    file.write(content)
    file.close()
