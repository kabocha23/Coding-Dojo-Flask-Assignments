from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'Shhhhhhhhhh'

@app.route('/')
def takeAGuess():
    session['random'] = (random.randrange(0, 101))
    print session['random']
    return render_template('GNG_index.html')

@app.route('/guess',methods=['POST'])
def guessed():
    guess = int(request.form['enter_guess'])
    print request.form
    num = session['random']

    if guess == None or guess < 0:
        text = 'Nice Try...'

    elif num < guess:
        print guess,' is higher than ',num
        text = 'Too High...'

    elif num > guess:
        print guess,' is lower than ',num
        text = 'Too Low...'

    elif num == guess:
        print 'win'
        text = 'YOU GOT IT!!'
        
    return render_template('GNG_index.html', text = text) 

@app.route('/play_again',methods=['POST']) 
def return_route():
    return redirect("/")

app.run(debug=True)
