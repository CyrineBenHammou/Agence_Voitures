from sklearn.base import BaseEstimator,TransformerMixin
import pandas as pd
import datetime
from sklearn.preprocessing import OneHotEncoder, StandardScaler



class TransformationVoiture(BaseEstimator,TransformerMixin):

    def __init__(self,date_to='annee'):
    # Hyperparametere : date_to
        self.date_to = date_to
    

    def fit(self, X, y=None):
        X_=X.copy()
        return self
    
    def transform(self, X, y=None):

        X_=X.copy()

        # suppression de colonne matricule
        X_ = X_.drop(columns=['Matricule'], axis=1)

        # transformation de la colonne date_circulation en age
        X_['Date_circulation'] = pd.to_datetime(X_['Date_circulation'])
        X_['age'] = datetime.datetime.now().year - X_['Date_circulation'].dt.year

        # suppression de la colonne date_circulation
        X_ = X_.drop(columns=['Date_circulation'], axis=1)


        # transformation de la colonne marque en one hot encoding
        OHE = OneHotEncoder()
        transformed = OHE.fit_transform(X_[['Marque']])
        X_.drop(columns = ['Marque'],inplace=True)
        X_[OHE.categories_[0]] = transformed.toarray()


        # transformation de la colonne couleur en one hot encoding
        transformed = OHE.fit_transform(X_[['Couleur']])
        X_.drop(columns = ['Couleur'],inplace=True)
        X_[OHE.categories_[0]] = transformed.toarray()
        

        #Normalisation des données
        ss=StandardScaler()
        ss.fit(X_)
        X_=ss.transform(X_)
        
        return X_