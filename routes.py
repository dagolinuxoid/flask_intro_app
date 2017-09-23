from flask import Flask, render_template
app = Flask(__name__)

# there is no route to template.html
# template.html is using as a base

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    # don't use it in production
    app.run(debug=True)