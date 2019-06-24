#!/usr/bin/env python
# Build A user application
# Done by : Nadia Ahmed
from flask import Flask, render_template, request
from flask import redirect, jsonify, url_for, flash
from sqlalchemy import create_engine,DateTime,and_
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
def userMain():
	return render_template('userMain.html')
	#return "This page will show main page "

# Show user page 
@app.route('/user',methods=['GET', 'POST'])
def userLogin():
	if request.method == 'POST':
		userId=request.form['id']
		userdata= session.query(User).filter_by(id=userId).one()
		#print(userId)
		return render_template('userStatistics.html',user_id=userId,user=userdata)
	else:
	    return render_template('userLogin.html')
	#return "This page will show user "

# Show user page 
@app.route('/user/<string:user_id>/statistics')
def userStatistics(user_id,user):
	return render_template('userStatistics.html',user_id=user_id,user=user)

#show user info
@app.route('/user/<string:user_id>/statistics/info')
def userInfo(user_id):
	userdata= session.query(User).filter_by(id=user_id).one()
	return render_template('userInfo.html',user=userdata)

# user waste statistics
@app.route('/user/<string:user_id>/statistics/waste',methods=['GET', 'POST'])
def wasteStatistics(user_id):
	if request.method == 'POST':
		print(request.form['start'])
		print(request.form['end'])
		userWaste= session.query(MeasurementWaste).filter_by(barcode=("W"+user_id)).all()
		return render_template('showWaste.html',user_id=user_id,waste=userWaste)
	else:
		#userWaste= session.query(MeasurementWaste).filter_by(barcode=("W"+user_id)).all()
		return render_template('wasteStatistics.html',user_id=user_id)

# show user waste Statistic
@app.route('/user/<string:user_id>/statistics/waste')
def showWaste():
	userWaste= session.query(MeasurementWaste).filter_by(barcode=("W"+user_id)).all()
	return render_template('showWaste.html',user_id=user_id,waste=userWaste)
	

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)