from sklearn.base import BaseEstimator,TransformerMixin
from skimage import color
import matplotlib.pyplot as plt
import numpy as np

class TransformationImageVoiture(BaseEstimator,TransformerMixin):
    def __init__(self) :
        return None
    
    def fit(self, X, y=None):
        X_=X.copy()
        return self

    def transform(self, X, y=None):

        X_=X.copy()
        X_ = color.rgb2gray(X_)
        X_ = np.resize(X_, (20,20))
        X_= X_.reshape(20*20)
        X_= X_.flatten()

        return X_