import requests
from lxml import etree

class get_url:
    def __init__(self):
      self.url = "http://www.dxy.cn/bbs/thread/626626#626626"
      self.header = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
      }
 
    def get_info(self):
      response = requests.get(self.url, self.header)
      html = response.text
      tree = etree.HTML(html)
      users = tree.xpath('//div[@class="auth"]/a/text()')
      comments = tree.xpath('//td[@class="postbody"]')
      for i in range(len(users)):
        print(users[i].strip()+":"+comments[i].xpath('string(.)').strip())#提取多个字符串
        print("*"*80)
    
if __name__ == '__main__':
    get_URL = get_url()
    get_URL.get_info()
