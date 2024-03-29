from flask import Flask, render_template, url_for, flash, redirect
from app import app
from app.forms import RegisterForm, LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Maximo'}
    posts = [
        {
            'bot': {'botname': 'mini-calc'},
            'function': 'basic arithmetic (2 user given values)',
            'id':'1',
            'status': 'ready to launch!'
        },
        {
            'bot': {'botname': 'palindrometer'},
            'function': 'checks if word is a palindrome',
            'id':'2',
            'status': 'uploading...'
        },
        {
            'bot': {'botname': 'thermobot'},
            'function': 'temparature analyzer',
            'id':'3',
            'status': 'coming soon...'
        },
        {
            'bot': {'botname': 'count-drac'},
            'function': 'counts words in article given by user',
            'id':'4',
            'status': 'in progress...'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('Home'))
    return render_template('register.html', title='Sign Up', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Log In', form=form)

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
