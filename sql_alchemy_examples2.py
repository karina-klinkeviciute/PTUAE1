from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sql_alchemy_examples import Project

engine = create_engine('sqlite:///projects.db')
Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""

while True:
    choice = int(input("Choose action: \n1 - display projects \n2 - create a project \n3 - change project data \n4 - delete a project\n"))

    if choice == 1:
        projects = session.query(Project).all()
        print("-------------------")
        for project in projects:
            print(project)
        print("-------------------")

    if choice == 2:
        name = input("Enter the name of the project")
        price = float(input("Enter the price for the project"))
        project = Project(name, price)
        session.add(project)
        session.commit()

    if choice == 3:
        projects = session.query(Project).all()
        print("-------------------")
        for project in projects:
            print(project)
        print("-------------------")
        change_id = int(input("Chosse the ID of the project that you want to change"))
        project_to_change = session.get(Project, change_id)
        change = int(input("What do you want to change: 1 - name, 2 - price"))
        if change == 1:
            project_to_change.name = input("Enter project's name")
        if change == 2:
            project_to_change.price = float(input("Enter the price of the project"))
        session.commit()

    if choice == 4:
        projects = session.query(Project).all()
        print("-------------------")
        for project in projects:
            print(project)
        print("-------------------")
        delete_id = int(input("Enter the ID of the project that you want to change"))
        project_to_delete = session.get(Project, delete_id)
        session.delete(project_to_delete)
        session.commit()
