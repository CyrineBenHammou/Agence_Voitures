from datetime import datetime 



class Voiture:

    def __init__(self, matricule='', marque='', date_circulation=datetime.now(), kilometrage=0, cylindres=0):
        self.matricule = matricule
        self.marque = marque
        self.date_circulation = date_circulation
        self.kilometrage = kilometrage
        self.cylindres = cylindres

    def saisir(self):
        self.matricule = input("Entrez la matricule")
        self.marque = input("Entrez la marque")
        self.date_circulation = input("Entrez la date_circulation") 
        self.date_circulation = datetime.strptime(self.date_circulation, "%d/%m/%Y") 
        self.kilometrage = input("Entrez le kilometrage")
        self.cylindres = input("Entrez le nombre de cylindres")
    

    def afficher(self):

        print('{0:<15s}|{1:<8s}|{2:<15s}|{3:<8s}|{4:<4s}'.format(self.matricule,self.marque,self.date_circulation.strftime("%d/%m/%Y"),self.kilometrage,self.cylindres))