from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    url = 'https://zelenkevich-swimming.ru/'  # URL сайта для скрапинга
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Извлечение всех блоков
    blocks = []
    for element in soup.find_all(True):  # True находит все теги
        blocks.append({
            'tag': element.name,
            'attributes': dict(element.attrs),
            'content': element.decode_contents()
        })

    return jsonify(blocks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
