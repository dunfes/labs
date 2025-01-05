from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "main page"

@app.route('/currency', methods=['GET'])
def get_currency():
    return "USD - 41.5"

if __name__ == '__main__':
    app.run(port=8000, debug=True)
