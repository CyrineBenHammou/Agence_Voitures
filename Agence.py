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
            database="agence",
            consume_results=True
        )
        
    def get_data_DB(self):
        
        # Obtention de la data à partir de la base de données
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM liste_voitures")

        # Création d'une instance de voiture 
        for row in cursor:
                v = Voiture(
                    matricule=row[0],
                    marque=row[1],
                    couleur=row[2],
                    date_circulation=row[3],
                    kilometrage=row[4],
                    cylindres=row[5],
                    image=row[6]
                )
                self.voitures.append(v)

        # Déconnexion de la base de données
        cursor.close()

    def afficher_voitures(self):
        
        self.get_data_DB()
        if self.voitures:
            for V in self.voitures:
                print(V.afficher())
        else:
            print('Pas de voiture')

    def rechercher_voiture(self, matricule):
        self.get_data_DB()
        for v in self.voitures:
            if v.matricule == matricule:
                return True
        return False
    
    def ajouter_voiture(self):
        r = input("Voulez-vous ajouter une voiture? Y for yes | N for no ")
        while True:
            if r == "Y":
                matricule = input("Matricule: ")
                if self.rechercher_voiture(matricule):
                    print(f"A car with matricule {matricule} already exists in the database.")
                    break
                else:
                    # Prompt the user for the details of the new car
                    v = Voiture()
                    v.saisir()

                    # Execute an INSERT query to add the new car to the database
                    cursor = self.db.cursor(buffered=True)
                    query = "INSERT INTO liste_voitures (matricule, marque, couleur, date_circulation, kilometrage, cylindre, image) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    values = (v.matricule, v.marque, v.couleur, v.date_circulation, v.kilometrage, v.cylindres, v.image)
                    cursor.execute(query, values)

                    print(f"La voiture portant la matricule {v.matricule} a été ajoutée.")

                    # Close the cursor and commit the transaction
                    cursor.close()
                    self.db.commit()
                    r= input("Voulez-vous rajouter une autre voiture? Y for yes | N for no") 

            elif r == "N":
                print('Aucune voiture ajoutée')
                break

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
    
    def trier_selon_date_circulation(self):
            

        # Fetch data from the database and create Voiture objects
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM liste_voitures")
        rows = cursor.fetchall()
                    
        for row in rows:
            v = Voiture(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            self.voitures.append(v)
                    
        # Sort the list of cars according to their date of circulation
        self.voitures.sort( key=lambda v: v.date_circulation)
        
    def get_voiture_plus_recente(self):
        self.trier_selon_date_circulation()
        print("La voiture la plus récente est:")
        self.voitures[-1].afficher_voiture()

    def get_voiture_plus_ancienne(self):
         self.trier_selon_date_circulation()
         print("La voiture la plus ancienne est:")
         self.voitures[0].afficher_voiture()


if __name__=='__main__':
    a=Agence()
    a.get_data_DB()
    #a.ajouter_voiture()
    a.afficher_voitures()
    
    
