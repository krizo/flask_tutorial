from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = { 'username': 'Kriz' }
    posts = [
        {
            'author': user,
            'body': 'Yay, first blog entry'
        },
        {
            'author': { 'username': 'Susan' },
            'body': 'And the second one'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
