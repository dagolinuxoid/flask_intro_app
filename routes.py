from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps
from cs50 import SQL

app = Flask(__name__)
app.config.from_object('dev_conf')

db=SQL('sqlite:///{}'.format(app.config['DATABASE']))
# psst not only session but flash also reqieres setting up of a secret key


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
   
@app.route('/compose',methods=['GET', 'POST'])
@login_required
def compose():
    if request.method == 'POST':
        if request.form.get('title') != '' and request.form.get('post') != '':
            db.execute('insert into posts values (:title, :post)',
                    title=request.form.get('title'), post=request.form.get('post'))
            return redirect(url_for('diary'))
    return render_template('compose.html')

@app.route('/diary')
@login_required
def diary():
    posts=db.execute('select title, post from posts')
    return render_template('diary.html',posts=posts)

# private page | for an individual user
@app.route('/hello')
@login_required
def hello():
    return render_template('hello.html')

@app.route('/log', methods=['GET', 'POST'])
def log():
    if session.get('logged_in'):
        return redirect(url_for('home'))
    if request.method == 'POST':
        if request.form.get('name') != app.config['USER'] or request.form.get('password') != app.config['PASSWORD']:
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
    app.run()
