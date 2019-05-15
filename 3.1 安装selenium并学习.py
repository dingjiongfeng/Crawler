import time
from selenium import webdriver

browser = webdriver.Chrome()
url = "https://mail.126.com/"
browser.get(url)
time.sleep(3)

browser.maximize_window()

time.sleep(5)
browser.switch_to.frame(0) # 找到邮箱账号登录框对应的iframe
email = browser.find_element_by_name('email')#找到邮箱账号输入框

email.send_keys('dingjiongfeng')
password = browser.find_element_by_name('password')
password.send_keys('***')

login_em = browser.find_element_by_id('dologin')
login_em.click()

time.sleep(5)
