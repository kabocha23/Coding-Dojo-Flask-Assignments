from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def root_route():
    
    return render_template("DN_index.html")

@app.route('/ninja')
def AllNinjas():
    return render_template("DN_ninja.html")

@app.route('/ninja/<color>')
def ChooseNinja(color):
    if color == 'blue':
        nme = 'Leonardo'
        color = url_for('static', filename='images/leonardo.jpg')
        return render_template("DN_ninjas.html", color = color, name = nme)
    elif color == 'orange':
        nme = 'Michaelangelo'
        color = url_for('static', filename='images/michaelangelo.jpg')      
        return render_template("DN_ninjas.html", color = color, name = nme)
    elif color == 'purple':
        nme = 'Donatello'
        color = url_for('static', filename='images/donatello.jpg')    
        return render_template("DN_ninjas.html", color = color, name = nme)
    elif color == 'red':
        nme = 'Raphael'
        color = url_for('static', filename='images/raphael.jpg') 
        return render_template("DN_ninjas.html", color = color, name = nme)
    else:
        nme = 'April'
        color = url_for('static', filename='images/notapril.jpg')
        return render_template("DN_ninjas.html", color = color, name = nme)

app.run(debug=True)

# find a way to link each ninja turtle with one html file