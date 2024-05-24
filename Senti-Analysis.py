import pandas as pd
from textblob import TextBlob
from transformers import pipeline
import json

with open('Iphone11-R.json', 'r') as file:
    data = json.load(file)

# Convert data to DataFrame
reviews_df = pd.DataFrame(data)

# Remove unnecessary columns
reviews_df = reviews_df[['review_text', 'review_rating']]

# Sentiment Analysis with TextBlob
def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

reviews_df['sentiment'] = reviews_df['review_text'].apply(get_sentiment)

# Classify the sentiment
reviews_df['sentiment_label'] = reviews_df['sentiment'].apply(lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral'))
print(reviews_df[['review_text', 'sentiment_label']].head())
print(reviews_df['sentiment_label'].value_counts())
