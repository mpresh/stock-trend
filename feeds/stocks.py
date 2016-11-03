import re
import csv
import requests
from bs4 import BeautifulSoup
from utils import remove_white_space, cleanup_int
from scraper import Scraper

YAHOO_SITE = "http://finance.yahoo.com/d/quotes.csv?s={}&f=sb2b3jk"
STOCKS = [("http://www.facebook.com", "FB"), ("http://www.twitter.com", "TWTR"),  ("http://www.hubspot.com", "HUBS"),
          ("http://www.google.com", "GOOGL"), ("http://www.tesla.com", "TSLA"), ("http://www.amazon.com", "AMZN"),
          ("http://www.apple.com", "AAPL"), ("http://www.amd.com", "AMD"), ("http://www.microsoft.com", "MSFT"),
          ("http://www.netflix.com", "NFLX"), ("http://www.ariad.com", "ARIA"), ("https://www.gogoair.com", "GOGO")]

class StockScraper(Scraper):

    def request_url(self, input):
        yahoo_url = YAHOO_SITE.format(input[1])
        return yahoo_url
 

    def get_key(self, input):
        return input[0]

    def make_request(self, request_item):
        result = []
        with requests.Session() as s:
            download = s.get(request_item)

            decoded_content = download.content.decode('utf-8')

            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            for row in my_list:
                result.append(row)

        return result
    
    def parse(self, input):
        input = input[0]
        print(input)
        data = {}
        data["price"] = input[4]
        return data

    
def main():
    s = StockScraper(STOCKS)
    s.run(display=True)
    print(s.results)
    
    
if __name__ == "__main__":
    main()
