#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 22:44:08 2017

@author: Marku
"""

import matplotlib.pyplot as plt
import pandas as pd

twitter_data = pd.read_csv('/Users/Marku/Documents/data_center/WorkSpace/Social-Media-Data-Analytics/Week4/results_trump.csv')

print(twitter_data.corr())

twitter_data_subjective = twitter_data[twitter_data['subjectivity']>0.5]

print(twitter_data_subjective.corr())

plt.scatter(twitter_data.retwc,twitter_data.subjectivity)