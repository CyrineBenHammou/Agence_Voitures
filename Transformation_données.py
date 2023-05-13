from sklearn.base import BaseEstimator,TransformerMixin
import pandas as pd
import datetime
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.decomposition import  PCA


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
        X_ = X_.drop(columns=['matricule'], axis=1)

        # transformation de la colonne date_circulation en age
        X_['date_circulation'] = pd.to_datetime(X_['date_circulation'])
        if self.date_to=='annee':
            X_['annee']=X_['date_circulation'].apply(lambda date : date.year)
        elif self.date_to=='age':
            X_['age']=X_['date_circulation'].apply(lambda date : datetime.now().year - date.year)

        

        # suppression de la colonne date_circulation
        X_ = X_.drop(columns=['date_circulation'], axis=1)

        # transformation de la colonne marque en one hot encoding
        OHE = OneHotEncoder()
        transformed = OHE.fit_transform(X_[['marque']])
        X_.drop(columns = ['marque'],inplace=True)
        X_[OHE.categories_[0]] = transformed.toarray()

        # transformation de la colonne couleur en one hot encoding
        transformed = OHE.fit_transform(X_[['couleur']])
        X_.drop(columns = ['couleur'],inplace=True)
        X_[OHE.categories_[0]] = transformed.toarray()
        
        #Normalisation des données
        ss=StandardScaler()
        ss.fit(X_)
        X_=ss.transform(X_)

        #Reduction des dimensions 
        pca=PCA(n_components=2)
        pca.fit(X_)
        X_=pca.transform(X_)
        
        return X_