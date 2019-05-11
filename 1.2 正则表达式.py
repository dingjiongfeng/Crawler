def movie_info(url):
    header = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
    }
    
    r = requests.get(url,header)
    ranks = re.findall(r'<em class="">(.+?)</em>',r.text)
    names = re.findall(r'<span class="title">([\u4e00-\u9fa5]+)</span>',r.text)
    # [\u4e00-\u9fa5]+为匹配一个或多个中文
    years = re.findall(r'<br>(.+?)&nbsp;/&nbsp;',r.text,re.S)
    text = re.sub('导演: ',"",r.text)  # ：中文标点符号
    directors = re.findall('<p class="">(.*?)&nbsp;&nbsp;', text, re.S)
    
    for rank,name,year,director in zip(ranks,names,years,directors):
        writer.writerow([rank,name,year,director])
    import csv

import csv

if __name__ == '__main__':
    file = open('C:\\Users\\Apple\\Desktop\\爬虫\\movie_info.csv','w+',encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(['rank','name','year','director'])

    for i in range(0,250,25):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
        movie_info(url)
