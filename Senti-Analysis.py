# -*- coding: utf-8 -*-
"""
@author: giami
"""

import pandas as pd
from textblob import TextBlob
import csv
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import seaborn as sns
import string 
from sklearn.metrics import accuracy_score

# Download the stop words list
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

file_path = "/Users/giamihuynh/Downloads/TxtMin-Project-SA-1/Processed_Data/Final_Gendered_2.csv"
reviews_df = pd.read_csv(file_path)
reviews_df = reviews_df[reviews_df['gender'] != 'unknown']
reviews_df['review_text'] = reviews_df['review_text'].fillna('').astype(str)

# Sentiment Analysis
def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

reviews_df['sentiment'] = reviews_df['review_text'].apply(get_sentiment)

# Classify the sentiment
reviews_df['sentiment_label'] = reviews_df['sentiment'].apply(lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral'))
sentiment_counts = reviews_df.groupby(['gender', 'sentiment_label']).size().unstack(fill_value=0)
average_sentiment_scores = reviews_df.groupby('gender')['sentiment'].mean()

# Calculate mode of review ratings for each gender
mode_rating = reviews_df.groupby('gender')['review_rating'].agg(lambda x: x.mode().iloc[0])
average_rating = reviews_df.groupby('gender')['review_rating'].mean()

print(average_rating)
print(mode_rating)
print(average_sentiment_scores)

# List of words to exclude (extremely common word)
exclude_words = {'good'}
# 'good', 'awesome', 'best', 'great', 'nice', 'excellent', 'amazing'

def analyze_sentimental_words_by_gender(data, gender):
    word_counter = Counter()
    sentimental_word_counter = Counter()

    for review in data:
        if review['gender'] == gender:
            words = re.findall(r'\b\w+\b', review['review_text'].lower())
            filtered_words = [word for word in words if word not in stop_words and word not in exclude_words]
            
            for word in filtered_words:
                word_counter[word] += 1
                word_sentiment = TextBlob(word).sentiment.polarity
                if word_sentiment != 0: 
                    sentimental_word_counter[word] += 1

    unique_words = len(word_counter)
    repeated_words = sum(count - 1 for count in word_counter.values() if count > 1)

    print(f"Total unique words for {gender}: {unique_words}")
    print(f"Total repeated words for {gender}: {repeated_words}")

    repetition_ratio = repeated_words / unique_words
    print(f"Repetition ratio for {gender}: {repetition_ratio:.2f}")

    return sentimental_word_counter

def analyze_negative_words_by_gender(data, gender):
    negative_word_counter = Counter()

    for review in data:
        if review['gender'] == gender:
            words = re.findall(r'\b\w+\b', review['review_text'].lower())
            filtered_words = [word for word in words if word not in stop_words and word not in exclude_words]
            
            for word in filtered_words:
                word_sentiment = TextBlob(word).sentiment.polarity
                if word_sentiment < 0:  # Consider only negative sentiment words
                    negative_word_counter[word] += 1

    return negative_word_counter

if __name__ == "__main__":
    data = []
    with open('/Users/giamihuynh/Downloads/TxtMin-Project-SA-1/Processed_Data/Final_Gendered_2.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    # Analyze sentimental words for each gender
    genders = ['male', 'female']
    sentimental_word_counters = {}
    for gender in genders:
        print(f"\n{gender} reviews:")
        sentimental_word_counters[gender] = analyze_sentimental_words_by_gender(data, gender)

    male_common_words = sentimental_word_counters['male'].most_common(20)
    female_common_words = sentimental_word_counters['female'].most_common(20)

    male_df = pd.DataFrame(male_common_words, columns=['word', 'count'])
    female_df = pd.DataFrame(female_common_words, columns=['word', 'count'])

    # Plotting
#    plt.figure(figsize=(14, 7))

    # Male reviews
#    plt.subplot(1, 2, 1)
#    sns.barplot(x='count', y='word', data=male_df, palette='Blues_d')
#    plt.title('Most Common Sentimental Words in Male Reviews')
#    plt.xlabel('Count')
#    plt.ylabel('Word')

    # Female reviews
#    plt.subplot(1, 2, 2)
#    sns.barplot(x='count', y='word', data=female_df, palette='Purples_d')
#    plt.title('Most Common Sentimental Words in Female Reviews')
#    plt.xlabel('Count')
#    plt.ylabel('Word')

#    plt.tight_layout()

# Analyze negative words for each gender
    negative_word_counters = {}
    for gender in genders:
        negative_word_counters[gender] = analyze_negative_words_by_gender(data, gender)

    male_negative_words = negative_word_counters['male'].most_common(20)
    female_negative_words = negative_word_counters['female'].most_common(20)

    male_df = pd.DataFrame(male_negative_words, columns=['word', 'count'])
    female_df = pd.DataFrame(female_negative_words, columns=['word', 'count'])

    # Plotting
#    plt.figure(figsize=(14, 7))

    # Male reviews
 #   plt.subplot(1, 2, 1)
 #   sns.barplot(x='count', y='word', data=male_df, palette='Blues_d')
 #   plt.title('Most Common Negative Words in Male Reviews')
 #   plt.xlabel('Count')
 #   plt.ylabel('Word')

    # Female reviews
 #   plt.subplot(1, 2, 2)
 #   sns.barplot(x='count', y='word', data=female_df, palette='Purples_d')
 #   plt.title('Most Common Negative Words in Female Reviews')
 #   plt.xlabel('Count')
 #   plt.ylabel('Word')

    plt.tight_layout()


# Word Count Analysis
# aiding source: https://www.w3schools.com/python/ref_string_maketrans.asp

w_c = []
trans1 = str.maketrans("", "", string.punctuation)

for rev in reviews_df["review_text"]:
    w = rev.translate(trans1)
    rev_l = len(w)
    w_c.append(rev_l)

reviews_df["review_w_c"] = w_c

# Calculate review lengths in words
reviews_df['review_length'] = reviews_df['review_text'].apply(lambda x: len(x.split()))

male_reviews = reviews_df[reviews_df['gender'] == 'male']
female_reviews = reviews_df[reviews_df['gender'] == 'female']

# Review lengths for male reviews
plt.figure(figsize=(12, 6))
sns.histplot(male_reviews['review_length'], bins=range(0, 201), kde=False)
plt.title('Review Length Distribution for Male Reviews')
plt.xlabel('Review Length (words)')
plt.ylabel('Frequency')
plt.xlim(0, 200)
plt.grid(True)

# Review lengths for female reviews
plt.figure(figsize=(12, 6))
sns.histplot(female_reviews['review_length'], bins=range(0, 201), kde=False)
plt.title('Review Length Distribution for Female Reviews')
plt.xlabel('Review Length (words)')
plt.ylabel('Frequency')
plt.xlim(0, 200)
plt.grid(True)

# Plotting sentiment scores for male reviews
plt.figure(figsize=(12, 6))
sns.histplot(male_reviews['sentiment'], bins=50, kde=True, stat='density')
plt.title('Sentiment Score Distribution for Male Reviews')
plt.xlabel('Sentiment Score')
plt.ylabel('Relative Frequency')
plt.grid(True)

# Plotting sentiment scores for female reviews
plt.figure(figsize=(12, 6))
sns.histplot(female_reviews['sentiment'], bins=50, kde=True, stat='density')
plt.title('Sentiment Score Distribution for Female Reviews')
plt.xlabel('Sentiment Score')
plt.ylabel('Relative Frequency')
plt.grid(True)

helpful_votes_by_gender_sentiment = reviews_df.groupby(['gender', 'sentiment_label'])['helpful_count'].sum().unstack(fill_value=0)

print(helpful_votes_by_gender_sentiment)

# Calculate accuracy
manually_categorized_data = pd.read_csv("/Users/giamihuynh/Downloads/TxtMin-Project-SA-1/Processed_Data/manual_categorized_reviews2.csv")
sampled_review_data = reviews_df.sample(n=100, random_state=42)

manual_sentiment = manually_categorized_data["category"]
predicted_sentiment = sampled_review_data["sentiment_label"]

accuracy = accuracy_score(manual_sentiment, predicted_sentiment)
print("Accuracy:", accuracy)
sampled_review_data['predicted_sentiment'] = predicted_sentiment # add predicted sentiment

# sampled_review_data.to_csv('sampled_review_data_with_predictions.csv', index=False) 