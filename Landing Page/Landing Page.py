from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def root_route():
    return render_template("LP_index.html", phrase="Jason")

@app.route('/ninjas')
def ninja_route():
    return render_template("LP_ninjas.html")

@app.route('/dojos/new')
def dojo_route():
    return render_template("LP_dojos_new.html")

app.run(debug=True)