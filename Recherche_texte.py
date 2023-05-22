import numpy as np

class Recherche_par_similaritétxt():
    def calcule_distance(self, vecteur, liste):
        distances = np.linalg.norm(liste - vecteur, axis=1)
        return distances

    def trier_distance(self, distances, liste):
        # Combinez les distances et les vecteurs
        vecteurs_distances = list(zip(liste, distances))

        # Triez la liste en fonction des distances
        vecteurs_distances_tries = sorted(vecteurs_distances, key=lambda x: x[1])

    

        return vecteurs_distances_tries