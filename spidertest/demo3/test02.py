import requests

searchContent = input("please input keyword: ")
url = f"https://www.baidu.com/s?wd={searchContent}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55"
}
resp = requests.get(url, headers=headers)
print(resp.text)
print('--------------------')
print(resp)
resp.close()
