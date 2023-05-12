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
                    print(f"La voiture portant la matricule {matricule} existe déjà.")
                    break
                else:
                    # Saisie des données de la voiture
                    v = Voiture()
                    v.saisir()

                    # Ajouter voiture dans la base
                    cursor = self.db.cursor(buffered=True)
                    query = "INSERT INTO liste_voitures (matricule, marque, couleur, date_circulation, kilometrage, cylindre, image) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    values = (v.matricule, v.marque, v.couleur, v.date_circulation, v.kilometrage, v.cylindres, v.image)
                    cursor.execute(query, values)

                    print(f"La voiture portant la matricule {v.matricule} a été ajoutée.")

                    # Fermer cursor et commit la transaction
                    cursor.close()
                    self.db.commit()
                    r= input("Voulez-vous rajouter une autre voiture? Y for yes | N for no") 

            elif r == "N":
                print('Aucune voiture ajoutée')
                break

            # Déconnexion de la base
            self.db.close()


    def supprimer_voiture(self):
        matricule = input("Entre la matricule de la voiture que vous voulez supprimer: ")

        if self.rechercher_voiture(matricule)==False:
            print(f"La voiture portant la matricule {matricule} n'existe pas.")
        else:
            # Supprimer la voiture de la base de données
            cursor = self.db.cursor(buffered=True)
            query = "DELETE FROM liste_voitures WHERE Matricule=%s"
            values = (matricule,)
            cursor.execute(query, values)

            print(f"La voiture portant la matricule {matricule} a été supprimer de la base de données.")

            # Close the cursor and commit the transaction
            cursor.close()
            self.db.commit()
            
            # Close the database connection
            self.db.close()
    
    def trier_selon_date_circulation(self):
        self.get_data_DB()

        #Fonction de trie
        self.voitures.sort(key=lambda v: v.date_circulation)
        
    def get_voiture_plus_recente(self):
        self.get_data_DB()
        self.trier_selon_date_circulation()
        print("La voiture la plus récente est:")
        self.voitures[-1].afficher()

    def get_voiture_plus_ancienne(self):
         self.trier_selon_date_circulation()
         print("La voiture la plus ancienne est:")
         self.voitures[0].afficher()


    
