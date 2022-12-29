# -*- coding:utf-8 -*-
'''
 使用 POST 方式抓取 有道翻译
    urllib2.Request(requestURL, data=data, headers=headerData)
    Request 方法中的 data 参数不为空，则默认是 POST 请求方式
    如果 data 为空则是 Get 请求方式
    {"errorCode":50}错误：
         有道翻译做了一个反爬虫机制，就是在参数中添加了 salt 和 sign 验证，具体操作说明参考：
         http://www.tendcode.com/article/youdao-spider/
'''

import requests
import time
import random
import hashlib
import sys

# 字符串转 utf-8 需要重新设置系统的编码格式
# reload(sys)
# sys.setdefaultencoding('utf8')

# 目标语言
targetLanguage = 'Auto'
# 源语言
sourceLanguage = 'Auto'

headerData = {
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-2022895048@10.168.8.76;',
    'Referer': 'fanyi.youdao.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

# 语言类型缩写
languageTypeSacronym = {
    '1': 'zh-CHS 》 en',
    '2': 'zh-CHS 》 ru',
    '3': 'en 》 zh-CHS',
    '4': 'ru 》 zh-CHS',
}

# 翻译类型
translateTypes = [
    '中文 》 英语',
    '中文 》 俄语',
    '英语 》 中文',
    '俄语 》 中文'
]


def startRequest(tanslateWd):
    requestURL = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    client = 'fanyideskweb'
    timeStamp = getTime()
    # key = 'ebSeFb%=XZ%T[KZ)c(sy!'
    key = 'ebSeFb%=XZ%T[KZ)c(sy!'

    sign = getSign(client, tanslateWd, timeStamp, key)

    data = {
        'i': tanslateWd,
        'from': sourceLanguage,
        'to': targetLanguage,
        'client': client,
        'doctype': 'json',
        'version': '2.1',
        'salt': timeStamp,
        'sign': sign,
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'true',
        'smartresult': 'dict'
    }

    # data = requests.urlencode(data)

    resonse = requests.post(requestURL, data=data, headers=headerData)

    print(resonse.text)


# 生成时间戳
def getTime():
    return str(int(time.time() * 1000) + random.randint(0, 10))


# 生成 Sign
def getSign(client, tanslateWd, time, key):
    s = client + tanslateWd + time + key
    m = hashlib.md5()
    m.update(s.encode('utf-8'))
    return m.hexdigest()


def getTranslateType(translateType):
    global sourceLanguage, targetLanguage
    try:
        if translateType:
            l = languageTypeSacronym[translateType].split(' 》 ')
            sourceLanguage = l[0]
            targetLanguage = l[1]
    except:
        print('翻译类型选择有误，程序将使用 Auto 模式为您翻译')


if __name__ == '__main__':
    print('翻译类型：')
    for i, data in enumerate(translateTypes):
        print('%d: %s' % (i + 1, data))

    translateType = input('请选择翻译类型：')
    getTranslateType(translateType)
    tanslateWd = input('请输入要翻译的消息：')
    startRequest(tanslateWd)
