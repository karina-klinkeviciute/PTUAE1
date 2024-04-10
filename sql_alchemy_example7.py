from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine('sqlite:///many_to_many_test.db')
Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('parent_id', Integer, ForeignKey("parent.id")),
    Column('child_id', Integer, ForeignKey("child.id"))
    )

class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    children = relationship("Child", secondary=association_table, back_populates="parents")

class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    school = Column(String)
    parents = relationship("Parent", secondary=association_table, back_populates="children")

Base.metadata.create_all(engine)
