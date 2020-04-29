from flask import Flask, render_template
app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/blog/2020/dogs')
def dog():
    return 'This is my dog'
