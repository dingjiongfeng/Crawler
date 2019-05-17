from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
import time
import csv

def getItem():
    title_list = soup.find_all('a',class_='black')
    newest_writer_list = soup.find_all('td',class_='table-s')
    title_record = []
    newest_writer_record = []
    for title in title_list:
        title_record.append(title.string)
    for newest_writer in newest_writer_list:
        try:
            newest_writer_record.append(newest_writer.find('a').string) #一个疑问，因为其中有None，所以要仔细观察数据
        except:
            pass
    return title_record,newest_writer_record
    
def get_write(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
    }
    html = requests.get(url, headers = headers)
    soup = bs(html.content,'lxml',from_encoding='utf-8')#html后要加上content
    datas = []
    for data in soup.find_all('td',class_="news"):
        result = data.find('a').string
        datas.append(result)
    file = open('C:\\Users\\Apple\\Desktop\\爬虫\\info2','w+',encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow('帖子标题')
    for data in datas:
        writer.writerow(data)
        
url = 'http://www.dxy.cn/bbs/thread/626626#626626 '
browser = webdriver.Chrome()
browser.get(url)

time.sleep(1)
browser.maximize_window()

login = browser.find_element_by_class_name('activate-info-tip-btn')
login.click()
#按下登录按钮
time.sleep(1)

#login_ = browser.find_element_by_css_selector(".aside.mobile_hide")但不符合
#这里class中间有空格，需要用find_element_by_css_selector来找出。由于马上登陆嵌套在这中，所以还要提取出来。
login_ = browser.find_element_by_link_text("马上登录")
login_.click()
#按下马上登陆按钮
browser.find_element_by_link_text("返回电脑登录").click()
time.sleep(1)

username = browser.find_element_by_name('username')#找到邮箱账号输入框
username.send_keys('**')

password = browser.find_element_by_name('password')
password.send_keys('**')

login_em = browser.find_element_by_class_name('button')
login_em.click()
time.sleep(1)

title_record, newest_writer_record = getItem()
file = open('C:\\Users\\Apple\\Desktop\\爬虫\\info1','w+',encoding='utf-8')
writer = csv.writer(file)
writer.writerow(['板块','最新发帖人'])
#将这些信息写入csv文件
for name,title in zip(title_record, newest_writer_record):
    writer.writerow([name, title])
    
browser.get("http://www.dxy.cn/bbs/thread/626626#626626")
html = browser.page_source
soup = bs(html, 'lxml')
user_list=[]
content_list=[]

users = soup.find_all('div',class_='auth')
for user in users:
    user_item = user.find('a').string
    user_list.append(user_item)
user_list = user_list[0:-1] #删去最后一个（自己）
    
contents = soup.find_all('td', class_='postbody')
for content in contents:
    content_item = content.get_text(strip=True) 
    content_list.append(content_item)
    
for i in range(len(user_list)):
    result = user_list[i].strip()+":"+content_list[i].strip()#content_list中有None
    dir_file = open("records.txt",'a', encoding="utf-8")
    dir_file.write(result+"\n")#写入文件 I/O operation on closed file.
    dir_file.write('*' * 80+"\n")
    dir_file.close()
print('*' * 5 +"抓取结束"+'*' * 5)
