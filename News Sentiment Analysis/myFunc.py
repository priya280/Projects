# imports 
import re
import nltk
import pandas as pd
import nltk 
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords 
import spacy 
nlp = spacy.load('en_core_web_lg')
import en_core_web_sm

def returnData(df):
    allSentence = []

    for text in df['Summary Text']:
        allSentence.append(text)

    lines = []

    for line in allSentence:
        words = line.split()
        for w in words:
            lines.append(w)

    lines  = [re.sub(r'[^A-Za-z0-9]+','',x) for x in lines]

    lines2 = []

    for words in lines:
        if words != '':
            lines2.append(words)

    s_stemmer = SnowballStemmer(language='english')

    stem = []

    for words in lines2: 
        if words not in nlp.Defaults.stop_words:
            stem.append(words)

    countingdf = pd.DataFrame(stem)

    countingdf = countingdf[0].value_counts()

    nlp = en_core_web_sm.load()

    str1 = " "
    stem2 = str1.join(lines2)
    stem2 = nlp(stem2)
    label = [(X.text,X.label_) for X in stem2.ents]
    edf1 = pd.DataFrame(label,columns=['Word','Entity'])
    edf2 = edf1.where(edf1['Entity'] == 'PERSON')
    edf3 = edf2['Word'].value_counts()

    return countingdf, edf3