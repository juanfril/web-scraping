from flask import Flask, jsonify, request
from core.scrape_service import ScrapeService

app = Flask(__name__)
scrape_service = ScrapeService()

@app.route('/scrape', methods=['GET'])
def scrape():
  data = scrape_service.scrape()
  return jsonify(data)
  
if __name__ == "__main__":
  app.run(debug=True)
