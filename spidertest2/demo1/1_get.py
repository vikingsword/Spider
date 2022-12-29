# import requests
#
# if __name__ == '__main__':
#     target = "http://fanyi.baidu.com/"
#     req = requests.get(url = target)
#     req.encoding = 'utf-8'
#     print(req.text)
#     print("123")


# -*- coding:UTF-8 -*-
import requests

if __name__ == '__main__':
    target = "https://fanyi.baidu.com/"
    target2 = "https://www.zhihu.com/"
    target3 = "http://www.coralbasic.com/archives/999"
    req = requests.get(url=target3)
    req.encoding = 'utf-8'
    print(req.text)
