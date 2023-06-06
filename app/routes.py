from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html.jinja')

@app.route('/book/<book>')
def book(book):
    return render_template('book.html.jinja', book=book)

@app.route('/name/<name>')
@app.route('/name')
def name(name="World"):
    return f"Hello, {name}!"

@app.route('/about')
def about():
    return render_template('about.html')