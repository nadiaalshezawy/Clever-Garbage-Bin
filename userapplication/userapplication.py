#!/usr/bin/env python
# Build A user application
# Done by : Nadia Ahmed
from flask import Flask, render_template, request
from flask import redirect, jsonify, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exists
from database_setup import MeasurementWaste, Base,User,MeasurementRecycle 
from flask import session as login_session
from datetime import datetime

app = Flask(__name__)
APPLICATION_NAME = "user application"
engine = create_engine('sqlite:///readingweight.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Show main page 
@app.route('/')
@app.route('/main')
def showMain():
	return render_template('userMain.html')
	#return "This page will show main page "

# Show user page 
@app.route('/user')
def userLogin():
	return render_template('userLogin.html')
	#return "This page will show user "

# Show user page 
@app.route('/user/<int:user_id>/')
def userStatistics(user_id):
	return render_template('userStatistics.html')
	#return "This page will show user "


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)