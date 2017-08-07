from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def root_route():
    return render_template("WMN_index.html")

@app.route('/process',methods=['POST'])
def process():
    print request.form
    my_data = request.form['name']
    return redirect('/')

app.run(debug=True)