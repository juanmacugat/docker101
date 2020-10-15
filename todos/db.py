import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://{user}:{password}@{host}:5432/{db}'.format(
    user="admin",
    password= "admin",
    host="192.168.1.5",
    db="todo"))

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()