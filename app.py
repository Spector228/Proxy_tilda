from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    url = 'https://zelenkevich-swimming.ru/'  # URL сайта для скрапинга
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка успешности запроса
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Failed to fetch URL: {str(e)}'}), 500

    try:
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
    except Exception as e:
        return jsonify({'error': f'Error processing the HTML: {str(e)}'}), 500

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not Found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
