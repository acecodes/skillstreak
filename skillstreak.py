import os
import time
from flask import Flask, render_template

year = time.strftime("%Y")
title = 'Skill Streak'

app = Flask(__name__)

@app.context_processor
def basics():
	return {'year':year, 'title':title}

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)