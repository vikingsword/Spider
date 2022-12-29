import urllib
from urllib import parse, request

# url1 = "https://httpbin.org/post"
# headers = {
#     'User-Agent': 'Mozilla/5.0'
# }
#
# data = bytes(urllib.parse.urlencode({'name': 'germey'}), encoding='utf-8')
#
# request = urllib.request.Request(url1, data, headers)
# response = urllib.request.urlopen(request)
# print(response.getcode())


url2 = "https://httpbin.org/post"
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {'name': 'germey'}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url2, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
