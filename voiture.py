from datetime import datetime
from PIL import Image




class Voiture:

    def __init__(self, matricule='', marque='', couleur='' ,date_circulation=datetime.now(), kilometrage=0, cylindres=0, image=None):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur
        self.date_circulation = date_circulation
        self.kilometrage = kilometrage
        self.cylindres = cylindres
        self.image = image

    def saisir(self):
        self.matricule = input("Entrez la matricule")
        self.marque = input("Entrez la marque")
        self.couleur = input("Entrez la couleur")
        self.date_circulation = input("Entrez la date_circulation") 
        self.date_circulation = datetime.strptime(self.date_circulation, "%d/%m/%Y") 
        self.kilometrage = int(input("Entrez le kilometrage"))
        self.cylindres = int(input("Entrez le nombre de cylindres"))
        self.image = input("Entrez le chemin de l'image")
        
    

    def afficher(self):

        print('{0:<15s}|{1:<8s}|{1:<8s}|{2:<15s}|{3:<8d}|{4:<4d}'.format(self.matricule,self.marque,self.date_circulation.strftime("%d/%m/%Y"),self.kilometrage,self.cylindres))
        if self.image:
            try:
                img = Image.open(self.image)
                img.show()
            except:
                print(f"Unable to load image from {self.image}")


