import sqlite3
import os
import argparse

parser = argparse.ArgumentParser(description="Explorer les donénes de la databse par titre")
parser.add_argument("titre", type=str, help="Titre du livre")

args = parser.parse_args()

absolute_path = os.path.join(os.path.dirname(__file__), "database_exerice.db")

connection = sqlite3.connect(absolute_path)

cursor = connection.cursor()


cursor.execute(""" CREATE TABLE IF NOT EXISTS Livres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    annee_publication INTEGER
)
               """)


""""
cursor.executemany("INSERT INTO Livres (titre, auteur, annee_publication) VALUES (?, ?, ?)", 
              [("Les Misérables", "Victor Hugo", 1862), ("Le Petit Prince", "Saint-Exupery", 1943)])

connection.commit()

cursor.execute("SELECT * FROM Livres")
for row in cursor.fetchall():
    print(row)
"""

def getLivreByTitle(cursor, titre):
    cursor.execute("SELECT * FROM Livres WHERE titre = ?", (titre,))
    for row in cursor.fetchall():
        print(row)

getLivreByTitle(cursor, args.titre)

cursor.close()

connection.close()
