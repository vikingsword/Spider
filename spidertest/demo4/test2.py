import json

import requests
# 删除o可以访问
url1 = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
url2 = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

form = {'i': '共产主义', 'from': 'zh-CHS', 'to': 'en', 'smartresult': 'dict', 'client': 'fanyideskweb',
             'salt': '15477056211258', 'sign': 'b3589f32c38bc9e3876a570b8a992604', 'ts': '1547705621125',
             'bv': 'b33a2f3f9d09bde064c9275bcb33d94e', 'doctype': 'json', 'version': '2.1', 'keyfrom': 'fanyi.web',
             'action': 'FY_BY_REALTIME', 'typoResult': 'false'}
headers = {
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-1384747936@10.108.162.138; OUTFOX_SEARCH_USER_ID_NCOO=461528666.40137166; ___rl__test__cookies=1662207185563',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}
resp = requests.post(url1, data=form, headers=headers)
print(resp.text)
res = json.loads(resp.text)
print(res)
