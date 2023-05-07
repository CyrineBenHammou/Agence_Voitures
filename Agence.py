from voiture import Voiture
import mysql.connector

import mysql.connector

class Agence:

    def __init__(self, voitures= []):
        self.voitures= voitures
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Agence"
        )

    def ajouter_voiture(self):
        while True:
            r = input("Voulez-vous ajouter une voiture? Y for yes | N for no ")
            if r == "Y":
                mat = input('Entrez matricule: ')
                if self.rechercher_voiture_par_mat(mat) == False:
                    print(" Ajouter une voiture ")
                    v = Voiture()
                    v.saisir()

                    # Insert the new Voiture object into the MySQL database
                    cursor = self.db.cursor()
                    sql = "INSERT INTO voiture (matricule, marque, modele) VALUES (%s, %s, %s)"
                    val = (v.matricule, v.marque, v.modele)
                    try:
                        cursor.execute(sql, val)
                        self.db.commit()
                        print(cursor.rowcount, "record inserted.")
                    except mysql.connector.Error as error:
                        print("Failed to insert record: {}".format(error))

                    r = input("Voulez-vous rajouter une autre voiture? Y for yes | N for no ")
                else:
                    print(" Cette Voiture existe déjà ! ")
            elif r == "N":
                print('Aucune voiture ajoutée')
                self.db.close()
                break



 def __init__(self, voitures= []):
        self.voitures= voitures