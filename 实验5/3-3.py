import requests
from lxml import  etree
import  csv

def GetWeather(url):
    weather_info = []
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
    resp = requests.get(url,headers=headers)
    resp_html = etree.HTML(resp.text)
    resp_list = resp_html.xpath("//ul[@class='weaul']/li")

    for li in resp_list:
        day_weather_info = {}
        #日期
        day_weather_info['date_time'] = li.xpath("./a/div[1]/span[1]/text()")[0].split(' ')[0]
        #最高温
        high = li.xpath("./a/div[4]/span[1]/text()")[0]
        day_weather_info['high'] = high[:high.find("度")]
        #最低温
        low = li.xpath("./a/div[4]/span[2]/text()")[0]
        day_weather_info['low'] = low[:low.find("度")]
        #天气
        day_weather_info['weather'] = li.xpath('./a/div[3]/text()')[0]
        weather_info.append(day_weather_info)

    return  weather_info
with open(weather.csv )


