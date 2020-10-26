#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:16:10 2020

@author: reneecothern

File to combine csv files into one
"""

import pandas as pd
import os


'''
Which columns do I want?

Keep** Country, Happiness.Rank, Happiness.score, GDP.per.capita, 
Social.Support (Family), 
Life.Expectancy, Freedom, Trust.Goverment.Corruption, Generosity,
Year
10 columns

Old 2018 columns: Index([u'Overall rank', u'Country or region', u'Score', u'GDP per capita',
       u'Social support', u'Healthy life expectancy',
       u'Freedom to make life choices', u'Generosity',
       u'Perceptions of corruption', u'Year'],
      dtype='object') (156, 10)

Remove** Lower Confidence Interval, Upper Confidence Interval, Region, 
Dystopia Residual

'''

whdata2016 = pd.read_csv("./world-happiness/2016.csv")
whdata2016["Year"]= 2016
whdata2016.drop(columns="Lower Confidence Interval", inplace=True)
whdata2016.drop(columns="Upper Confidence Interval", inplace=True)
whdata2016.drop(columns="Region", inplace=True)
whdata2016.drop(columns="Dystopia Residual", inplace=True)

whdata2016.rename(columns={'Happiness Rank': 'Happiness.Rank', \
                           'Happiness Score': 'Happiness.Score', \
                           'Economy (GDP per Capita)': 'GDP.per.capita', \
                           'Health (Life Expectancy)': 'Life.Expectancy', \
                           'Trust (Government Corruption)': 'Trust.Goverment.Corruption',
                           'Family': 'Social.Support'}, inplace=True)
print "New columns:", whdata2016.columns, whdata2016.shape

    
whdata2017 = pd.read_csv("./world-happiness/2017.csv")
whdata2017["Year"]= 2017

whdata2017.drop(columns="Whisker.high", inplace=True)
whdata2017.drop(columns="Whisker.low", inplace=True)
whdata2017.drop(columns="Dystopia.Residual", inplace=True)

whdata2017.rename(columns={'Economy..GDP.per.Capita.': 'GDP.per.capita', \
                           'Health..Life.Expectancy.': 'Life.Expectancy', \
                           'Trust..Government.Corruption.': 'Trust.Goverment.Corruption',
                           'Family': 'Social.Support'}, inplace=True)
print
print "New columns:", whdata2017.columns, whdata2017.shape

  
whdata2018 = pd.read_csv("./world-happiness/2018.csv")
whdata2018["Year"]= 2018

whdata2018.rename(columns={'Overall rank': 'Happiness.Rank', \
                           'Country or region': 'Country', \
                           'Score': 'Happiness.Score', \
                           'GDP per capita': 'GDP.per.capita', \
                           'Social support': 'Social.Support', \
                           'Healthy life expectancy': 'Life.Expectancy',
                           'Freedom to make life choices': 'Freedom', \
                           'Perceptions of corruption': 'Trust.Goverment.Corruption' \
                               }, inplace=True)
print
print "New columns:", whdata2018.columns, whdata2018.shape


   
whdata2019 = pd.read_csv("./world-happiness/2019.csv")
whdata2019["Year"]= 2019

whdata2019.rename(columns={'Overall rank': 'Happiness.Rank', \
                           'Country or region': 'Country', \
                           'Score': 'Happiness.Score', \
                           'GDP per capita': 'GDP.per.capita', \
                           'Social support': 'Social.Support', \
                           'Healthy life expectancy': 'Life.Expectancy',
                           'Freedom to make life choices': 'Freedom', \
                           'Perceptions of corruption': 'Trust.Goverment.Corruption' \
                               }, inplace=True)
print
print "New columns:", whdata2019.columns, whdata2019.shape


whData = pd.concat([whdata2016,whdata2017,whdata2018,whdata2019])

whData.to_csv('wh_2016to2019.csv', index=False)

