import os
import time
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

year = time.strftime("%Y")
title = 'Skill Streak'

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.context_processor
def basics():
	return {'year':year, 'title':title}

# Views

# Main page view
@app.route('/')
def index():
    return render_template('index.html')

# User view
@app.route('/user/<name>')
def user(name):
	agent = request.headers.get('User-Agent')
	return '<h1>Hello, {name}!</h1>\nYou are using {agent}'.format(name=name, agent=agent)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')

@app.errorhandler(500)
def server_error(e):
	return 'Aww snap, there was an internal error!', 500

if __name__ == '__main__':
	app.run(debug=True)