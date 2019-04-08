from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/signup", methods=['POST'])
def user_signup():
    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form["email"]
    
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''
    has_error = False

    if not username:
        username_error = "Please enter the valid name"
        has_error = True
    elif ' ' in username:
        username_error = 'username should not contain whitespace'
        has_error = True
    elif len(username) < 3 or len(username) > 20:
            username_error = "Username should be between 3 to 20 charaters"
            has_error = True

    if not password: 
        password_error = "Please enter the password"
        has_error = True
    elif ' ' in password:
        password_error = "Invalid password"
        has_error = True
    elif len(password) < 3 or len(password) > 20:
            password_error = "Password should be between 3 to 20 characters"
            has_error = True

    if not verify_password:
        verify_password_error = "Please enter to verify password"
        has_error = True
    else:
        if verify_password != password :
            verify_password_error = "Passwords don't match"
            has_error = True

    if email:
        if ' ' in email or '@' not in email or '.' not in email:
            email_error = "Email is invalid"
            has_error = True
        elif len(email) < 3 or len(email) > 20:
            email_error = "Email should be between 3 to 20 characters"
            has_error = True


    
    if has_error:
        return render_template('index.html', 
            username_error=username_error,
            password_error=password_error,
            verify_password_error=verify_password_error,
            email_error = email_error,
            username = username,
            email = email
            )
    else:
        return render_template('welcome.html', name=username)


app.run()