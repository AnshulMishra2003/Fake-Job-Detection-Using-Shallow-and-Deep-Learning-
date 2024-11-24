import streamlit as st 
import matplotlib.pyplot as plt
import joblib
import re
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from nltk.corpus import stopwords

siteHeader = st.container()
viz_word_cloud = st.container()

stopwords= set(['br', 'the', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",\
            "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', \
            'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their',\
            'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', \
            'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', \
            'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', \
            'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',\
            'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',\
            'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',\
            'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', \
            's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', \
            've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn',\
            "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',\
            "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", \
            'won', "won't", 'wouldn', "wouldn't"])

def decontracted(phrase):
    # specific
    phrase = re.sub(r"won't", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase

def preprocess(text):

    preprocessed = []
    text = re.sub(r"http\S+", "", text)
    text = BeautifulSoup(text, 'lxml').get_text()
    text = decontracted(text)
    text = re.sub("\S*\d\S*", "", text).strip()
    text = re.sub('[^A-Za-z]+', ' ', text)
    text = ' '.join(e.lower() for e in text.split() if e.lower() not in stopwords)
    preprocessed.append(text.strip())

    return preprocessed

def create_wordcloud(model, topic):
    fig = plt.figure(figsize=(6,6))
    text = {word: value for word, value in model.get_topic(topic)}
    print(text)
    wc = WordCloud(max_words=100, stopwords=stopwords)
    wc.generate_from_frequencies(text)
    plt.imshow(wc, interpolation="bilinear")
    plt.title('Word cloud with BERTopic model')
    plt.axis("off")
    st.pyplot(fig)
    #st.pyplot(plt.gcf()) 

def create_wordcloud_no_model(text):
  
   fig = plt.figure(figsize=(6,6))  
   wc = WordCloud(max_words=100, stopwords=stopwords)
   wc.generate(text) 
    
   plt.imshow(wc, interpolation="bilinear")
   plt.title('Word cloud without model')
   plt.axis("off")
   st.pyplot(fig)


with siteHeader:
  st.title('Welcome to Fake Job Detection App!')

  # Add a description 
  st.write('The app visualize the word cloud in regards to the entered Job description!') 

  # Create a text input for job description
  user_input = st.text_input('Please Enter the job description in English:') 
  # Display the job description
  if user_input:
    st.write('Job description: ', user_input)
    cleaned_description = preprocess(user_input)[0]  
    st.write('After cleaning Job description: ', cleaned_description)

with viz_word_cloud:
  word_cloud = st.button('Visualize word cloud', disabled=not user_input) 

  if word_cloud:
    create_wordcloud_no_model(cleaned_description)

    topic_model = joblib.load('../model/berttopic')
    create_wordcloud(topic_model, topic=0)
