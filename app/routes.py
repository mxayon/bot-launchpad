from flask import render_template, url_for
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
        },
        {
            'bot': {'botname': 'Thermobot'},
            'function': 'temparature analyzer'
        },
        {
            'bot': {'botname': 'Count-Drac'},
            'function': 'counts words in article given by user'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/workspace')
def workspace():
    return render_template('workspace.html')

# '''
# <h1> Hello, ''' + user['username']+ '''!</h1>
# '''
