import urllib.parse

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # get link and title
    target = 'http://www.ntyou.cc/video/4190.html'

    # url parser
    netloc = urllib.parse.urlparse(target).netloc
    scheme = urllib.parse.urlparse(target).scheme
    print(netloc)
    print(scheme)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    req = requests.get(url=target, headers=headers)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    linkList = soup.find('div', attrs={'class', 'movurl mod'}).find_all('a')
    for i in linkList:
        # http://www.ntyou.cc/play/4190-1-1.html
        # todo download link is in #document  
        url = scheme + '://' + netloc + i['href']
        req2 = requests.get(url=url, headers=headers)
        html2 = req2.text
        print(html2)
        soup2 = BeautifulSoup(html2, 'html.parser')
        # div = soup2.find('div', attrs={'class', 'MacPlayer'})
        # print(div.text)
