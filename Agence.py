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
            database="Agence",
            consume_results=True
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

    def rechercher_voiture(self, matricule):
            trouve = False
            # Execute a SELECT query to retrieve the data for the given matricule
            cursor = self.db.cursor(buffered=True)
            cursor.execute("SELECT Matricule FROM liste_voitures WHERE Matricule=%s", (matricule,))

            # Check if a row was returned
            if cursor.rowcount == 0:
                print(f"No car with matricule {matricule} found in the database.")
            else: trouve = True
            return trouve
    
    
    def ajouter_voiture(self):
        matricule = input("Matricule: ")
        
        if self.rechercher_voiture(matricule):
            print(f"A car with matricule {matricule} already exists in the database.")
        else:
            # Prompt the user for the details of the new car
            v = Voiture()
            v.saisir()

            # Execute an INSERT query to add the new car to the database
            cursor = self.db.cursor(buffered=True)
            query = "INSERT INTO liste_voitures (matricule, marque, couleur, date_circulation, kilometrage, cylindre, image) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (v.matricule, v.marque, v.couleur, v.date_circulation, v.kilometrage, v.cylindres, v.image)
            cursor.execute(query, values)

            print(f"The car with matricule {v.matricule} has been added to the database.")

            # Close the cursor and commit the transaction
            cursor.close()
            self.db.commit()

        # Close the database connection
        self.db.close()

    def supprimer_voiture(self):
        matricule = input("Enter the matricule of the car to delete: ")

        if self.rechercher_voiture(matricule)==False:
            print(f"A car with matricule {matricule} doesn't exist in the database.")
        else:
            # Execute a DELETE query to remove the car from the database
            cursor = self.db.cursor(buffered=True)
            query = "DELETE FROM liste_voitures WHERE Matricule=%s"
            values = (matricule,)
            cursor.execute(query, values)

            print(f"The car with matricule {matricule} has been deleted from the database.")

            # Close the cursor and commit the transaction
            cursor.close()
            self.db.commit()

        # Close the database connection
        self.db.close()

if __name__=='__main__':
    a=Agence()
    #a.rechercher_voiture('123')
    #a.supprimer_voiture()
    a.ajouter_voiture()