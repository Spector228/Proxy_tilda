from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# URL сайта, с которого нужно скопировать блоки
TARGET_URL = 'https://zelenkevich-swimming.ru/'

def extract_all_blocks(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Найти все блоки
    all_blocks = soup.find_all('div')
    
    blocks = []
    for block in all_blocks:
        block_id = block.get('id', 'no-id')
        block_html = str(block)
        blocks.append({
            'id': block_id,
            'html': block_html
        })
    
    return blocks

@app.route('/')
def index():
    blocks = extract_all_blocks(TARGET_URL)
    return jsonify(blocks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

