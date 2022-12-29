import requests
from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
    url = 'https://www.dmzj.com/view/yaoshenji/41917.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    r = requests.get(url=url, headers=headers)
    html = BeautifulSoup(r.text, 'html.parser')
    script_info = html.script
    pics = re.findall('\d{13,14}', str(script_info))
    chapterpic_hou = re.findall('\|\|(\d{5})', str(script_info))[0]
    chapterpic_qian = re.findall('\|jpg\|(\d{4})', str(script_info))[0]
    for pic in pics:
        url = 'https://images.dmzj.com/img/chapterpic/' + chapterpic_qian + '/' + chapterpic_hou + '/' + pic + '.jpg'
        print(url)
