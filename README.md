# Text Mining Project - Sentiment Analysis
## Group Members: Maria, Giami, and Hannah 

## Romeo vs. Juliet: Investigating Gender-Based Linguistic Variations in Online Reviews: A Sentiment Analysis Approach

### Abstract 
This project aims to investigate how language and sentiment vary between online reviews written by men and women. Understanding the role of gender in review language is essential for businesses to tailor their marketing strategies effectively and efficiently. We plan to use a dataset of online reviews sourced from various platforms, and look at how differently language is used between genders. By using processing techniques, we will extract sentiments and linguistic features to examine differences between male and female-authored reviews. We also plan to use libraries that are available for gender identification to determine the gender of the user(name). Analyzing patterns will help reveal insights into gender-specific linguistic tendencies, and give deeper insights into underlying preferences driving review composition. Ultimately, this research aims to contribute to a deeper understanding of gender dynamics in online discourse and offer actionable implications for businesses looking to engage with diverse consumer segments. 

### Research Questions 
- MQ: Which gender is likely to give a positive, neutral, or negative review?
- Which gender is more likely to be critical in their review? 
  - Check how many words and how often the words are repeated.
- Which gender has the longest review?

### Datasets 
Contain name/profile:
- iPhone Reviews from Amazon (https://www.kaggle.com/datasets/thedevastator/apple-iphone-11-reviews-from-amazon-com): Reviews of iPhone XR contains around 5010 reviews of the product. The data contains many extra fields which we are not interested in such as the total_comments, url, reviewed_at (date) and others. 
- iPhone 14 Customer Reviews Dataset (https://www.kaggle.com/datasets/shahriarkabir/iphone-14-customer-reviews-dataset-ratings): Around 1,023 review where the customer location will not be useful to analyze gender behavior.
- Amazon One Plus Reviews (https://data.world/opensnippets/amazon-mobile-phones-reviews) - However will likely not be used due that it doesn't seem to contain apple products in contrary to its description.

Doesn't contain name of reviewer:
- Amazon Mobile Phone Reviews (https://data.world/promptcloud/amazon-mobile-phone-reviews) - Around 1279 reviews of specifically iPhone products so it would have to be filtered out and saved into a csv file.

- Process: The dataset as one can see are from different phones however for the sake of the analysis we will consider them the same since they are the made from the same brand. First off we would have to filter out any irrelevant characters such as numbers or uncommon punctuation like : and ;. Filtering these irrelevant punctuation will hopefully allow the more significant punctuation such as ! for sentimental analysis. One may consider making the review all the same case however capitalizing an entire words like AMAZING! creates more of a positive sentiment than Amazing! so we will keep fully capitalized words (if any). Some people rather than using words may use emojis to showcase their opinion/emotion. This means we would have to figure out a way to identify an emoji and evaluate it whether it would be perceived as good or bad. A possible idea would be to use identify the emoji with its unicode. Since all the data we have been able to collect is in english there is no need to translate or do language processing. In terms of enriching the data we can also investigate what aspects of the phone do reviewers tend to focus on like whether it is the camera quality or the size of the screen and see if there is any difference between the genders. One of the research questions concerns the length of the review of each gender so we would find the length of the review before preprocessing it.


  
### Planned Milestones 
- update 1: May 8
  - Pre-processing the data - Maria
- update 2: May 20 
  - Sentiment Analysis - Giami
- Interpreting the Results - Hannah 
- Plot the Results - Hannah 
- Presentation (May 28) - Everyone 
  - Background Information 
  - Key Findings 
  - Critical appraisal of project and results 
  - Connection of the project to course content  
- Paper (due May 31st)
  - Intro - Hannah
  - Methods - Maria and Giami
  - Results - Hannah
  - Discussion - Maria
  - Conclusion/ Suggestion for future - Giami 

### Questions of Each Update
Update 0:
- We want to use a gender guesser library to guess the gender of the reviewer since most datasets do not provide that info. However, we are unsure of how it would approach names that could be used for males and females (ex. Jamie). What would you advise? [https://pypi.org/project/gender-guesser/]
  
### Documentation
