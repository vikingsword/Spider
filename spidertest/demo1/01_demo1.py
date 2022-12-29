import urllib.request

print("first way: ")
url1 = "https://w.wallhaven.cc/full/l3/wallhaven-l3xk6q.jpg"
url2 = "https://www.baidu.com"
response1 = urllib.request.urlopen(url2)
print(response1.getcode())
print(response1)

print("second way: ")
headers = {
    'User-Agent': 'Mozilla/5.0'
}
urllib.request.build_opener(headers)
request = urllib.request.urlopen(url2)
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))
