import pandas as pd
from textblob import TextBlob
import csv
from collections import Counter
import re

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
# print(average_sentiment_scores)

def analyze_word_repetition_by_gender(data, gender):
    word_counter = Counter()

    for review in data:
        # Check if the review belongs to the specified gender
        if review['gender'] == gender:
            words = re.findall(r'\b\w+\b', review['review_text'].lower())
            word_counter.update(words)

    unique_words = len(word_counter)
    repeated_words = sum(count - 1 for count in word_counter.values() if count > 1)

    print(f"Total unique words: {unique_words}")
    print(f"Total repeated words: {repeated_words}")

    repetition_ratio = repeated_words / unique_words
    print(f"Repetition ratio: {repetition_ratio:.2f}")

    return word_counter

if __name__ == "__main__":
    data = []
    with open('/Users/giamihuynh/Downloads/TxtMin-Project-SA-1/Processed_Data/Final_Gendered_2.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

# Analyze word repetition for each gender
genders = ['male', 'female']
for gender in genders:
    print(f"\n{gender} reviews:")
    word_counter = analyze_word_repetition_by_gender(data, gender)

# Print the most common words for each gender
print(f"Most common words:")
print(word_counter.most_common(10))
