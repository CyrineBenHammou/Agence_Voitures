from voiture import Voiture
import mysql.connector
from datetime import datetime

class Agence:
    def __init__(self, voitures=None):
        if voitures is None:
            voitures = []
        self.voitures = voitures
        
        # Connect to the MySQL database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Agence"
        )

    def afficher_voitures(self):
        # Execute a SELECT query to retrieve the data from the database table
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM liste_voitures")

        # Check if any rows were returned
        if cursor.rowcount == 0:
            print("No cars found in the database.")
            return

        # Iterate over the results and create instances of the Voiture class with the retrieved data
        for row in cursor:
            v = Voiture(
                matricule=row[0],
                marque=row[1],
                couleur=row[2],
                date_circulation=datetime.strptime(row[3]),
                kilometrage=row[4],
                cylindres=row[5],
                image=row[6]
            )

            # Call the afficher() method on each instance to display the data
            v.afficher()

        # Close the database connection
        self.db.close()

    


if __name__=='__main__':
    a=Agence()
    a.afficher_voitures()