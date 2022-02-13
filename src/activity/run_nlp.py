import pandas as pd
import spacy
from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS
import nltk
from nltk.util import ngrams
import string
import collections
import re

punctuation = set(string.punctuation)
stop = STOP_WORDS
nlp = English()
tokenizer = nlp.tokenizer

def spacy_tokenizer_lemmatizer(text):
    tokens = tokenizer(text)
    
    lemma_list = []
    for token in tokens:
        if token.is_stop is False:
            lemma_list.append(token.lemma_)
    
    return(lemma_list)

def spacy_tokenizer_pos(text):
    tokens = tokenizer(text)
    
    pos_list = []
    for token in tokens:
        pos_list.append(token.pos_)
    
    return(pos_list)

def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F300-\U0001F5FF" 
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               u"\U00002500-\U00002BEF"
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"
                               u"\u3030"
                               "]+", flags=re.UNICODE)

    return emoji_pattern.sub(r'', string)

def find_ngram(data=None, number_of_ngrams=1, top=10):

    grams = ngrams(data, number_of_ngrams)
    grams_frequency = collections.Counter(grams)
    top_ngram = grams_frequency.most_common(top)
    top_ngram_df = pd.DataFrame(top_ngram, columns=['word', 'count'])
    #top_ngram_df['word'] = pd.DataFrame(top_ngram_df['word'].tolist())

    return top_ngram_df
