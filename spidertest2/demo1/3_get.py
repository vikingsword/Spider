import requests

if __name__ == '__main__':
    # you must close your system proxy first
    target = "https://www.biquge7.top/50043/2"
    # add headers then you can spider https
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "referer": "https://www.biquge7.top/50043"
    }
    req = requests.get(url=target, headers=headers)
    req.encoding = 'utf-8'
    print(req.text)
