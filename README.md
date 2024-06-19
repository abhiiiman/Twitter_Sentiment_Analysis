# Twitter Sentiment Analysis 🐦😃☹️

### This project leverages _Natural Language Processing_ __(NLP)__ and _Logistic Regression_ to classify the sentiment of tweets as either `positive` or `negative`. The model achieved an accuracy of `82%`. Below you'll find detailed instructions on how to set up and run this project locally, as well as how to use the deployed `Streamlit` app.

# Project Structure
<!-- Twitter_Sentiment_Analysis<br>
│<br>
├── Data<br>
│   └── dataset.csv<br>
│<br>
├── Models<br>
│   ├── Twitter_Model.sav<br>
│   └── Vectorizer.pkl<br>
│<br>
├── app.py<br>
├── README.md<br>
└── Twitter_Sentiment_Analysis.ipynb<br> -->
<!-- ![alt text](Screenshots\image2.png) -->
<p>
    <img src="Screenshots\image2.png"/>
</p>


## Setup Instructions

1. **Clone the Repository**

```html
git clone https://github.com/abhiiiman/Twitter_Sentiment_Analysis.git
```

```html
cd Twitter_Sentiment_Analysis
```

2. **Create a Virtual Environment**

```html
python -m venv venv
```
- Mac Users
```html
source venv/bin/activate 
```
- Windows Users
```html
venv\Scripts\activate
```

3. **Install Dependencies**

```html
pip install -r requirements.txt
```

4. **Download NLTK Data**

- In a Python shell, run:

```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

5. **Download the Dataset from here**
[Download the Dataset](https://www.kaggle.com/datasets/kazanova/sentiment140)

6. **Run the Streamlit App**

```html
streamlit run app.py
```

# Using the Deployed Streamlit App
1. Navigate to the Streamlit App [Click Here](https://twitter-sentiment-analysis-e1b1.onrender.com/)
2. Enter Tweet Content
3. Predict Sentiment
4. Screenshots
- Negative Tweet

<!-- ![alt text](Screenshots\image.png) -->
<p>
    <img src="Screenshots\image.png"/>
</p>

- Positive Tweet

<!-- ![alt text](Screenshots\image-1.png) -->
<p>
    <img src="Screenshots\image-1.png"/>
</p>

# Don't forget to give it a Star!

## _If you loved this project, give it a_ ⭐ _on GitHub! It would make my codebase as happy as a positive tweet_ 😄.
