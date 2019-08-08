from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Maximo'}
    posts = [
        {
            'bot': {'botname': 'Mini-Calc'},
            'function': 'basic arithmetic (2 user given values)'
        },
        {
            'bot': {'botname': 'Palindrometer'},
            'function': 'checks if word is a palindrome'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
    
@app.route('/about')
def about():
    return render_template('about.html', title='Home')

# '''
# <h1> Hello, ''' + user['username']+ '''!</h1>
# '''
