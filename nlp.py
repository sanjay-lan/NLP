!pip install nltk

paragraph = """Shah Rukh Khan, born 2 November 1965, also known by the initialism SRK, is an Indian actor and film producer who works in Hindi cinema. Referred to in the media as the "Baadshah of Bollywood" and "King Khan",[b] he has appeared in more than 100 films, and earned numerous accolades, including 14 Filmfare Awards. He has been awarded the Padma Shri by the Government of India, as well as the Order of Arts and Letters and Legion of Honour by the Government of France. Khan has a significant following in Asia and the Indian diaspora worldwide. In terms of audience size and income, several media outlets have described him as one of the most successful film stars in the world.[c] Many of his films thematise Indian national identity and connections with diaspora communities, or gender, racial, social and religious differences and grievances."""

paragraph

import nltk
from nltk.stem import PorterStemmer
nltk.download('stopwords')
from nltk.corpus import stopwords

# tokenization (paragraph to sentance)
nltk.download('punkt_tab')
sentences = nltk.sent_tokenize(paragraph)
sentences

#  stamming (gives root word)
stemmer = PorterStemmer()

# lemmatizer
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

import re
corpus = []
for i in range(len(sentences)):
  review=re.sub('[^a-zA-Z]', ' ', sentences[i])
  # review=re.sub(r'\s+', ' ', sentences[i])
  review= review.lower()
  corpus.append(review)

corpus

# stamming (the words may not be meaningfull but this process is fast)
for i in corpus:
  words = nltk.word_tokenize(i)
  for word in words:
    if word not in set(stopwords.words('english')):
      print(stemmer.stem(word))

# lammatizer (it gives some meaningfull words and this process is slow)
for i in corpus:
  words = nltk.word_tokenize(i) #converting each sentence to words
  for word in words: #go through all the words and apply lammatization
    if word not in set(stopwords.words('english')): #only taking that words that are not present in the stopwords
      print(lemmatizer.lemmatize(word))

from sklearn.feature_extraction.text import CountVectorizer # to do bag of words vectorization
cv = CountVectorizer(binary=True, ngram_range=(3,3)) #doing vectorization in binary
X= cv.fit_transform(corpus) #applying to corpus

#  all the words and their index number according to alphabetically or dictionary
cv.vocabulary_

# applying to the first sentence
corpus[0]

# applying bag of words for the first sentence and showing it
X[0].toarray()

# TF-IDF (it reduces sparse matrix and preserve some amount of symentic meaning of the words)
from sklearn.feature_extraction.text import TfidfVectorizer
cv = TfidfVectorizer(ngram_range=(3,3))
X= cv.fit_transform(corpus)

corpus[0]

X[0].toarray()

