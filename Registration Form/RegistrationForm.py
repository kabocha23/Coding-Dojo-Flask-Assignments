from flask import Flask, render_template, request, redirect, session, flash
import re
FIRSTLAST_REGEX = re.compile(r'^[a-zA-Z.+_-]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
UPPERDIGIT_REGEX = re.compile(r'^(?=.*[0-9])(?=.*[A-Z]).+$')
app = Flask(__name__)
app.secret_key = 'dnslakjnjnccacdlk'

@app.route('/')
def root_route():
    return render_template("RegistrationForm_index.html")

@app.route('/results',methods=['POST'])
def results():
    print request.form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    
    if len(first_name) < 1:
        flash("First Name cannot be empty")
    elif len(last_name) < 1:
        flash("Last Name cannot be empty")
    elif len(password) < 1:
        flash("Please enter a password")
    elif len(password) < 8:
        flash("Password must be longer than 8 characters")
    elif len(confirm_password) < 1:
        flash("Please confirm password")
    elif password != confirm_password:
        flash("Passwords must match")
    elif not FIRSTLAST_REGEX.match(first_name):
        flash("First Name can only contain letters")
    elif not FIRSTLAST_REGEX.match(last_name):
        flash("Last Name can only contain letters")
    elif not EMAIL_REGEX.match(email):
        flash("Invalid Email Address format")
    elif not UPPERDIGIT_REGEX.match(password):
        flash("Password must contain at least one upper case letter and one digit")
    else:
        return render_template("RegistrationForm_results.html",first_name = first_name, last_name = last_name, email = email, password = password, confirm_password = confirm_password)
    return redirect('/')

@app.route('/',methods=['POST'])
def return_route():
    return redirect("/")
app.run(debug=True)

# Create a simple registration page with the following fields:

# Here are the validations you must include:

# All fields are required and must not be blank
# First and Last Name cannot contain any numbers
# Password should be more than 8 characters
# Email should be a valid email
# Password and Password Confirmation should match
# When the form is submitted, make sure the user submits appropriate information. If the user did not submit appropriate information, return the error(s) above the form that asks the user to correct the information. 

# Message Flashing with Categories
# For this, you will need to use flash messages at the very least. You may have to take this one step further and add categories to the flash messages. You can learn that from the flask doc: flash messages with categories

# If the form with all the information is submitted properly, simply have it say a message "Thanks for submitting your information."

# Ninja Version:
# Add the validation that requires a password to have at least 1 uppercase letter and 1 numeric value.

# Hacker Version:
# Add a birth-date field that must be validated as a valid date and must be from the past.

