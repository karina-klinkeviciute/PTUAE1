import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///projects.db')
Base = declarative_base()


class Project(Base):
    __tablename__ = "Project"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.id} {self.name} - {self.price} {self.created_date}"


Base.metadata.create_all(engine)
