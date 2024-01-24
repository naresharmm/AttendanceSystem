from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

# Regular expressions for validation
email_regex = re.compile(r'^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$')
password_regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")

@app.route('/')
def welcome():
    # Serve welcome.html at the root
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Extract form data
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        username = request.form['username']
        confirm_password = request.form['confirmPassword']

        # Perform validations
        if not all([email, password, name, username, confirm_password]):
            return "All form fields must be filled out.", 400
        if not email_regex.match(email):
            return "Invalid email format. Please try again.", 400
        if not password_regex.match(password):
            return "Invalid password format. Please try again.", 400
        if password != confirm_password:
            return "Passwords do not match. Please try again.", 400

        # Redirect to main page if validations pass
        return redirect(url_for('main'))

    # Serve login.html for GET request
    return render_template('login.html')

@app.route('/main')
def main():
    # Serve main.html
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
