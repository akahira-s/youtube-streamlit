import scrapy


class FreelanceLevtechSpider(scrapy.Spider):
    name = 'freelance-levtech'
    allowed_domains = ['freelance.levtch.jp']
    start_urls = ['http://freelance.levtch.jp/']

    def parse(self, response):
        pass
