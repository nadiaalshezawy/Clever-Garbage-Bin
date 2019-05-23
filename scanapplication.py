#!/usr/bin/env python
# Build A scanner application
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
APPLICATION_NAME = "scan application"
engine = create_engine('sqlite:///readingweight.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Show main page 
@app.route('/')
@app.route('/main')
def showMain():
	return render_template('showMain.html')
    #return "This page will show main page catalog"

# new reading
@app.route('/addreading', methods=['GET', 'POST'])
def addReading():
	if request.method == 'POST':
		barcode = request.form['barcode']
		weight =request.form['weight']
		print(barcode + " "+barcode[0]+" "+weight )
		#save the reading in recycle table in barcode start with R
		if barcode[0]=="R":
			readings= session.query(MeasurementRecycle).all()
			newreading = MeasurementRecycle(id=3, date=datetime.now(),barcode=request.form['barcode'], weight=request.form['weight']);
			session.add(newreading)
			session.commit()
			flash("new reading added!")
			print("recycle")
		#save the reading in waste table in barcode start with W
		elif barcode[0]=="W":
			readings= session.query(MeasurementWaste).all()
			newreading = MeasurementWaste(id=4, date=datetime.now(),barcode=request.form['barcode'], weight=request.form['weight']);
			session.add(newreading)
			session.commit()
			flash("new reading added!")
			print("Waste")
		return redirect(url_for('addReading'))
	return render_template('addReading.html')
    #return "This page will add reading"



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000, threaded=False)