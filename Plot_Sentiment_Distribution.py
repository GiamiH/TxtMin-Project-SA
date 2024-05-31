import matplotlib.pyplot as plt
import numpy as np

# Female Sentiment Analysis Distribution
y = np.array([69, 117, 507]) #693
mylabels = ["Negative = 0.1%", "Neutral = 0.17%", "Positive = 0.73%"]

font1 = {'family':'serif','color':'black','size':20}

plt.title("Female Sentiment Distribution", fontdict = font1)
plt.pie(y, labels = mylabels)
plt.show

#plt.savefig('Female_Distribution.png')


# Male Sentiment Analysis Distribution 
y2 = np.array([68, 162, 774]) #1004
mylabels2 = ["Negative = 0.07%", "Neutral = 0.16%", "Positive = 0.77%"]

plt.title("Male Sentiment Distribution", fontdict = font1)
plt.pie(y2, labels = mylabels2)
plt.show

#plt.savefig('Male_Distribution.png')
