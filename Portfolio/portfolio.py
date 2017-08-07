from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def jasons_page():
    return render_template('portfolio.html')

@app.route('/projects')
def jason_projects():
    return render_template('port_projects.html')

@app.route('/about')
def about_jason():
    return render_template('port_about.html')

app.run(debug=True)