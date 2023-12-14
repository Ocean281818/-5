import requests
from bs4 import BeautifulSoup

class Weather:
    def __init__(self):
        self.url = 'https://www.tianqi.com/hangzhou/30'

    def get_data(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
        r = requests.get(url=self.url, headers=headers)
        if r.status_code == 200:
            r.encoding = 'UTF-8'
            return r.text
            soup = BeautifulSoup(r.content, 'text')
        else:
            print('请求失败')

if __name__=="__main__":
    wea=Weather()
    wea.get_data()
    print(wea)