import csv
import sys
import re
import scrapy
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from urllib.parse import urljoin

class DzivokliSpider(scrapy.Spider):
    name = "dzivokli"

    def start_requests(self):
        URL = 'https://www.ss.lv/lv/real-estate/flats/riga/all/hand_over/'
        yield scrapy.Request(url=URL, callback=self.response_parser)

    def response_parser(self, response):

        region = sys.argv[1]
        maxRent = int(sys.argv[2])
        minRoomCount = int(sys.argv[3])
        orderCol = sys.argv[4]
        for selector in response.css('tr[id^="tr_"]'):
            relative_link = selector.css('a::attr(href)').extract_first()
            absolute_link = urljoin(response.url, relative_link)
            info=selector.css('td.msga2-o.pp6::text, td.msga2-o.pp6 b::text').getall()
            rent_r=info[6]
            match = re.search(r'\b\d+\b', rent_r)
            if match:
                rent = int(match.group())
            else:
                print("No integer value found.")
            if info[0]==region and rent<=maxRent and int(info[2])>=minRoomCount:
                if len(info)<5:
                    continue

                yield {
       
                        'adrese': info[1],
                        'istabu skaits':info[2],
                        'platība m2':info[3],
                        'cena':info[6],
                        'hipersaite': absolute_link
                    }
            next_page = response.css('a.navi[rel="next"]::attr(href)').extract_first()
            if next_page:
                yield response.follow(next_page, callback=self.response_parser)

def dzivokli_spider_result():
    dzivokli_results = []

    def crawler_results(item):
        dzivokli_results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)
    crawler_process = CrawlerProcess()
    crawler_process.crawl(DzivokliSpider)
    crawler_process.start()
    return dzivokli_results

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python project/scrapy_project/spiders/dzivokli.py <region> <max-rent> <min-room-count> <order-col>")
    else:

        dzivokli_data=dzivokli_spider_result()
    if len(dzivokli_data)==0:
        print("nav ierakstu")
    else:
        keys = dzivokli_data[0].keys()
        with open('dzivokli_data.csv', 'w', newline='') as output_file_name:
            writer = csv.DictWriter(output_file_name, keys)
            writer.writeheader()
            writer.writerows(dzivokli_data)