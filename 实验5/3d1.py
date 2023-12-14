import requests
from lxml import  etree

url = 'https://www.tianqi.com/hangzhou/'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}

response = requests.get(url,headers=headers)

html = etree.HTML(response.text)
weather_list = html.xpath('//dl[@class="weather_info"]//text()')
weather_text =''.join(weather_list)
print(weather_text)


