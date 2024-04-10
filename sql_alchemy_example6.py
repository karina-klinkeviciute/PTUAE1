from sqlalchemy.orm import sessionmaker
from sql_alchemy_example5 import engine, Child, Parent

Session = sessionmaker(bind=engine)
session = Session()

child = Child(name="Simon", surname="Thompson")
child2 = Child(name="Aisha", surname="Thompson")
parent = Parent(name="Lina", surname="Thompson")
parent.children.append(child)
parent.children.append(child2)
session.add(parent)
session.commit()

parent = session.get(Parent, 1)
for child in parent.children:
    print(child.name, child.surname)

parent.children[0].name = "Jack"
session.commit()

print(child2.parent.name)

child3 = parent.children[0]
parent.children.remove(child3)
session.commit()
