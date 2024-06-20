from adapters.web_scraper import WebScraper

class ScrapeService:
  def __init__(self):
    self.web_scraper = WebScraper()

  def scrape(self):
    return self.web_scraper.scrape()
