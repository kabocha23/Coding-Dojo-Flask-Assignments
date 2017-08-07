from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def root_route():
    return render_template("DS_index.html")

@app.route('/results',methods=['POST'])
def results():
    print request.form
    nme = request.form['name']
    loc = request.form['location']
    lang = request.form['language']
    comm = request.form['comments']
    return render_template("DS_results.html",name = nme, location = loc, language = lang, comments = comm)

@app.route('/',methods=['POST'])
def return_route():
    return redirect("/")
app.run(debug=True)