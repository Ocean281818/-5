import requests
from bs4 import BeautifulSoup


class Douban:
    def __init__(self):
        self.url = 'https://movie.douban.com/top250'
        self.startnum = []
        for start_num in range(0, 251, 25):
            self.startnum.append(start_num)
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}

    def get_top250(self):
        for start in self.startnum:
            start = str(start)
            html = requests.get(self.url, params={'start': start}, headers=self.header)
            soup = BeautifulSoup(html.text, "html.parser")
            names = soup.find_all('div', class_='hd')

            for index, name in enumerate(names):
                title = name.a.span.text
                print(f'{start} - {index + int(start) + 1}: 《{title}》')


if __name__ == "__main__":
    cls = Douban()
    cls.get_top250()