import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://{user}:{password}@{host}:5432/{db}'.format(
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASS"],
    host=os.environ["DB_HOST"],
    db="todo"))

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()