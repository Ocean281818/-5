import requests
from lxml import etree
from bs4 import BeautifulSoup

def get_data(url):
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"}
    resp = requests.get(url=url, headers=headers)
    if resp.status_code == 200:
        if resp.status_code == 200:
            # 设置编码格式
            resp.encoding = 'UTF-8'
            # 通过text方法返回网页源码
            return resp.text
        else:
            return '请求失败'



URL = 'http://www.weather.com.cn/weather/101210101.shtml'

html_code = get_data(URL)
soup = BeautifulSoup(html_code, "html.parser")
div = soup.find("div", attrs={'id': '7d'})
ul = div.find("ul")
lis = ul.find_all("li")

li_today = lis[0]
weather_list = []
weather = []

date_today = li_today.find('h1').text
wea_today = li_today.find('p',class_="wea").text
tem_h_today = 'NONE'
tem_l_today = li_today.find('p',class_="tem").find("i").text
spans_today = li_today.find('p',attrs={"class":"win"}).find_all("span")
win1_today = ''

for s in spans_today:
    win1_today += s.get('title') + '且'
win2_today = li_today.find('p',attrs={"class":"win"}).find("i").text

weather_today = [date_today,wea_today,tem_h_today,tem_l_today,win1_today + win2_today]

weather_all = []

for li in lis[1:]:
    date = li.find('h1').text
    wea = li.find('p', class_="wea").text
    tem_h = li.find('p', class_="tem").find("span").text
    tem_l = li.find('p', class_="tem").find("i").text
    spans = li.find('p', attrs={"class":"win"}).find("span")
    win1 = spans.get('title') + '且'
    win2 = li.find('p', attrs={"class":"win"}).find("i").text
    weather = [date,wea,tem_h,tem_l,win1 + win2]

    weather_all.append(weather)

weather_all.insert(0,weather_today)

for i in weather_all:
    print(i)