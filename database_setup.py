#program that set up the data base 
#!/usr/bin/env python3
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Float
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
    wastelimit = Column(Float, nullable=False)
    recyclelimit = Column(Float, nullable=False)
    

class MeasurementWaste(Base):
    __tablename__ = 'measurementwaste'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime,nullable=False)
    barcode = Column(String, ForeignKey('user.id'))
    weight = Column(Float, nullable=False)
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id' : self.id,
            'date' : self.date,
            'barcode' : self.barcode,
            'weight' : self.weight,
            'user' : self.user,
            }

class MeasurementRecycle(Base):
    __tablename__ = 'measurementrecycle'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime,nullable=False)
    barcode = Column(String, ForeignKey('user.id'))
    weight = Column(Float, nullable=False)
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id' : self.id,
            'date' : self.date,
            'barcode' : self.barcode,
            'weight' : self.weight,
            'user' : self.user,
            }




engine = create_engine('sqlite:///readingweight.db')
Base.metadata.create_all(engine)
