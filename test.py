import re
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from nltk.corpus import stopwords
from nltk.stem.snowball import PorterStemmer, SnowballStemmer
from nltk import word_tokenize
from collections import Counter


def normalize_text(text):
    stopwords_set= set(stopwords.words('english'))
    stemmer = SnowballStemmer('english')
    text = text.replace('\n',' ').lower().strip()
    text = re.sub("[^a-zA-Z]+", " ", text).split()
    text = ' '.join(stemmer.stem(i) for i in text)
    stemmed = ' '.join([word for word in text.split() if word not in stopwords_set])
    return(stemmed)

def if_topic_in(topic):
    """function to determine if each entry belongs to our topic list
    ---------------------------------------------

    :param topic: list of many topics of one article
    :param topic_list: list of pre-defined topics

    :returns: index of first element in the topic list that belongs to topic_list
    """
    topic_list = ["sports", "food", "music", "comedy", "poetry","money"]
    try:
        ans = list(set(topic).intersection(topic_list))
    except:
        ans = ""

    return ans
# grab the data
news = pd.read_csv("./data.csv")
# let's take a look at our data
news.head()
news['TEXT'] = [normalize_text(text) for text in news['description']]
for text in news['TEXT']:
    words=word_tokenize(text)
    topic=if_topic_in(words)
    print(topic)

news.head()
