#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df1 = pd.read_csv('steps.csv', sep=";")

df1.head(10)


# In[3]:


df2 = pd.read_csv('survey.csv')
df2.head()


# In[4]:


df2['weight'].describe()


# In[6]:


df2['weight'].value_counts()


# In[11]:


df2['age'].describe()


# In[6]:


df2['weight'].sort_values()


# ## Here I removed the impossible values. 

# In[5]:


df2 = df2[df2.weight !=700]


# In[6]:


df2['weight'].sort_values()


# In[7]:


df2 = df2[df2.weight !=20]


# In[8]:


df2 = df2[df2.weight !=6.0]


# In[9]:


df2['weight'].sort_values()


# In[10]:


df2['weight'].dropna()


# ## Here I combined the two dataframes with the pd.merge function which merges the two df's based on the user id column.

# In[11]:


df = pd.merge(df1, df2)
df.head()


# ## Here I created the variable which indicates the mean steps per participant named: steps_mean

# In[12]:


df.columns.get_loc('13-5-2014')


# In[13]:


df.columns.get_loc('20-6-2013')


# In[14]:


df['steps_mean'] = df.loc[:,"20-6-2013":"13-5-2014"].mean(axis=1, skipna = True).round(1)
df.head()


# ### Here I performed an analysis on the variable steps_mean. 

#  I first looked at the measures for this variable. As there where some outliers and impossible values, I decided to remove these for the sake of sufficient visualization. I assumed that a mean of 30000 would be a realistic max value. 

# In[15]:


df['steps_mean'].describe()


# In[17]:


df['steps_mean'].sort_values()


# In[18]:


df = df[df.steps_mean !=201722.600000]


# In[19]:


df['steps_mean'].sort_values()


# In[20]:


df = df[df.steps_mean !=58491.1]


# In[22]:


df['steps_mean'].sort_values()


# In[23]:


df = df[df.steps_mean !=43912.3]


# In[24]:


df['steps_mean'].sort_values()


# In[25]:


df = df[df.steps_mean !=30373.8]


# In[26]:


df['steps_mean'].sort_values()


# In[27]:


df = df[df.steps_mean !=4.0]


# In[28]:



df['steps_mean'].name = 'mean steps per participant'
steps_mean = df['steps_mean'].dropna() 
sns.displot(steps_mean, kde=False) 
plt.title('Mean steps per participant')
plt.show()


# 
# Some things to note about this distribution:
# 
# It has several peaks on the left hand side of the graph. 
# It has a 'tail' on the right which means that the distribution is right-skewed. 
# When the distribution is right-skewed, the mean is higher than the median. 
# 

# ### The relation of mean steps per participant with a gender

# In[29]:


sns.catplot(x="gender", y="steps_mean", data=df)


# This scatter plot provides us with information on which gender has the highest mean steps per participant. We can see that there are more female plots which reach higher values compared to the male plots.

# ### The relation between two categorical variables

# In[32]:


sns.catplot(y="education", hue="gender", kind="count",
            palette="pastel", edgecolor=".6",
            data=df)


# This bar plot visualizes the relationship between education level and gender. The graph tells us that the distribution between male and female within education level 1 is quite even. There seem to be more males with education level 2. Education level 3 and 4 are both distributed quite evenly. More or less double the amount of males appear to have education level 5 which could be defined as a significant difference. 
# 

# In[33]:


pd.crosstab(df["education"], df["gender"])


# This cross table shows the level of education for both males and females. It is shown in absolute numbers which makes it hard to analyze. Therefore, I have created the following crosstab which contains proportional data. 

# In[38]:


pd.crosstab(df["education"],df["gender"], normalize="columns")

