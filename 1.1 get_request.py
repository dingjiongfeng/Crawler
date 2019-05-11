import requests
url = 'https://www.baidu.com'
header = {'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN',
'Connection': 'keep-alive' }
header1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
#header和header1等价，所以user-agent 以字典键对形式作为headers的内容，就可以反爬成功，就不需要其他键对
r = requests.get(url, header1)
print(r.headers)
print()
print(r.request.headers)
