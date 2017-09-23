from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# there is no route to template.html
# template.html is using as a base

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

# private page | for an individual user
@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        if request.form['name'] != 'admin' or request.form['password'] != 'admin':
            flash('Invalid credentials')
        else:
            return redirect(url_for('hello'))       
    return render_template('log.html')

if __name__ == '__main__':
    # don't use it in production
    app.run(debug=True)