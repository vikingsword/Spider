import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target = "https://www.biquge7.top/50043/1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    req = requests.get(url=target, headers=headers)
    req.encoding = 'utf-8'
    html = req.text
    print(html)
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.find('h1', id='tit')
    # print(text)