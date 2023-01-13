# -*- coding:utf-8 -*-
# Author:thy


# 引入模块
import time

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import urllib.request, urllib.error
import queue
import threading

# 请求头
# USER_AGENTS = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 "
#     "Safari/537.36",
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; "
#     ".NET CLR 3.0.04506)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR "
#     "2.0.50727)",
# ]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

# 定义一个优先级队列存放顺序的章节链接
priQue = queue.PriorityQueue()
# 定义一个优先级队列存放爬取到的章节内容
contentPriQue = queue.PriorityQueue()
# 定义一个存放线程的列表
threadList = []
# 定义一个存放写入线程的列表
writeThreadList = []


# 随机获取请求头，避免因多次访问被拒绝
# def createHeader():
#     headers = dict()
#     headers["User-Agent"] = random.choice(USER_AGENTS)
#     headers["Referer"] = "https://www.biquge7.top/"
#     return headers
#     pass


# 解析网页结构获取数据
def getData(baseUrl):
    # 获取全部章节地址
    # domain parse
    target = urllib.parse.urlparse(baseUrl).netloc
    # scheme parse
    scheme = urllib.parse.urlparse(baseUrl).scheme

    soup = getSoup(baseUrl)

    bookName = soup.find('h1').text
    linkList = soup.find('div', attrs={'class', 'list'}).find_all('a')

    for i in linkList:
        url = scheme + '://' + target + i['href']
        order_number = str(i['href']).split('/')[2]
        title = str(i['title']).replace(' ', ' ')
        priQue.put((order_number, url, title))
        pass

    # 创建并开启新线程
    for k in tqdm(range(10)):
        thread = GetThread(k)
        thread.start()
    #     threadList.append(thread)
    #     pass
    # for t in threadList:
    #     t.join()
    #     pass

    # 获取完成后最后按顺序写入文件
    writeFileByOrder(bookName)
    pass


def getSoup(target):
    # headers = createHeader()
    req = requests.get(url=target, headers=headers)
    req.encoding = 'utf-8'
    html = req.text
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    return soup


# 将内容写入文件
def writeToFile(content, bookName):
    # with自带close效果
    t1 = time.time()
    fileName = str(bookName) + '.txt'
    with open(fileName, 'a', encoding='utf-8') as f:
        f.write(content)
    f.close()
    pass


# 创建一个线程类用于获取章节内容
class GetThread(threading.Thread):

    def __init__(self, threadId):
        threading.Thread.__init__(self)
        self.threadId = threadId
        pass

    # 设置线程任务
    def run(self):
        # 获取队列中的所有地址
        t1 = time.time()
        while not priQue.empty():
            urlData = priQue.get()
            # 获取当前章节的章节序号 priQue.put((order_number, url, title))
            index = int(urlData[0])
            detail_url = urlData[1]
            title = urlData[2]

            # 定义一个变量存放章节内容
            fileContent = ""
            # 获取页数
            # pageNum = getPageNum(firstUrl)

            soup2 = getSoup(detail_url)
            texts = soup2.find('div', attrs={'class', 'text'})
            try:
                # 我也不知道为什么用了多线程就出现莫名其妙的错误，可能是线程冲突吧，nnd
                # todo 这里出了莫名其妙的bug程序执行可能变慢
                texts_parse = texts.text.strip().replace('\xa0', '')
                # texts_parse = str(texts.text).strip().replace('\xa0', '')
                # print(texts_parse)
                content = texts_parse + '\n'
                content.encode('utf-8')

                fileContent += title + '\n' + content + '\n'

                # 将获取到的章节内容按照章节优先级放入队列中
                contentPriQue.put((index, fileContent))
            except Exception as e:
                pass
            pass
        pass
        t2 = time.time()
        print('读取用时' + str(t2 - t1))

    pass


# 按顺序将内容写入文件的方法
def writeFileByOrder(bookName):
    # 获取锁
    # lockObj.acquire()
    while not contentPriQue.empty():
        data = contentPriQue.get()
        # index = data[0]
        content = data[1]
        writeToFile(content, bookName)
        # print('第 ', index, ' 章获取完毕')
        pass
    # 释放锁
    # lockObj.release()
    pass


# 主函数
def main():
    # 爬取网页结构并解析数据
    getData(base_url)
    pass


if __name__ == '__main__':
    # url
    example_url = "https://www.biquge7.top/50043"
    base_url = input('please input target url(such as ' + example_url + ') :')
    while True:
        while True:
            if not base_url.__contains__('https://www.biquge7.top'):
                base_url = input('your url is not correct, please try again: ')
            else:
                break
        time_start = time.time()
        main()
        time_end = time.time()
        print('下载用时：' + str(time_end - time_start))
        break
    pass
