# program to add intial sample data to our database
#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Measurement, Base, User

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
User1 = User(id="23123" ,name="Sulaiman Ibrahim", familynumber=6, city="Al Barsha2 ",address="street 23a, villa 20")
session.add(User1)
session.commit()

# Create dummy user2
User2 = User(id="45678" ,name="Abdullah Mohammed", familynumber=10, city="Al Warqa3 ",address="street 14a , villa 34")
session.add(User2)
session.commit()

# Create reading for readingweight
measurement1 = Measurement(id=1, barcode="45678", wasteweight=2.4, recycleweight=1.3, comment="The waste weight is over averge")

session.add(measurement1)
session.commit()

# Create reading for readingweight
measurement2 = Measurement(id=2, barcode="23123", wasteweight=3.6, recycleweight=1, comment="The waste weight is over averge ")

session.add(measurement2)
session.commit()




print ("added menu items!")