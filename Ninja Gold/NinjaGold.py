from flask import Flask, render_template, request, redirect, session
# from bs4 import BeautifulSoup
import random

# soup = BeautifulSoup(html_doc, 'html.parser')
app = Flask(__name__)
app.secret_key = 'Shhhhhhhhhh'

@app.route('/')
def NinjaGold():
    print session['gold_counter']
    session['message'] = ''
    return render_template('NG_index.html')

@app.route('/process_money',methods=['POST'])
def ProcessMoney():

    if request.form['building'] == 'Farm':
        sumGoldIncrease1()

    elif request.form['building'] == 'Cave':   
        sumGoldIncrease2()
        
    elif request.form['building'] == 'House':
        sumGoldIncrease3()

    elif request.form['building'] == 'Casino':
        sumGoldGainLose()
        
    return render_template('NG_index.html') 

def sumGoldIncrease1():
    result1 = int(random.randrange(10, 21))
    session['gold_counter'] += result1
    print session['gold_counter']
    print "farm"
    session['message'] = "Earned " + str(result1) + " gold from the farm!"
    return render_template('NG_index.html')

def sumGoldIncrease2():
    result2 = int(random.randrange(5, 11))
    session['gold_counter'] += result2
    print session['gold_counter']
    print "cave"
    session['message'] = "Earned " + str(result2) + " gold from the cave!"
    return render_template('NG_index.html')

def sumGoldIncrease3():
    result3 = int(random.randrange(2, 6))
    session['gold_counter'] += result3
    print session['gold_counter']
    print "house"
    session['message'] = "Earned " + str(result3) + " gold from the house!"
    return render_template('NG_index.html')

def sumGoldGainLose():
    result4 = int(random.uniform(-50, 51))
    session['gold_counter'] += result4
    print session['gold_counter']
    print "casino"
    if result4 > 0:
        session['message'] = "Entered a Casino and won " + str(result4) + " gold!"
    elif result4 < 0:
        if session['gold_counter'] > 0:
            session['message'] = "Entered a Casino and lost " + str(result4) + " gold..."
        if session['gold_counter'] < 0:
            session['message'] = "Good Job, you lost all of your money and now your'e a homeless ninja!"
    elif result4 == 0:
        session['message'] = "Entered a Casino and came out even"
    return render_template('NG_index.html')

@app.route('/play_again',methods=['POST']) 
def return_route():
    session['gold_counter'] = 0
    return redirect("/")

app.run(debug=True)
