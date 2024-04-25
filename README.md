# Text Mining Project - Sentiment Analysis
## Group Members: Maria, Giami, and Hannah 

## Romeo vs. Juliet: Investigating Gender-Based Linguistic Variations in Online Reviews: A Sentiment Analysis Approach

### Abstract 

### Research Questions 
- MQ: Which gender is likely to give a positive, neutral, or negative review?
- Which gender is more likely to be critical in their review? 
  - Check how many words and how often the words are repeated.
- Which gender has the longest review?

### Datasets 
- iPhone Reviews from Amazon (https://www.kaggle.com/datasets/thedevastator/apple-iphone-11-reviews-from-amazon-com): Reviews of iPhone XR contains around 5010 reviews of the product. The data contains many extra fields which we are not interested in such as the total_comments, url, reviewed_at (date) and others. 

- iPhone 14 Customer Reviews Dataset (https://www.kaggle.com/datasets/shahriarkabir/iphone-14-customer-reviews-dataset-ratings): Around 1,023 review where the customer location will not be useful to analyze gender behavior.

- Process: First off we would have to filter out any irrelavant characters such as number or uncommon punctuation like : and ;. Filtering these irrelevant punctuation will hopefully allow the more significant puntuation such as ! for sentimental analysis. One may conside making the review all the same case however capitalizing an entire words like AMAZING! creates more of a positive sentiment than Amazing!. Some people rather than using words may use emojis to showcase their opinion/emotion. This means we would have to figure out a way to identify an emoji and evaluate it whether it would be perceived as good or bad. A possible idea would be to use identify the emoji with its unicode. Since all the data we have been able to collect is in englsih there is no need to translate or do language processing.

  
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
- We want to use a gender guesser library to guess the gender of the reviewer since most datasets do not provide that info. However, we are unsure of how it would approach names that could be used for males and females (ex. Jamie). What would you advise?
  
### Documentation
