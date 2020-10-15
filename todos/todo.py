from sqlalchemy import Column, Integer, String

import db


class Todo(db.Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)

    def __init__(self, description):
        self.description = description