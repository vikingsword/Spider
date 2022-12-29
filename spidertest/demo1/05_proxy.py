import time
import urllib.request
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler(
    {
        'http': 'http://127.0.0.1:8080',
        'https': 'https://127.0.0.1:8080'
    }
)
# build_opener 中可以传入一个元组, 如下:
username = 'admin'
password = 'admin'
url = 'http://test.com'
p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, username, password)
auth_handler = urllib.request.HTTPBasicAuthHandler(p)
hander = (proxy_handler, auth_handler)
# 然后将 hander 传入 build_opener中生成opener
opener = build_opener(proxy_handler)
try:
    res = opener.open(url)
    html = res.read().decode('utf-8')
    print(html)
    # 如果是文件的话或许可以做一个文件输出
    imag = res.read()
    # 修改保存的文件名
    f = open('imag.jpg','w')
except URLError as e:
    print(e.reason)
