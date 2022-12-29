import requests

query = input("please input your text: ")
url = f"https://fanyi.baidu.com/sug"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
data = {
    "kw": query
}
resp = requests.post(url, data=data)

print(resp.json())
resp.close()

