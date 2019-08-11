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

@app.route('/palindrometer')
def palindrometer():
    return "I am PALINDROMETER"

@app.route('/thermobot')
def thermobot():
    return "I am THERMOBOT"

@app.route('/count-drac')
def countdrac():
    return "I am COUNT-DRAC"

@app.route('/show/<inte>')
def show(inte):
  my_greeting = "Your number is " + str(inte)
  return render_template("index.html", greeting=my_greeting)


# '''
# <h1> Hello, ''' + user['username']+ '''!</h1>
# '''
