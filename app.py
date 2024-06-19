import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

nltk.download('punkt')
nltk.download('stopwords')

# creating the helper functions to clean the text here.
def stemming(content):
    stemmer = PorterStemmer()
    content = content.lower()
    words = nltk.word_tokenize(content)
    cleaned_words = [word for word in words if word.isalnum()]  # remove non-alphanumeric characters
    filtered_words = [word for word in cleaned_words if word not in stopwords.words('english')]
    stemmed_words = [stemmer.stem(word) for word in filtered_words]
    return ' '.join(stemmed_words)

# creating the helper functions to perform text vectorization.
def vectorization(text, tfidf):
    vectorized_text = tfidf.transform([text])
    return vectorized_text

st.title("Twitter Sentiment Prediction")
st.header("😍\t😢")
st.subheader("Enter the Tweet below to predict")
text_input = st.text_area("Type here...")

# loading the model and vectorizer here
model = pickle.load(open(r"Twitter_Model.sav", 'rb'))
tfidf = pickle.load(open(r"Vectorizer.pkl", 'rb'))

if st.button("Predict Now"):

    # checking for any null input here.
    if text_input == '':
        st.warning("Please! provide some valid input before proceeding to Predict.")

    else:
        # Text Preprocessing here.
        cleaned_text = stemming(text_input)
        vector_input = vectorization(cleaned_text, tfidf)

        # predicting using the model here.
        result = model.predict(vector_input)[0]

        # classifying the result here.
        if result == 0:
            st.subheader(f"This is a Negative Tweet 😢")
        else:
            st.subheader(f"This is a Positive Tweet 😍")
