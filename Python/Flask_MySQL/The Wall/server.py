from flask import Flask, render_template, redirect, request, flash
import re
from MySQLConnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "bootsandpants"
mysql = MySQLConnector
@app.route('/')
def index():
    return render_template('index_html')

@app.route('/process', methods=['POST'])
def process():
    emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if email_regex.match(request.form['email']):
        print "this is a valid email!"
        query = "INSERT INTO emails (email, created_at,updated_at) VALUES (:email, NOW(), NOW();"
        data = {"email":request.form['email']}
        mynewid = mysql.query_db(query,data)
        print "I just inserted this!", mynewid
        flash("this is a valid email! Your email {} is valid!".format(request.form['email']))
        return redirect('/success')
    else:
        print "this is not a valid email"
        flash("This is not a valid email!")
    return redirect('/')

@app.route('/success')
def success():
    query = "SELECT * FROM emails"
    listofemails = mysql.query_db(query)
    return render_template('success.html', emails = listofemails)


app.run(debug=True)
