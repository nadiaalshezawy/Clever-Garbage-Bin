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

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


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
    totalwaste=0
    optimumwaste=0
    userdata= session.query(User).filter_by(id=user_id).one()
    #convert the date from input to datetime formate
    if request.method == 'POST':
        startdate = datetime.strptime(request.form['start'],'%Y-%m-%d')
        enddate =datetime.strptime(request.form['end'],'%Y-%m-%d')
        userWaste= session.query(MeasurementWaste).filter(MeasurementWaste.barcode==("W"+user_id),MeasurementWaste.date>=startdate,MeasurementWaste.date<=enddate).all()
        # finding the totale of optimum weight 
        for record in userWaste:
            totalwaste+=record.weight
            if optimumwaste==0:
                date1=record.date.date()
                optimumwaste+=(globWaste*userdata.familynumber)
            elif record.date.date() != date1:
                       optimumwaste+=(globWaste*userdata.familynumber)
                       date1=record.date.date()
                       
        return render_template('showWaste.html',user_id=user_id,waste=userWaste,totalwaste=totalwaste,optimumwaste=optimumwaste)
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
    totalrecycle=0
    totalwaste=0
    if request.method == 'POST':
        startdate = datetime.strptime(request.form['start'],'%Y-%m-%d')
        enddate =datetime.strptime(request.form['end'],'%Y-%m-%d')
        userRecycle= session.query(MeasurementRecycle).filter(MeasurementRecycle.barcode==("R"+user_id),MeasurementRecycle.date>=startdate,MeasurementRecycle.date<=enddate).all()
        userWaste= session.query(MeasurementWaste).filter(MeasurementWaste.barcode==("W"+user_id),MeasurementWaste.date>=startdate,MeasurementWaste.date<=enddate).all()
        # finding the totale of recycel weight and waste weight 
        for record in userWaste:
            totalwaste+=record.weight
        for record in userRecycle:
            totalrecycle+=record.weight
        percentrecycle=(totalrecycle/(totalrecycle+totalwaste))*100
        percentrecycle='%.3f'%percentrecycle
        return render_template('showRecycle.html',user_id=user_id,recycle=userRecycle,totalrecycle=totalrecycle,percentrecycle=percentrecycle)
    else:
        return render_template('recycleStatistics.html',user_id=user_id)

# show user recycle Statistics
@app.route('/user/<string:user_id>/statistics/recycle')
def showRecycle(user_id):
    userRecycle= session.query(MeasurementRecycle).filter_by(barcode=("R"+user_id)).all()
    return render_template('showRecycle.html',user_id=user_id,recycle=userRecycle)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)    