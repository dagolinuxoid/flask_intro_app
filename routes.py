from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
from functools import wraps
app = Flask(__name__)

# psst not only session but flash also reqieres setting up of a secret key
app.secret_key = os.urandom(24)
# there is no route to template.html
# template.html is using as a base

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

# how does it exactly work?
def login_required(isLogged):
    @wraps(isLogged)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return isLogged(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('log'))
    return wrap
   
# private page | for an individual user
@app.route('/hello')
@login_required
def hello():
    return render_template('hello.html')

@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        if request.form['name'] != 'admin' or request.form['password'] != 'admin':
            flash('Invalid credentials')
        else:
            session['logged_in'] = True
            return redirect(url_for('hello'))       
    return render_template('log.html')

@app.route('/logout')
@login_required
def logout():
    # session.pop('logged_in', None)
    session.clear()
    flash('You are logged out')
    return redirect(url_for('log'))
 
@app.errorhandler(404)
def page404(error):
    return render_template('page404.html'), 404

if __name__ == '__main__':
    # don't use it in production
    app.run(debug=True)