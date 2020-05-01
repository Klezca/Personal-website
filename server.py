from flask import Flask, render_template, request, redirect
import csv
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name=None):
    return render_template(page_name)


@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e

    # now you're handling non-HTTP exceptions only
    return render_template("error.html", e=e), 500


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline="") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = csv.writer(database2, delimiter=',', lineterminator='\n',
                          quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow([email, subject, message])


@app.route('/submit-form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong'
