import pandas as pd
from textblob import TextBlob
import csv
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import seaborn as sns

# Download the stop words list
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

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

average_rating = reviews_df.groupby('gender')['review_rating'].mean()
average_sentiment_scores = reviews_df.groupby('gender')['sentiment'].mean()

# List of words to exclude (common words)
exclude_words = {'good'}
# 'good', 'awesome', 'best', 'great', 'nice', 'excellent', 'amazing'

def analyze_sentimental_words_by_gender(data, gender):
    word_counter = Counter()
    sentimental_word_counter = Counter()

    for review in data:
        # Check if the review belongs to the specified gender
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
        # Check if the review belongs to the specified gender
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

    # Prepare data for plotting
    male_common_words = sentimental_word_counters['male'].most_common(20)
    female_common_words = sentimental_word_counters['female'].most_common(20)

    male_df = pd.DataFrame(male_common_words, columns=['word', 'count'])
    female_df = pd.DataFrame(female_common_words, columns=['word', 'count'])

    # Plotting
    plt.figure(figsize=(14, 7))

    # Male reviews
    plt.subplot(1, 2, 1)
    sns.barplot(x='count', y='word', data=male_df, palette='Blues_d')
    plt.title('Most Common Sentimental Words in Male Reviews')
    plt.xlabel('Count')
    plt.ylabel('Word')

    # Female reviews
    plt.subplot(1, 2, 2)
    sns.barplot(x='count', y='word', data=female_df, palette='Purples_d')
    plt.title('Most Common Sentimental Words in Female Reviews')
    plt.xlabel('Count')
    plt.ylabel('Word')

    plt.tight_layout()

# Analyze negative words for each gender
    negative_word_counters = {}
    for gender in genders:
        negative_word_counters[gender] = analyze_negative_words_by_gender(data, gender)

    # Prepare data for plotting
    male_negative_words = negative_word_counters['male'].most_common(20)
    female_negative_words = negative_word_counters['female'].most_common(20)

    male_df = pd.DataFrame(male_negative_words, columns=['word', 'count'])
    female_df = pd.DataFrame(female_negative_words, columns=['word', 'count'])

    # Plotting
    plt.figure(figsize=(14, 7))

    # Male reviews
    plt.subplot(1, 2, 1)
    sns.barplot(x='count', y='word', data=male_df, palette='Blues_d')
    plt.title('Most Common Negative Words in Male Reviews')
    plt.xlabel('Count')
    plt.ylabel('Word')

    # Female reviews
    plt.subplot(1, 2, 2)
    sns.barplot(x='count', y='word', data=female_df, palette='Purples_d')
    plt.title('Most Common Negative Words in Female Reviews')
    plt.xlabel('Count')
    plt.ylabel('Word')

    plt.tight_layout()
    plt.show()