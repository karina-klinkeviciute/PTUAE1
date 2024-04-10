from sqlalchemy.orm import sessionmaker
from sql_alchemy_example3 import engine, Child, Parent

Session = sessionmaker(bind=engine)
session = Session()

child = Child(name="John", surname="Smith", school="Smart kids school")
parent = Parent(name="Jane", surname="Smith", child=child)
session.add(parent)
session.commit()

children = session.query(Child).all()
print(children)

new_child = Child(name="Tom", surname="Smith")
parent = session.get(Parent, 1)
parent.child = new_child
parent.child.name = "Mathew"
session.commit()
session.delete(parent)

