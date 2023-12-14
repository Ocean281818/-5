# coding:utf-8
import requests
from bs4 import BeautifulSoup

def get_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }

    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        # 设置编码格式
        r.encoding = 'UTF-8'
        # 通过text方法返回网页源码
        return r.text
    else:
        return '请求失败'

URL = 'http://www.weather.com.cn/weather/101270101.shtml'
# 调用函数获取网页源代码
html_code = get_data(URL)
soup = BeautifulSoup(html_code, "html.parser")

div = soup.find("div", id="7d")
# 获取div标签，下面这种方式也可以
# div = soup.find('div', attrs={'id': '7d', 'class': 'c7d'})  # div
ul = div.find("ul")  # ul
lis = ul.find_all("li")  # li

# 此行为该网站更新信息时间
# print(soup.find("div", id='around').find("h1").find("i").text)
li_today = lis[0]
# 发现在晚上访问该网站，今日的天气是没有最高气温，需要手动添加，无法遍历添加
weather_list = []
weather = []
# 添加今天的数据
date_today = li_today.find('h1').text  # 日期
wea_today = li_today.find('p', class_="wea").text  # 天气
tem_h_today = 'NONE'
tem_l_today = li_today.find('p', class_="tem").find("i").text  # 温度最低
spans_today = li_today.find('p', attrs={"class": "win"}).find_all("span")
win1_today = ''  # 风向
for s in spans_today:
    win1_today += s.get('title') + '且'
win2_today = li_today.find('p', attrs={"class": "win"}).find("i").text  # 风力

weather_today = [date_today, wea_today, tem_h_today, tem_l_today, win1_today + win2_today]

weather_all = []
# 添加剩下6天的数据
for li in lis[1:]:
    date = li.find('h1').text  # 日期
    wea = li.find('p', class_="wea").text  # 天气
    tem_h = li.find('p', class_="tem").find("span").text  # 温度最高
    tem_l = li.find('p', class_="tem").find("i").text  # 温度最低
    spans = li.find('p', attrs={"class": "win"}).find("span")  # 此处不需要find_all
    win1 = spans.get('title') + '且'  # 风向
    win2 = li.find('p', attrs={"class": "win"}).find("i").text  # 风力
    weather = [date, wea, tem_h, tem_l, win1 + win2]

    weather_all.append(weather)

# 插入首天数据
weather_all.insert(0, weather_today)
print(weather_all)
