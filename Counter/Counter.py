from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Shhhhhhhhhh'

@app.route('/')
def index():
    sumSessionCounter()
    sumSessionCounter()
    return render_template("counter_index.html")

@app.route('/add', methods=['POST']) 
def sumSessionCounter():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset',) 
def sumSessionResetter():
    session['counter'] = -2
    return redirect('/')

app.run(debug=True)