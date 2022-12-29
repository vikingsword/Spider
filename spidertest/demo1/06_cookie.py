import urllib.request
from http import cookiejar
from urllib.error import URLError

print('get cookie:')
cookie = cookiejar.CookieJar()
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cookie_handler)

response = opener.open('http://192.168.37.1/pikachu/vul/sqli/sqli_str.php')
for item in cookie:
    print(item.name + "=" + item.value)

print('persistence cookie as file with txt:')
filename = 'cookie.txt'
cookie = cookiejar.MozillaCookieJar(filename)
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cookie_handler)
response = opener.open('http://192.168.37.1/pikachu/vul/sqli/sqli_str.php')
cookie.save(ignore_discard=True, ignore_expires=True)

print('persistence cookie as file with lwp:')
filename = 'cookie2.txt'
cookie = cookiejar.LWPCookieJar(filename)
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cookie_handler)
opener.open('http://192.168.37.1/pikachu/vul/sqli/sqli_str.php')
cookie.save(ignore_expires=True, ignore_discard=True)

print('load cookie information from disk:')
cookie = cookiejar.LWPCookieJar()
cookie.load('cookie2.txt', ignore_discard=True, ignore_expires=True)
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cookie_handler)
response = opener.open('http://192.168.37.1/pikachu/vul/sqli/sqli_str.php')
html = response.read().decode('utf-8')
# print(html)

