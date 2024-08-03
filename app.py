import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    try:
        url = 'https://zelenkevich-swimming.ru/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        blocks = []
        for element in soup.find_all(True):
            blocks.append({
                'tag': element.name,
                'attributes': dict(element.attrs),
                'content': element.decode_contents()
            })

        return jsonify(blocks)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
