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
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        username = request.form['username']
        confirm_password = request.form['confirmPassword']

        if not all([email, password, name, username, confirm_password]):
            return "Please fill in all fields", 400

        if not email_regex.match(email):
            return "Invalid email format", 400

        if not password_regex.match(password):
            return "Invalid password format", 400

        if password != confirm_password:
            return "Passwords do not match", 400

        # Here, you would typically add code to save the new user to your database
        # For now, we'll simply redirect to the main page

        return redirect(url_for('main'))

    return render_template('login.html')
@app.route('/main')
def main():
    # Serve main.html
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
