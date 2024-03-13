import sqlite3

conn = sqlite3.connect("employees2.db")

c = conn.cursor()


# c.execute("""CREATE TABLE employees (
#              name text,
#              surname text,
#              position text,
#              salary real)
# """)
#
# conn.commit()
# conn.close()


with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS employees2 (
                 name text,
                 surname text,
                 position text
                 -- salary real
                 )
    """)

# with conn:
#     c.execute("""
#     INSERT INTO employees (name, surname, position, salary)
#     VALUES ("James", "Bond", "programmer", 1900)
#
#     """)

# with conn:
#     c.execute("""
#     SELECT * FROM employees WHERE position = "programmer"
#
#     """)
#     for record in c.fetchall():
#         print(record)

# with conn:
#     c.execute("""
#     UPDATE employees
#     SET salary = 2500
#     WHERE name = "James"
#
#     """)
#
# with conn:
#     c.execute("""
#     DELETE FROM employees
#     WHERE name = "James"
#
#     """)

name = input("Enter your first name: ")
surname = input("Enter your last name: ")
position = input("Enter your position: ")
# salary = float(input("Enter your salary: "))

with conn:
    c.execute(f"""
    INSERT INTO employees2 VALUES("%s", "%s", "%s")
    
    """, (name, surname, position))
