from sklearn.base import BaseEstimator,TransformerMixin
import pandas as pd
import datetime
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.decomposition import  PCA


class TransformationVoiture(BaseEstimator,TransformerMixin):

    def __init__(self,date_to='annee') :
    # Hyperparametere 2 : date_to
        self.date_to = date_to
        self.ohe = OneHotEncoder(sparse=False)
        self.ss = StandardScaler()     

    def fit(self, X, y=None):
        X_=X.copy()

        # parametere : objet One Hot Encoder
        
        self.ohe.fit(X_[['marque', 'couleur']])

        # parametre : objet Standard Scaler
        
        self.ss.fit()
        
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

        # transform 'marque' column to one-hot encoding
        marque_encoded=self.ohe.transform(X_[['marque']])
        df_marque = pd.DataFrame(marque_encoded.toarray(), 
                         columns=['marque_'+str(cat) for cat in self.ohe.categories_[0]],
                         index=X_.index)
        X_=pd.concat([X_,df_marque], axis=1)
        X_.drop('marque', axis=1, inplace=True, errors='ignore')

        # transform 'couleur' column to one-hot encoding
        couleur_encoded=self.ohe.transform(X_[['couleur']])
        df_couleur = pd.DataFrame(couleur_encoded.toarray(), 
                          columns=['couleur_'+str(cat) for cat in self.ohe.categories_[0]],
                          index=X_.index)
        X_=pd.concat([X_,df_couleur], axis=1)
        X_.drop('couleur', axis=1, inplace=True, errors='ignore')

        
        #Normalisation des données
        X_=self.ss.transform(X_)

        return X_ 