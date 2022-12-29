import urllib.parse
from multiprocessing.pool import ThreadPool

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    target = 'https://www.agemys.net/detail/20220076'

    netloc = urllib.parse.urlparse(target).netloc
    scheme = urllib.parse.urlparse(target).scheme
    print(netloc + '\n' + scheme)

    req = requests.get(target)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    linkList = soup.find('div', attrs={'class': 'movurl', 'style': 'display:block'}).find_all('a')
    for i in linkList:
        # https://www.agemys.net/play/20220076?playid=2_13
        url = scheme + '://' + netloc + i['href']
        req2 = requests.get(url=url, headers=headers)
        html2 = req2.text
        soup = BeautifulSoup(html2, 'html.parser')
        div = soup.find('ifram',id='age_playfram')
        print(div)
        # print(url)
        # print(i['title'])

    # 开8个线程池
    # pool = ThreadPool(8)
    # results = pool.map(downVideo, serach_res.keys())
    # pool.close()
    # pool.join()
