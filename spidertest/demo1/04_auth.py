# import urllib.request
# from urllib.error import URLError
#
# username = 'admin'
# password = 'admin'
#
# url = 'https://ssr3.scrape.center/'
#
# p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
#
# auth_handler = urllib.request.HTTPBasicAuthHandler(p)
# opener = urllib.request.build_opener(auth_handler)
#
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)
from urllib.request import HTTPPasswordMgrWithDefaultRealm, build_opener, HTTPBasicAuthHandler
from urllib.error import URLError

username = 'admin'
password = 'admin'
url = 'http://test.com'
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)
try:
    res = opener.open(url)
    html = res.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
