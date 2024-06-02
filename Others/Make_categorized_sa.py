import pandas as pd
import random

file_path = "/Users/giamihuynh/Downloads/TxtMin-Project-SA-1/Processed_Data/Final_Gendered_2.csv"
reviews_df = pd.read_csv(file_path)

random_reviews = reviews_df.sample(n=100, random_state=42)

# Manually categorize the reviews
categorized_reviews = []
for idx, review_text in enumerate(random_reviews['review_text']):
    print(f"Review {idx + 1}:")
    print(review_text)
    while True:
        category = input("Enter category (negative, neutral, positive): ").strip().lower()
        if category in ['negative', 'neutral', 'positive']:
            break
        else:
            print("Invalid category. Please enter 'negative', 'neutral', or 'positive'.")
    categorized_reviews.append({'review_text': review_text, 'category': category})

# Save to a new CSV file
output_file_path = "/Users/giamihuynh/Downloads/TxtMin-Project-SA-1/Processed_Data/manual_categorized_reviews2.csv"
categorized_reviews_df = pd.DataFrame(categorized_reviews)
categorized_reviews_df.to_csv(output_file_path, index=False)

print("Manually categorized reviews saved to:", output_file_path)