import pandas as pd
from textblob import TextBlob

file_path = "/Users/giamihuynh/Downloads/TxtMin-Project-SA-1/Processed_Data/Final_Gendered_2.csv"
reviews_df = pd.read_csv(file_path)
reviews_df = reviews_df[reviews_df['gender'] != 'unknown']
reviews_df['review_text'] = reviews_df['review_text'].fillna('').astype(str)

# Sentiment Analysis with TextBlob
def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

reviews_df['sentiment'] = reviews_df['review_text'].apply(get_sentiment)

# Classify the sentiment
reviews_df['sentiment_label'] = reviews_df['sentiment'].apply(lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral'))
sentiment_counts = reviews_df.groupby(['gender', 'sentiment_label']).size().unstack(fill_value=0)
# print(sentiment_counts)

average_rating = reviews_df.groupby('gender')['review_rating'].mean()
average_sentiment_scores = reviews_df.groupby('gender')['sentiment'].mean()
print(average_sentiment_scores)