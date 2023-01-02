import requests
from bs4 import BeautifulSoup


def getSoup():
    url = 'https://www.biquge7.top/34936/1'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    req = requests.get(url=url, headers=headers)
    req.encoding = 'utf-8'
    html = req.text
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    return soup
    pass


if __name__ == '__main__':
    soup2 = getSoup()
    texts = soup2.find('div', attrs={'class', 'text'})
    # texts_parse = texts.text.strip().replace('\xa0', '').replace('”嫩嫩:', '')
    texts_parse = texts.text.strip().replace('\xa0', '')
    print(texts_parse)

