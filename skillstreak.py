import os
import time
from flask import Flask, render_template

year = time.strftime("%Y")
title = 'Skill Streak'

app = Flask(__name__)

@app.context_processor
def basics():
	return {'year':year, 'title':title}

# Main page view
@app.route('/')
def index():
    return render_template('index.html')

# User view
@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, {name}!</h1>'.format(name=name)

if __name__ == '__main__':
	app.run(debug=True)