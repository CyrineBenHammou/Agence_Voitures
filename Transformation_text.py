import nltk
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import word_tokenize
from sklearn.base import BaseEstimator, TransformerMixin


class TransformationVoitureTexte(BaseEstimator, TransformerMixin):
    def __init__(self, language='frensh'):
        # Initialisation de la classe
        self.vocabulaire = set()
        self.stop_words = set(stopwords.words(language))

    def fit(self, X, y=None):
        # Apprentissage du vocabulaire à partir des données d'entraînement
        for document in X:
            # Transformer le document en minuscule et le tokenizer en mots
            tokens = word_tokenize(document.lower())
            # Enlever les stopwords et les ponctuations
            tokens = [token for token in tokens if token not in self.stop_words and token.isalpha()]
            # Ajouter les mots au vocabulaire
            self.vocabulaire.update(tokens)
        return self

    def transform(self, X, y=None):
        # Transformation des données en vecteurs BoW
        BOW = []
        for document in X:
            # Compter le nombre d'occurrences de chaque mot dans le document
            counts = Counter()
            # Transformer le document en minuscule et le tokenizer en mots
            tokens = word_tokenize(document.lower())
            # Enlever les stopwords et les ponctuations
            tokens = [token for token in tokens if token not in self.stop_words and token.isalpha()]
            # Compter le nombre d'occurrences de chaque mot dans le document
            counts.update(tokens)
            # Créer un dictionnaire avec le mot et son nombre d'occurrences
            document_index = {mot: counts[mot] for mot in self.vocabulaire}
            # Ajouter l'index du document à la liste des index
            BOW.append(document_index)
        return BOW

if __name__ == '__main__' :
    # Créer une instance de la classe TransformationVoitureTexte
    transformer = TransformationVoitureTexte()

    # Définir un exemple de document texte décrivant une voiture
    texte_voiture = ['ma voiture est rapide.', 'La moto est plus rapide que la voiture.']
    # Transformer le document texte en un vecteur BoW
    transformer.fit(texte_voiture)
    vecteur_bow = transformer.transform(texte_voiture)

    # Afficher le vecteur BoW
    print(vecteur_bow)