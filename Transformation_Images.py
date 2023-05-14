from sklearn.base import BaseEstimator,TransformerMixin
from skimage import color
import numpy as np
from skimage.io import imread

class TransformationImageVoiture(BaseEstimator,TransformerMixin):
    def __init__(self) :
        return None
    
    def fit(self, X_, y=None):
        
        return self

    def transform(self, X_, y=None):

       
        X_ = imread(X_)
        X_ = color.rgb2gray(X_)
        X_ = np.resize(X_, (20,20))
        X_= X_.reshape(20*20)
        X_= X_.flatten()

        return X_