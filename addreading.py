# program to add intial sample data to our database
#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import MeasurementWaste, Base,User,MeasurementRecycle 
from datetime import datetime 

engine = create_engine('sqlite:///readingweight.db')


# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user1
User1 = User(id="23123" ,name="Sulaiman Ibrahim", familynumber=6, city="Al Barsha2 ",address="street 23a, villa 20",wastelimit=18.0,recyclelimit=100.0)
session.add(User1)
session.commit()

# Create dummy user2
User2 = User(id="45678" ,name="Abdullah Mohammed", familynumber=10, city="Al Warqa3 ",address="street 14a , villa 34",wastelimit=18,recyclelimit=100)
session.add(User2)
session.commit()

# Create reading for readingweight of waste
measurement1 = MeasurementWaste(id=1, date=datetime.now(),barcode="W45678", weight=2.4)

session.add(measurement1)
session.commit()

# Create reading for readingweight of waste
measurement2 = MeasurementWaste(id=2, date=datetime.now(),barcode="W23123", weight=3.6)

session.add(measurement2)
session.commit()

# Create reading for readingweight of recycle
measurement1 = MeasurementRecycle(id=1, date=datetime.now(),barcode="R45678", weight=1.4)

session.add(measurement1)
session.commit()

# Create reading for readingweight of recycle
measurement2 = MeasurementRecycle(id=2, date=datetime.now(),barcode="R23123", weight=1.6)

session.add(measurement2)
session.commit()




print ("added menu items!")