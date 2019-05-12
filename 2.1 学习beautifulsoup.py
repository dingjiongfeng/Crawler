from bs4 import BeautifulSoup as bs
import requests
url = "http://www.dxy.cn/bbs/thread/626626#626626"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
}
html = requests.get(url, header)
soup = bs(html.content, 'lxml') 
#html在这里是一个response对象，无法用BeautifulSoup解析，如果要解析，解析对象应该是html.content

for data in soup.find_all(name="tbody"):  
    #data为tag类型 find_all返回的时tag类型的列表
    #因为有的tag中不符合，所以要try
    try:
        userid = data.find('div',class_='auth').get_text(strip=True)
        print(userid)
        comment = data.find('td',class_='postbody').get_text(strip=True)
        print(comment)
    except:
        pass
