from flask import Flask, render_template, session, request, redirect,
import random
app = Flask(__name__)
app.secret_key = "ry_mu "

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def guess():
    if 'num' not in session:
       session['num'] = random.randint(0,101)
       print "the number is", session['num']

     guess = request.form['guessbox']

    if int(guess) > int(session)['num']:
        print guess, "is too high"
    if int(guess) < int(session['num']):
        print guess, "is too small"
    return redirect('/')
app.run(debug=True)
