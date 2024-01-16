import csv
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
        for selector in response.css('tr[id^="tr_"]'):
            relative_link = selector.css('a::attr(href)').extract_first()
            absolute_link = urljoin(response.url, relative_link)

            yield {
                  
                'address': selector.css('td.msga2-o.pp6::text, td.msga2-o.pp6 b::text').getall(),
                'hipersaite': absolute_link
                #'rooms': selector.css('td.msga2-o.pp6::text').getall(),
                #'hipersaite': selector.css('a::attr(href)').extract_first()
            }
        #next_page = response.css('a.navi[rel="next"]::attr(href)').extract_first()
        #if next_page:
           #yield response.follow(next_page, callback=self.response_parser)

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
    dzivokli_data=dzivokli_spider_result()

    keys = dzivokli_data[0].keys()
    with open('dzivokli_data.csv', 'w', newline='') as output_file_name:
        writer = csv.DictWriter(output_file_name, keys)
        writer.writeheader()
        writer.writerows(dzivokli_data)