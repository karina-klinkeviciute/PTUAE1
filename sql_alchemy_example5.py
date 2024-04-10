from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine('sqlite:///one_to_many_test.db')
Base = declarative_base()


class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    children = relationship("Child", back_populates="parent")


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    school = Column(String)
    parent_id = Column(ForeignKey("parent.id"))
    parent = relationship("Parent", back_populates="children")


    def __repr__(self):
        return f'{self.name} {self.surname} from school {self.school}'

Base.metadata.create_all(engine)
