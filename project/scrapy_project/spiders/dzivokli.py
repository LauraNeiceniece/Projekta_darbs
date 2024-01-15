import scrapy

class DzivokliSpider(scrapy.Spider):
    name = "dzivokli"
    allowed_domains = ["www.ss.lv"]
    start_urls = ["https://www.ss.lv/lv/real-estate/flats/riga/all/hand_over/"]

    def parse(self, response):
        pass
