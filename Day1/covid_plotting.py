#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import calendar
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_19-covid-Confirmed.csv&filename=time_series_2019-ncov-Confirmed.csv')


# In[3]:


df = df.drop(['Province/State', 'Lat', 'Long'], axis=1)
df = df.sort_values(by = 'Country/Region')
df = df.groupby(['Country/Region']).sum()


# In[4]:


df = df.loc[:, df.isin(['0']).mean() <= .7]


# In[5]:


def plot_top_countries_for_date(countryCount, date):
    filteredDf = df.nlargest(countryCount, [date])
    datePlot = filteredDf.plot(kind='pie', y=date)
    datePlot.get_figure().savefig('top_countries_for_date.png', dpi=300)


# In[6]:


plot_top_countries_for_date(10, '3/22/20')


# In[7]:


def plot_country_by_date(country):
    countryPlot = df.loc[country, : ].plot(kind='bar')
    countryPlot.get_figure().savefig('dates_for_country.png', dpi=300)


# In[8]:


plot_country_by_date('India')


# In[9]:


continentDf = pd.read_csv('https://raw.githubusercontent.com/dbouquin/IS_608/master/NanosatDB_munging/Countries-Continents.csv')


# In[10]:


mergedContinentDf = pd.merge(left=df, right=continentDf, left_on='Country/Region', right_on='Country')
mergedContinentDf = mergedContinentDf.groupby(['Continent']).sum()


# In[11]:


def plot_continents(date):
    continentPlot = mergedContinentDf.plot(kind='pie', y=date)
    continentPlot.get_figure().savefig('continent_date_plot.png', dpi=300)


# In[12]:


plot_continents('3/22/20')

