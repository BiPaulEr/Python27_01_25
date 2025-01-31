import sqlite3
import os
import argparse

class ConnexionDatabase:
    def __init__(self, url):
        self.url = url
    def __enter__(self):
        self.connection = sqlite3.connect(self.url)
        return self.connection
     
    def __exit__(self, exc_type, exc_instance, traceback):
        if (exc_type):
            print(f"{exc_type} {exc_instance}")
        if self.connection:
            self.connection.close()
        return True

class CursorDatabase:
    def __init__(self, connection):
        self.connection = connection

    def __enter__(self):
        self.cursor = connection.cursor()
        return self.cursor
     
    def __exit__(self, exc_type, exc_instance, traceback):
        if (exc_type):
            print(f"{exc_type} {exc_instance}")
            if(self.connection):
                self.connection.rollback()
        else:
            if(self.connection):
                self.connection.commit()  
        if cursor:
            self.cursor.close()
        return True

def getLivreByTitle(cursor, titre):
    cursor.execute("SELECT * FROM Livres WHERE titre = ?", (titre,))
    for row in cursor.fetchall():
        print(row)

parser = argparse.ArgumentParser(description="Explorer les donénes de la databse par titre")
parser.add_argument("titre", type=str, help="Titre du livre")
args = parser.parse_args()

absolute_path = os.path.join(os.path.dirname(__file__), "database_exerice.db")

with ConnexionDatabase(absolute_path) as connection:
    with CursorDatabase(connection) as cursor:
        getLivreByTitle(cursor, args.titre)

print("end")