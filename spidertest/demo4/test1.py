import requests

url1 = "http://www.ct.cn/"
url2 = 'http://www.cntour.cn/'
url3 = 'https://www.taobao.com/robots.txt'

# 模拟用户请求页面
headers = {
    'Cookie': '__51cke__=; _cliid=l8AA5fCAeXygHh_o; _siteStatId=9f562aee-1602-4512-9bc3-2376d4290afc; _siteStatDay=20220903; _siteStatRedirectUv=redirectUv_18895330; _siteStatVisitorType=visitorType_18895330; _siteStatVisit=visit_18895330; Hm_lvt_06350c6ad4283096ae81ad0aca67c0b7=1662201283; Hm_lvt_8041e149edeb80e896d05220f1c65443=1662201283; _checkSiteLvBrowser=true; _siteStatReVisit=reVisit_18895330; __tins__17240319=%7B%22sid%22%3A%201662201279240%2C%20%22vd%22%3A%205%2C%20%22expires%22%3A%201662204094105%7D; __51laig__=5; _siteStatVisitTime=1662202294586; Hm_lpvt_06350c6ad4283096ae81ad0aca67c0b7=1662202296; Hm_lpvt_8041e149edeb80e896d05220f1c65443=1662202296',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
resp = requests.get(url1, headers=headers)
resp.encoding = 'utf'
print(resp.text)
