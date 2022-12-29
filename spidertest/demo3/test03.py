import requests

query = input('please input your raw text: ')
url = f"https://fanyi.baidu.com/#en/zh/{query}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55"

}
resp = requests.get(url, headers=headers)
print(resp.text)
# print(resp.content)
print('----------------')
# print(resp.headers)
resp.close()


