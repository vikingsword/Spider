import urllib

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    con = "https://www.biquge7.top/50043"
    # domain parse
    target = urllib.parse.urlparse(con).netloc

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    req = requests.get(url=con, headers=headers)
    req.encoding = 'utf-8'
    html = req.text
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')

    linkList = soup.find('div', attrs={'class', 'list'}).find_all('a')

    for i in linkList:
        href = i['href']
        url = target + href
        title = i['title']
        print(title)

    # print(linkList)
