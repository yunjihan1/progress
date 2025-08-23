from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detail')
def detail():
    return render_template('detail.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)