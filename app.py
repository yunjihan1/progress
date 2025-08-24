from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:10101010@localhost:3306/progress'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '%r 번 고객님의 이름은 %r 이고 %r 이메일을 가집니다' % (self.id, self.username, self.email)

class product(db.Model):
    __tablename__ = 'product'

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    product_sum = db.Column(db.Integer, nullable=False)
    product_discountrate = db.Column(db.Integer, server_default='0')
    product_like = db.Column(db.Integer, server_default='0')
    product_path = db.Column(db.String(255), nullable=False)


with app.app_context():
    db.create_all()
    new_user = User(username='john3', email='john3@example.com')
    db.session.add(new_user)
    db.session.commit()

    new_product = product(product_name='black short', product_sum=1000, product_discountrate=10, product_like=10, product_path='a')
    db.session.add(new_product)
    db.session.commit()

    users = User.query.all()
    print(users)

    user = User.query.filter_by(username='john3').first()
    print(user)

    users = User.query.filter_by(username='john3').all()
    for user in users:
        user.email = 'john@newexample.com'
    db.session.commit()

    User.query.filter_by(username='john3').update({'email': '<EMAIL>'})



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
    app.run(debug=True, use_reloader=False)