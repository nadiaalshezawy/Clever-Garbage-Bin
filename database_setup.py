#program that set up the data base 
#!/usr/bin/env python3
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Date, Float
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(String, primary_key=True)
    name = Column(String(250), nullable=False)
    familynumber = Column(Integer, nullable=False)
    city = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)
    

class Measurement(Base):
    __tablename__ = 'measurement'

    id = Column(Integer, primary_key=True)
    wasteweight = Column(Float, nullable=False)
    recycleweight = Column(Float, nullable=False)
    barcode = Column(String, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id' : self.id,
            'wasteweight' : self.wasteweight,
            'recycleweight' : self.recycleweight,
            'barcode' : self.barcode,
            'user' : self.user,
            }




engine = create_engine('sqlite:///readingweight.db')
Base.metadata.create_all(engine)
