from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)

@app.route('/parse', methods=['POST'])
def parse():
    data = request.get_json()
    url = data['url']
    
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=options)
    
    driver.get(url)
    time.sleep(5)  # Даем время загрузиться странице
    
    script = '''
    const blocks = document.querySelectorAll('.t-zoombox');
    const blocksHtml = [];
    
    blocks.forEach(block => {
        blocksHtml.push(block.outerHTML);
    });

    return blocksHtml.join('\\n\\n');
    '''
    html = driver.execute_script(f'return ({script})()')
    driver.quit()

    return jsonify({'num_blocks': len(html.split('\n\n')), 'html': html})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
