import re
from nltk.corpus import stopwords
from nltk.stem.snowball import PorterStemmer, SnowballStemmer
from nltk import word_tokenize
import pandas as pd


def normalize_text(text):
    stopwords_set= set(stopwords.words('english'))
    stemmer = SnowballStemmer('english')
    text = text.replace('\n',' ').lower().strip()
    text = re.sub("[^a-zA-Z]+", " ", text).split()
    text = ' '.join(stemmer.stem(i) for i in text)
    stemmed = ' '.join([word for word in text.split() if word not in stopwords_set])
    return(stemmed)

def if_topic_in(topic):
    topic_list = ["sports", "food", "music", "comedy","money","novel","poetry"]
    try:
        ls = list(set(topic).intersection(topic_list))
        ans=ls[0]
    except:
        ans = "None"
    return ans
def find_topic(t):
    t= normalize_text(t)
    words=word_tokenize(t)
    topic=if_topic_in(words)
    return topic
events=pd.read_csv('./data.csv', sep=",", encoding='cp1252')
events['group']=[find_topic(t) for t in events['description']]
print(events)
events.to_csv('data.csv', index=False)