# try:
# 	import config
# 	SQLALCHEMY_DATABASE_URI = config.SQLALCHEMY_DATABASE_URI
# except ImportError:
# 	pass

import os
import time
from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime, date
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

basedir = os.path.abspath(os.path.dirname(__file__))

year = time.strftime("%Y")
current_time = datetime.utcnow()
title = 'Skill Streak'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is a temporary key that will be replaced once the app is deployed'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)

class NameForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	users = db.relationship('User', backref='role')

	def __repr__(self):
		return '<Role %r>' % self.name

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

	def __repr__(self):
		return '<User %r>' % self.username


def streak(user, year, month, day):
	today = date.today()
	start = date(year, month, day)
	return str(today - start)

@app.context_processor
def basics():
	return {'year':year, 'title':title, 'current_time':current_time, 'streak':streak}

# Views

# Main page view
@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.name.data).first()
		if user is None:
			user = User(username = form.name.data)
			db.session.add(user)
			session['known'] = False
		else:
			session['known'] = True
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('index'))
	return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))

# User view
@app.route('/user/<name>')
def user(name):
	agent = request.headers.get('User-Agent')
	return render_template('user.html', agent=agent, name=name)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('Looks like you have changed your name!')
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('signup'))
	return render_template('signup.html', form=form, name=session.get('name'))

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')

@app.errorhandler(500)
def server_error(e):
	return 'Aww snap, there was an internal error!', 500

if __name__ == '__main__':
	app.run(debug=True, port=8001)