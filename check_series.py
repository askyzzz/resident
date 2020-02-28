import requests
from bs4 import BeautifulSoup
import lxml

url = 'http://theresident.ru/'
headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

class RequestUrl():

    def __init__(self, url):
        self.url = url

    def getUrl(self):
        session = requests.Session()
        contents = session.get(url=self.url).content
        soup = BeautifulSoup(contents, 'html.parser')
        return soup

    def check(self):
        soup = self.getUrl()
        season = soup.find_all("td", {"align": "center"})
        print(season)

if __name__=='__main__':
    pars = RequestUrl(url)
    pars.check()
