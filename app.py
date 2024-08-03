from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_zero_blocks(url):
    response = requests.get(url)
    if response.status_code != 200:
        return []
    soup = BeautifulSoup(response.text, 'html.parser')
    zero_blocks = soup.find_all(class_='zero-block-class')
    return [block.prettify() for block in zero_blocks]

@app.route('/scrape')
def scrape():
    url = 'https://zelenkevich-swimming.ru/'
    blocks_data = get_zero_blocks(url)
    return jsonify(blocks_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
