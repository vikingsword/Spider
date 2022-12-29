import socket
import urllib.request

url1 = "https://www.baidu.com"
url2 = "https://vikingar.top"
# response = urllib.request.urlopen(url2)
# print(response.read().decode('utf-8'))
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))


print('------------------------')
# urllib.request.parse_keqv_list({'name', 'zs'}, encodings='utf-8')
url3 = 'https://httpbin.org/post'
data = bytes(urllib.parse.urlencode({'name': 'germey'}), encoding='utf-8')
response = None
try:
    response = urllib.request.urlopen(url3, data, timeout=1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('Time out')
# print(response.read().decode('utf-8'))
