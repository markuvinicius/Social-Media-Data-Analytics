#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 22:44:08 2017

@author: Marku
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.api as sm


twitter_data = pd.read_csv('/Users/Marku/Documents/data_center/WorkSpace/Social-Media-Data-Analytics/Week4/results_trump.csv')

print(twitter_data.head())
print(twitter_data.corr())

#polaridade versus subjetividade
plt.figure()
plt.scatter(twitter_data.polarity,twitter_data.subjectivity,marker='x',c='blue')
plt.xlabel("Polaridade")
plt.ylabel("Subjetividade")

#regressão linear para as variáveis polaridade e subjetividade
x1 = twitter_data.polarity
y1  = twitter_data.subjectivity
x1 = sm.add_constant(x1)
lr_model_1 = sm.OLS(y1,x1).fit()

#predição baseada na regressão linear das variáveis
x_prime = np.linspace(x1.polarity.min() , x1.polarity.max() , 100 )
x_prime = sm.add_constant(x_prime)
y_hat = lr_model_1.predict(x_prime)
#desenha linha de tendência predita
plt.plot(x_prime[:,1],y_hat,c='red')


#retweets versus polaridade
plt.figure()
plt.scatter(twitter_data.polarity,twitter_data.retwc,marker='o',c='red')
plt.xlabel("Polarity")
plt.ylabel("Retweet Count")

#regressão linear para as variáveis retweets e polaridade
x2  = twitter_data.polarity
y2  = twitter_data.retwc
x2  = sm.add_constant(x2)
lr_model_2 = sm.OLS(y2,x2).fit()

#predição baseada na regressão linear das variáveis
x_prime_1 = np.linspace(x2.polarity.min() , x2.polarity.max() , 100 )
x_prime_1 = sm.add_constant(x_prime_1)
y_hat_1 = lr_model_2.predict(x_prime_1)
#desenha linha de tendência predita
plt.plot(x_prime_1[:,1],y_hat_1,c='blue')

plt.savefig("/Users/Marku/Documents/data_center/WorkSpace/Social-Media-Data-Analytics/Week4/polarityxretwc.png")

