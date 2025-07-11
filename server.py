from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, template_folder='../client/html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({'echo': data})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
