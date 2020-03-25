#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Package imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Load datasets

train_df = pd.read_csv('./train.csv')
test_df = pd.read_csv('./test.csv')


# In[3]:


train_df.info()


# In[4]:


train_df = train_df.drop(['PassengerId', 'Name', 'Ticket', 'Fare', 'Cabin'], axis = 1)


# In[5]:


train_df


# In[6]:


# Plotting survival by all factors

factorSurvival = sns.heatmap(train_df.corr(), annot=True, fmt=".2f")
factorSurvival.set_title('Survival by all Factors')
plt.show()


# In[7]:


# Plotting survival by gender

genderSurvival = sns.barplot(x = 'Sex', y = 'Survived', hue = 'Pclass', data = train_df, order = ['male', 'female'], ci = 'sd')
genderSurvival.set_title('Survival by Gender')
plt.show()


# In[8]:


# Expand values

train_df['Pclass'].replace({
    1: 'Upper',
    2: 'Middle',
    3: 'Lower'
}, inplace=True)

train_df['Survived'].replace({
    1: 'Yes',
    0: 'No'
}, inplace=True)


# In[20]:


# Plotting the survival by age and socio-economic class

genderClassSurvival = sns.FacetGrid(train_df, row='Survived', col='Pclass')
genderClassSurvival.map(sns.distplot, "Age")
plt.subplots_adjust(top=0.9)
plt.suptitle('Survival by Age and Socio Economic Class')
plt.show()


# In[ ]:




