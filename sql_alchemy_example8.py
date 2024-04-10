from sqlalchemy.orm import sessionmaker
from sql_alchemy_example7 import engine, Child, Parent

Session = sessionmaker(bind=engine)
session = Session()

parent = Parent(name="Jack", surname="Johnson")
parent2 = Parent(name="Tina", surname="Johnson")
child1 = Child(name="Simone", surname="Johnson")
child2 = Child(name="Thomas", surname="Johnson")

parent.children.append(child1)
parent2.children.append(child1)
parent2.children.append(child2)

session.add(parent)
session.add(parent2)
session.commit()

parent = session.get(Parent, 1)
for child in parent.children:
    print(child.name, child.surname)

child = session.get(Child, 1)
for parent in child.parents:
    print(parent.name)

parent.children[0].name = "John"
session.commit()

child.parents[0].name = "Ryan"
session.commit()

child1 = parent.children[0]
parent.children.remove(child1)
session.commit()
