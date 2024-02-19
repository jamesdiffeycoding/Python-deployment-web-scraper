from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/portfolio')
def portfolio():
    return "This is the portfolio page"
