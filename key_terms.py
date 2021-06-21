#!/usr/bin/env python3
import string
import nltk
from lxml import etree
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
# from collections import Counter
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

xml_path = 'news.xml'
stop_words = stopwords.words('english')
lemmatizer = WordNetLemmatizer()
vectorizer = TfidfVectorizer(analyzer='word')
headers = []
dataset = []

with open(xml_path) as file:
    root = etree.parse(file).getroot()


for news in root[0]:
    headers.append(news[0].text)
    tokens = word_tokenize(news[1].text.lower())
    lemma = []
    doc = ''

    for n in range(len(tokens)):
        tokens[n] = lemmatizer.lemmatize(tokens[n], pos='n')
        if tokens[n] not in list(string.punctuation) and tokens[n] not in stop_words:
            lemma.append(tokens[n])

    nouns = [nltk.pos_tag([lem])[0][0] for lem in lemma if nltk.pos_tag([lem])[0][1] == 'NN']
    for noun in nouns:
        doc += noun + ' '
    dataset.append(doc)

tfidf_matrix = vectorizer.fit_transform(dataset)
for head in range(len(headers)):
    print(headers[head], ':', sep='')
    tf_idf = pd.DataFrame(data=tfidf_matrix[head].toarray().reshape(tfidf_matrix[head].shape[1], 1), index=vectorizer.get_feature_names(), columns=['tfidf'])
    freq_counter = sorted(tf_idf.to_dict()['tfidf'].items(), key=lambda x: (x[1], x[0]), reverse=True)
    # freq_counter = Counter([nltk.pos_tag([lem])[0][0] for lem in lemma if nltk.pos_tag([lem])[0][1] == 'NN'])
    # freq_counter = sorted(freq_counter.most_common(), key=lambda x: (x[1], x[0]), reverse=True)

    for i in range(5):
        print(freq_counter[i][0], end=' ')
    print()
    print()
