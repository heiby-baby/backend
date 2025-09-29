from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/save', methods=['POST'])
def save_data():
    try:
        data = request.get_json()
        text = data.get('data', '')
        
        with open('data.txt', 'a', encoding='utf-8') as f:
            f.write(text + '\n')
        
        return jsonify({'message': 'Данные сохранены'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)