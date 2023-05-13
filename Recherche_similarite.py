import numpy as np


class Recherche_par_similarité():
    def calcule_distance(self, vecteur_normalise, liste_normalisee):
        distances = np.linalg.norm(liste_normalisee - vecteur_normalise, axis=1)
        print(distances)
        return distances

    def trier_distance(self, distances):
        
        
        indices_trie = np.argsort(distances)
        print(indices_trie)
        return indices_trie

    def afficher_voiture_similaire(self, df,indices_trie):
        
        # reorder rows in dataframe based on sorted indices
        df_trie = df.iloc[indices_trie]

        # display dataframe with sorted rows
        print(df_trie)
