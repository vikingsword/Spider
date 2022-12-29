import requests as requests

url = "https://www.baidu.com/s?wd=%E9%97%AA%E5%85%89%E7%9A%84%E5%93%88%E8%90%A8%E7%BB%B4"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55"

}
resp = requests.get(url, headers=headers)
print(resp)
print(resp.text)
resp.close()
