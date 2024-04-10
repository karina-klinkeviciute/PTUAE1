from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine('sqlite:///many2one_test.db')
Base = declarative_base()


class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    child_id = Column(Integer, ForeignKey('child.id'))
    child = relationship("Child")


class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    school = Column(String)

    def __repr__(self):
        return f'{self.name} {self.surname} from school {self.school}'

Base.metadata.create_all(engine)
