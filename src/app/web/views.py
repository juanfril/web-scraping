from flask import Blueprint, jsonify
from app.services.scraper_service import ScraperService

main = Blueprint('main', __name__)
scraper_service = ScraperService()

@main.route('/scrape', methods=['GET'])
def scrape():
    scraper_service.run_spider()
    return jsonify({'message': 'Scraping started'})

@main.route('/data', methods=['GET'])
def get_data():
    data = scraper_service.get_scraped_data()
    if data:
        return jsonify(data)
    else:
        return jsonify({'error': 'No data found'}), 404
