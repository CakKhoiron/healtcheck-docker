from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
    return '<html><head><title>Payment Warehouse</title><meta charset="utf-8" /></head><body><h1>UP</h1></body></html>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
