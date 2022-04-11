import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = db.create_engine('sqlite:///real_ventures.db')

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
