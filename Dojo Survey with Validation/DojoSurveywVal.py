from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key = 'dnslakjnjnccacdlk'

@app.route('/')
def root_route():
    return render_template("DojoSurveywVal_index.html")

@app.route('/results',methods=['POST'])
def results():
    print request.form
    nme = request.form['name']
    loc = request.form['location']
    lang = request.form['language']
    comm = request.form['comments']
    
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
    elif len(request.form['comments']) < 1:
            flash("Comments cannot be empty!")
    elif len(request.form['comments']) > 120:
        flash("Comments cannot be longer than 120 characters!")
    else:
        return render_template("DojoSurveywVal_results.html",name = nme, location = loc, language = lang, comments = comm)
    return redirect('/')

@app.route('/',methods=['POST'])
def return_route():
    return redirect("/")
app.run(debug=True)

# Add validations to check that the name and comment fields are not blank (display appropriate validation errors)
# Add validations to check that the comment is no more than 120 characters (display appropriate validation errors)