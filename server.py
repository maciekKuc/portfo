from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

def write_to_database(data):
     with open('database.csv', newline='', mode='a') as base:
         email = data['email']
         subject = data['subject']
         message = data['message']
         csv_file = csv.writer(base, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
         csv_file.writerow([email, subject, message])

@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_database(data)
            return render_template('./thankyou.html', user=data['email'])
        except:
            return 'something went wrong'
    else:
        return 'errior'

