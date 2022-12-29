import urllib.request
from urllib.error import HTTPError, URLError

try:
    response = urllib.request.urlopen('https://vikingar.top/132')
except HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except URLError as e:
    print(e.reason, e.code, e.headers, sep='\n')
else:
    print('request successfully!')