import sqlite3
import os

absolute_path = os.path.join(os.path.dirname(__file__), "database.db")

connection = sqlite3.connect(absolute_path)

cursor = connection.cursor()
"""
cursor.execute(" CREATE TABLE employees (
                id INTEGER PRIMARY KEY,
                name VARCHAR(20),
                salaire DECIMAL(6, 2)
               )
               ")
"""

"""
cursor.execute("INSERT INTO employees (name, salaire) VALUES ('PIERRE', 200)")

connection.commit()
"""
"""
cursor.executemany("INSERT INTO employees (name, salaire) VALUES (?, ?)",
                   [("MANY_PAUL", 500), ("MANY_ERNEST", 800)])
connection.commit()
"""

"""
cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(row)
"""

def getEmployeesName(cursor, salaire, operator = ">"):
    cursor.execute(f"SELECT * FROM employees WHERE salaire {operator} ?", (salaire,))
    for row in cursor.fetchall():
        print(row)

getEmployeesName(cursor, 400, "!=")

cursor.close()

connection.close()
