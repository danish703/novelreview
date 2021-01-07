import pandas as pd
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from  django.conf import settings
from pathlib import Path
def polaritycheck(x):
    if x>0 and x<=0.5:
        return 0
    elif x>0.5:
        return 1
    else:
        return -1

def dataprepartion():
    data = pd.read_csv(Path.joinpath(settings.DATASET_LOCATION,'data.csv'), encoding="ISO-8859-1")
    #data = pd.read_csv('data.csv', encoding="ISO-8859-1")
    data = data.drop('Status', axis=1)
    data['Polarity'] = data['Review'].apply(lambda x: TextBlob(x).sentiment.polarity)
    data['pol_cat'] = data['Polarity'].apply(polaritycheck)
    data['Review'] = data['Review'].str.lower().str.strip()
    return data

def remove_stopwords(line):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(line)
    filterd_sentence= [w for w in word_tokens if not w in stop_words]
    return " ".join(filterd_sentence)

def datawithoutstopwords():
    data = dataprepartion()
    data['stop_review']= data['Review'].apply(lambda x:remove_stopwords(x))
    return data

def commentPredict(line):
    print(line)
    data = datawithoutstopwords()
    vect = CountVectorizer()
    X_train, X_test, Y_train, Y_test = train_test_split(data['stop_review'], data['pol_cat'], test_size=0.1,
                                                        random_state=324)
    tf_train = vect.fit_transform(X_train)
    tf_test = vect.transform(X_test)
    lr = LogisticRegression()
    lr.fit(tf_train, Y_train)
    c = vect.transform([remove_stopwords(line)])
    return [lr.predict(c)[0],TextBlob(line).sentiment.polarity]