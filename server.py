from flask import Flask, render_template, url_for, redirect, request
from data import db, User
from user import create_new_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example_test_db.db'
db.init_app(app)

@app.route('/', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/create_user', methods=['POST', 'GET'])
def create_task():
    if request.method == 'POST': 
        username = request.form.get('username')
        password = request.form.get('password')

        create_new_user(username, password)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
