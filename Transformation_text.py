import nltk
from nltk.corpus import stopwords
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer
import os

class TransformationVoitureTexte(BaseEstimator, TransformerMixin):
    
    def __init__(self, language='french'):
        self.stopwords = set(stopwords.words(language))
        self.cv = CountVectorizer()
 
    def fit(self, X, y=None):
        def segmenter(document):
            tokens = nltk.word_tokenize(document.lower())
            return [token for token in tokens if token not in self.stopwords and token.isalpha()]
        
        self.cv = CountVectorizer(tokenizer=segmenter)
        self.cv.fit(X)

    def transform(self, X, y=None):
        return self.cv.transform(X)

if __name__ == '__main__':
    transformer = TransformationVoitureTexte()

    dir_path = os.getcwd()
    data_path=dir_path+'\\Txt_voiture'
    nameslist = os.listdir(data_path)
    Paths=[]
    for name in nameslist:      
        text_path = os.path.join(data_path, name) 
        Paths.append(text_path)

    Corpus = []
    for path in Paths:
        with open(path, 'r', encoding='latin-1') as file:
            for line in file:
                Corpus.append(line)
    
    transformer.fit(Corpus)
    X = transformer.transform(Corpus)
    print(X.toarray())