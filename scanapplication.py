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

app = Flask(__name__)
APPLICATION_NAME = "scan application"
engine = create_engine('sqlite:///readingweight.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Show main page catalog
@app.route('/')
def showMain():
    return "This page will show main page catalog"


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000, threaded=False)