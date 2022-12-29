import urllib.parse

param = {
    'id': 1,
    'name': 'vikingar'
}
base_url = 'https://www.baidu.com'
ext_url = urllib.parse.urlencode(param)
url = base_url + ext_url
print(ext_url)
print(url)

param2 = urllib.parse.parse_qs(ext_url)
print(param2)

param3 = urllib.parse.parse_qsl(ext_url)
print(param3)

# 将中文字符转化为url编码
keyword = '壁纸'
keyword_parse = urllib.parse.quote(keyword)
url = 'https://www.baidu.com/s?wd=' + keyword_parse
print(url)

# 中文字符url编码后还原
keyword_original = urllib.parse.unquote(keyword_parse)
print(keyword_original)
