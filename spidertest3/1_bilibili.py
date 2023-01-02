import time

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'cookie':'buvid_fp=ce1db6c232ac1c86ee48e4ec5a930cd1; _uuid=E85F345D-CD107-41091-B1053-C22FF5C7182714443infoc; fingerprint=ce1db6c232ac1c86ee48e4ec5a930cd1; buvid3=D6B9C985-5AA2-AC4A-32A1-2F47310471C915001infoc; b_nut=1672281716; buvid4=5FE0213C-BDC4-D25C-F97A-9524005C3DB415001-022122910-3zihZNIDlM8cxuYpBLFjPQ%3D%3D; DedeUserID=80080888; DedeUserID__ckMd5=899702257b7e582c; i-wanna-go-back=-1; b_ut=5; CURRENT_FNVAL=4048; rpdid=|()|RR)Rmk~0J\'uY~kk)umkJ; b_lsid=7BC2A45B_18566130C77; SESSDATA=dd07ec95%2C1688006808%2C2dcdc%2Ac2; bili_jct=fa3deb26b8fed5827f57a21863e9cc9b; sid=678bo7jr; bp_video_offset_80080888=745671481738920000; nostalgia_conf=-1; innersign=1; PVID=2'

}

for i in range(1, 100):
    url = 'https://www.bilibili.com/video/BV1qG4y1m7M3/?spm_id_from=333.337.search-card.all.click'
    res = requests.get(url=url, headers=headers)
    print(res.status_code)
    # print('send ' + str(i) + ' successful')
    time.sleep(0.1)
