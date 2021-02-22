import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__ (self,site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                f = open(r"/home/blackkasper/parser_data.txt",'a')
                f.write(url)
                f.write("\n")

                print("\n" + url)
        f.close()

news = "https://ria.ru/"
Scraper(news).scrape()
