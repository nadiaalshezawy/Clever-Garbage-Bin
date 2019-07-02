#!/usr/bin/env python
# Build A user application
# Done by : Nadia Ahmed
from flask import Flask, render_template, request
from flask import redirect, jsonify, url_for, flash
from sqlalchemy import create_engine,DateTime,cast, Date,extract,and_
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

# average globale waste variable
globWaste= 1.2

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
        #print(request.form['start'])
        #print(request.form['end'])
        #startdate = datetime.strptime(request.form['start'],'%Y-%m-%d').date()
        startdate = datetime.strptime(request.form['start'],'%Y-%m-%d')
        enddate =datetime.strptime(request.form['end'],'%Y-%m-%d')
        #rawdata= session.query(MeasurementWaste).filter_by(id=1).one()
        userWaste2= session.query(MeasurementWaste).filter(MeasurementWaste.barcode==("W"+user_id),MeasurementWaste.date>=startdate,MeasurementWaste.date<=enddate).all()
        #MeasurementWaste.barcode==("W"+user_id),
        #print(rawdata.date.month)
        #print(rawdata.date.date())
        #convert string input to date format
        #print(startdate);
        """ if rawdata.date.date() < startdate:
            print("start is bigger")
        else:
            print("start is smaller")"""
        #userWaste= session.query(MeasurementWaste).filter_by(barcode=("W"+user_id)).all()
        return render_template('showWaste.html',user_id=user_id,waste=userWaste2)
    else:
        return render_template('wasteStatistics.html',user_id=user_id)


# show user waste Statistic
@app.route('/user/<string:user_id>/statistics/waste')
def showWaste():
    userWaste= session.query(MeasurementWaste).filter_by(barcode=("W"+user_id)).all()
    return render_template('showWaste.html',user_id=user_id,waste=userWaste)

# user Recycle statistics
@app.route('/user/<string:user_id>/statistics/recycle',methods=['GET', 'POST'])
def recycleStatistics(user_id):
    if request.method == 'POST':
        startdate = datetime.strptime(request.form['start'],'%Y-%m-%d')
        enddate =datetime.strptime(request.form['end'],'%Y-%m-%d')
        userRecycle= session.query(MeasurementRecycle).filter(MeasurementRecycle.barcode==("R"+user_id),MeasurementRecycle.date>=startdate,MeasurementRecycle.date<=enddate).all()
        return render_template('showRecycle.html',user_id=user_id,recycle=userRecycle)
    else:
        return render_template('recycleStatistics.html',user_id=user_id)

# show user recycle Statistics
@app.route('/user/<string:user_id>/statistics/recycle')
def showRecycle(user_id):
    userRecycle= session.query(MeasurementRecycle).filter_by(barcode=("R"+user_id)).all()
    return render_template('showRecycle.html',user_id=user_id,recycle=userRecycle)

# show comment on user Waste statistics
@app.route('/user/<string:user_id>/statistics/wastecomment')
def showWasteComment(user_id):
	return render_template('showWasteComment.html',user_id=user_id) 

# show comment on user Recycle statistics
@app.route('/user/<string:user_id>/statistics/recyclecomment')
def showRecycleComment(user_id):
	return render_template('showRecycleComment.html',user_id=user_id)   

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)