from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sql_alchemy_examples import Project

engine = create_engine("sqlite:///projects.db")

Session = sessionmaker(bind=engine)

session = Session()

# project1 = Project("Second project", 5000)
# session.add(project1)
# session.commit()

project1 = session.get(Project, 1)
print(project1)

project2 = session.query(Project).filter_by(name="Second project").one()
print(project2)

projects = session.query(Project).all()
for project in projects:
    print(project)

search = session.query(Project).filter(Project.name.ilike("Second%"))
for project in search:
    print(project)

search = session.query(Project).filter(Project.price > 3000)
for project in search:
    print(project)

search = session.query(Project).filter(Project.name.ilike("Second%"), Project.price > 3000)
for project in search:
    print(project)

project1.name = "First project"
project2.price = 4000
session.commit()

session.delete(project1)
session.commit()
