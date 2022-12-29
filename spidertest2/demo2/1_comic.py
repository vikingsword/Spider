import os
import re
from contextlib import closing

import requests
from bs4 import BeautifulSoup


def getTitleAndLink():
    url = 'https://www.dmzj.com/info/baiguitan.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    req = requests.get(url=url, headers=headers)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    linkList = soup.find('div', class_='tab-content tab-content-selected zj_list_con autoHeight').find_all('a')
    linkList.reverse()
    print(linkList)
    return linkList

    # https://images.dmzj.com/img/chapterpic/27919/123175/15907199661672.jpg


if __name__ == '__main__':
    # target = 'https://www.dmzj.com/view/baiguitan/82426.html'

    link = getTitleAndLink()

    for i in link:
        target = i['href']
        chapter_save_dir = i['title']
        if chapter_save_dir not in os.listdir('./'):
            os.mkdir(chapter_save_dir)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "Referer": "https://www.dmzj.com/"
        }
        req = requests.get(url=target, headers=headers)
        html = BeautifulSoup(req.text, 'html.parser')
        script_info = html.script
        print(script_info)
        pics = re.findall('\d{13,14}', str(script_info))
        for idx, pic in enumerate(pics):
            if len(pic) == 13:
                pics[idx] = pic + '0'
        pics = sorted(pics, key=lambda x: int(x))
        chapterpic_qian = re.findall('(\d{5})', str(script_info))[0]
        chapterpic_hou = re.findall('(\d{6})', str(script_info))[0]
        for idx, pic in enumerate(pics):

            if pic[-1] == '0':
                url = 'https://images.dmzj.com/img/chapterpic/' + chapterpic_qian + '/' + chapterpic_hou + '/' + pic[
                                                                                                                 :-1] + '.jpg'
            else:
                url = 'https://images.dmzj.com/img/chapterpic/' + chapterpic_qian + '/' + chapterpic_hou + '/' + pic + '.jpg'

            with closing(requests.get(url, headers=headers, stream=True)) as response:
                chunk_size = 1024
                content_size = int(response.headers['content-length'])
                if response.status_code == 200:
                    print('file size:%0.2f KB' % (content_size / chunk_size))
                    pic_name = '%03d.jpg' % (idx + 1)
                    pic_save_path = os.path.join(chapter_save_dir, pic_name)
                    with open(pic_save_path, "wb") as file:
                        for data in response.iter_content(chunk_size=chunk_size):
                            file.write(data)
                else:
                    print('link error')
            print('download successful！')
