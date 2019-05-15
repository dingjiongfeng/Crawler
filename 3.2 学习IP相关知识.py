import requests
from bs4 import BeautifulSoup
import time
import re
import json

def open_proxy_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
    }
    try:
        r=requests.get(url, headers=headers, timeout=20)#timeout为防止服务器响应缓慢，导致客服端处理异常
        r.raise_for_status()
        #如果发送了一个错误请求(一个 4XX 客户端错误，或者 5XX 服务器错误响应)，我们可以通过Response.raise_for_status() 来抛出异常。
        r.encoding = r.apparent_encoding #apparent_encoding 为'utf-8'
        return r.text
    except:
        print('无法打开网页'+url)
        
def get_proxy_ip(response):
    proxy_id_list = []
    soup = BeautifulSoup(response, 'html.parser')
    proxy_ips = soup.find('table', id = 'ip_list').find_all('tr')
    for proxy_ip in proxy_ips:
        if len(proxy_ip.select('td')) >=8: #取出列表
            ip = proxy_ip.select('td')[1].text
            port = proxy_ip.select('td')[2].text
            protocol = proxy_ip.select('td')[5].text
            if protocol in ('HTTP','HTTPS','http','https'):
                proxy_id_list.append(f'{protocol}://{ip}:{port}')
    return proxy_id_list
    
def check_proxy_avaliability(proxy):
    url = 'http://www.baidu.com'
    result = open_url_using_proxy(url, proxy)
    VALID_PROXY = False
    if result:
        text, status_code = result
        if status_code == 200:
            r_title = re.findall('<title>.*</title>', text)
            if r_title:
                if r_title[0] == '<title>百度一下，你就知道</title>':
                    VALID_PROXY = True
        if VALID_PROXY:
            check_ip_url = 'https://jsonip.com/'
            try:
                text, status_code = open_url_using_proxy(check_ip_url, proxy)
            except:
                return

            print('有效代理IP: ' + proxy)
            with open('valid_proxy_ip.txt','a') as f:
                f.writelines(proxy)
            try:
                source_ip = json.loads(text).get('ip')
                print(f'源IP地址为：{source_ip}')
                print('='*40)
            except:
                print('返回的非json,无法解析')
                print(text)
    else:
        print('无效代理IP: ' + proxy)
        
def open_url_using_proxy(url, proxy):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    headers = {'User-Agent': user_agent}
    proxies = {}
    if proxy.startswith(('HTTPS','https')):
        proxies['https'] = proxy
    else:
        proxies['http'] = proxy

    try:
        r = requests.get(url, headers = headers, proxies = proxies, timeout = 10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return (r.text, r.status_code)
    except:
        print('无法访问网页' + url)
        return False
        
if __name__ == '__main__':
    proxy_url = 'https://www.xicidaili.com/'
    proxy_ip_filename = 'proxy_ip.txt'
    text = open_proxy_url(proxy_url)
    with open(proxy_ip_filename, 'w') as f:
        f.write(text)
    text = open(proxy_ip_filename, 'r').read()
    proxy_ip_list = get_proxy_ip(text)
    proxy_ip_list.insert(0, 'http://172.16.160.1:3128') #我自己的代理服务器
    for proxy in proxy_ip_list:
        check_proxy_avaliability(proxy)
