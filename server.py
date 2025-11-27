from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/save', methods=['POST'])
def save_data():
    try:
        data = request.get_json()
        text = data.get('data', '')
        
        with open('/data/data.txt', 'a', encoding='utf-8') as f:
            f.write(text + '\n')
        
        return jsonify({'message': 'Данные сохранены'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/load', methods=['GET'])
def load_data():
    try:
        if not os.path.exists('/data/data.txt'):
            return jsonify({'content': 'Файл пуст'})
        
        with open('/data/data.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        
        return jsonify({'content': content})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)