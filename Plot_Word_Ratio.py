import matplotlib.pyplot as plt
import numpy as np

# Male Reviews 
x = np.array(["Unique Words", "Repeated Words"])
y = np.array([1926, 12067])

font1 = {'family':'serif','color':'black','size':20}

plt.title("Male Repition Ratio = 3.16", fontdict = font1)
plt.bar(x,y)
plt.show()

plt.savefig('Male_Word_Ratio.png')

# Female Reviews 
x2 = np.array(["Unique Words", "Repeated Words"])
y2 = np.array([1475, 7407])

plt.title("Female Repition Ratio = 2.49", fontdict = font1)
plt.bar(x2, y2)
plt.show()

plt.savefig('Female_Word_Ratio.png')
