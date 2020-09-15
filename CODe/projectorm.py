import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserInput(Base) :
    '''HELLO WORLD ''' 
    __tablename__ = 'userinputs'

    id = Column(Integer, primary_key = True)
    house_area = Column(Integer)
    no_of_rooms = Column(Integer)
    age = Column(Integer)
    location = Column(String)
    
class Prediction(Base) :
    __tablename__ = 'prediction'
    
    id = Column(Integer, primary_key = True)
    result = Column(Integer)
    input_id = Column(Integer, ForeignKey('userinputs.id'))
    
if __name__ == "__main__":
    engine2 = create_engine('sqlite:///rishidatabase.sqlite3') # create Empty database name utkarsh.sqlite3
    Base.metadata.create_all(engine2) # create the above table