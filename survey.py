#%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('E:/gnuplot/Distance learning survey.csv')
df.head()

que1 = df['How do you feel overall about distance education?'].value_counts()
que2 = df[' Do you have access to a device for learning online?'].value_counts()
que3 = df['What device do you use for distance learning?'].value_counts()
que4 = df['How much time do you spend each day on an average on distance education?'].value_counts()
que5 = df['How effective has remote learning been for you?'].value_counts()
que6 = df['How helpful your [School or University] has been in offering you the resources to learn from home?'].value_counts()
que7 = df[' Do you enjoy learning remotely?'].value_counts()
que8 = df['How helpful are your teachers while studying online?'].value_counts()

fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(que1,autopct = '%.2f%%',radius=1.2,explode=[0,0,0.2,0])
ax.legend(wedges, ['Excellent','Good','Average','Poor'],loc ="center left",bbox_to_anchor =(1, 0, 0.5, 1))
ax.set_title("How do you feel overall about distance education?",fontweight = 'bold',fontsize = 20)



fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(que2,autopct = '%.2f%%',radius=1.2,explode=[0,0.2])
ax.legend(wedges, ['Yes','Yes,but it doesn’t work well','No,I use others device'],loc ="center left",bbox_to_anchor =(1, 0, 0.5, 1))
ax.set_title("Do you have access to a device for learning online?",fontweight = 'bold',fontsize = 20)



fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(que3,autopct = '%.2f%%',radius=1.2,explode=[0,0,0.2,0])
ax.legend(wedges, ['Smartphone','Laptop','Desktop','Tablet'],loc ="center left",bbox_to_anchor =(1, 0, 0.5, 1))
ax.set_title("What device do you use for distance learning?",fontweight = 'bold',fontsize = 20)


fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(que4,autopct = '%.2f%%',radius=1.2,explode=[0,0,0.2,0])
ax.legend(wedges, ['1-3 hours','3-5 hours','5-7 hours','7+ hours'],loc ="center left",bbox_to_anchor =(1, 0, 0.5, 1))
ax.set_title("How much time do you spend each day on an average on distance education?",fontweight = 'bold',fontsize = 20)



fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(que5,autopct = '%.2f%%',radius=1.2,explode=[0,0,0.2,0])
ax.legend(wedges, ['Extremely effective','Moderately effective','Slightly effective','Not at all effective'],loc ="center left",bbox_to_anchor =(1, 0, 0.5, 1))
ax.set_title("How effective has remote learning been for you?",fontweight = 'bold',fontsize = 20)


fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(que6,autopct = '%.2f%%',radius=1.2,explode=[0,0,0.2,0])
ax.legend(wedges, ['Extremely helpful','Moderately helpful','Slightly helpful','Not at all helpful'],loc ="center left",bbox_to_anchor =(1, 0, 0.5, 1))
ax.set_title("How helpful your [School or University] has been in offering you the resources to learn from home?",fontweight = 'bold',fontsize = 20)


fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(que7,autopct = '%.2f%%',radius=1.2,explode=[0,0,0.2,0])
ax.legend(wedges, ['Yes, absolutely','Yes, but I would like to change a few things','No, there are quite a few challenges','No, not at all'],loc ="center left",bbox_to_anchor =(1, 0, 0.5, 1))
ax.set_title("Do you enjoy learning remotely?",fontweight = 'bold',fontsize = 20)


fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(que8,autopct = '%.2f%%',radius=1.2,explode=[0,0,0,0.2])
ax.legend(wedges, ['Extremely helpful','Moderately helpful','Slightly helpful','Not at all helpful'],loc ="center left",bbox_to_anchor =(1, 0, 0.5, 1))
ax.set_title("How helpful are your teachers while studying online?",fontweight = 'bold',fontsize = 20)

plt.show()



