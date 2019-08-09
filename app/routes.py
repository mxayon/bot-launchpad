from flask import render_template, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Maximo'}
    posts = [
        {
            'bot': {'botname': 'mini-calc'},
            'function': 'basic arithmetic (2 user given values)'
        },
        {
            'bot': {'botname': 'palindrometer'},
            'function': 'checks if word is a palindrome'
        },
        {
            'bot': {'botname': 'thermobot'},
            'function': 'temparature analyzer'
        },
        {
            'bot': {'botname': 'count-drac'},
            'function': 'counts words in article given by user'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/workspace')
def workspace():
    return render_template('workspace.html', bot='Botswerk')

@app.route('/mini-calc')
def minicalc():
    return "I am MINI-CALC"


# '''
# <h1> Hello, ''' + user['username']+ '''!</h1>
# '''
