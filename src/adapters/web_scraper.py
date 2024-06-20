import scrapy
from scrapy.crawler import CrawlerProcess

class PublicRegisterSpider(scrapy.Spider):
  name = 'public_register'
  start_urls = ['https://members.collegeofopticians.ca/Public-Register']
  
  def parse(self, response):
    for member in response.css('div.member'):
      yield {
        'name': member.css('h2::text').get(),
        'details': member.css('p::text').get()
      }

class WebScraper:
  def scrape(self):
    process = CrawlerProcess(settings={
            'FEED_FORMAT': 'json',
            'FEED_URI': 'output.json'
        })
    process.crawl(PublicRegisterSpider)
    process.start()
      
    with open('output.json') as json_file:
      data = json.load(json_file)

    return data
