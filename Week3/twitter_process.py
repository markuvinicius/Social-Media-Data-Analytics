import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

twitter_data = pd.read_csv('../Week2/result.csv')

plt.figure()
#histograma da quantidade de friends do twitter
hist1,edges1 = np.histogram(twitter_data.friends)
plt.bar(edges1[:-1],hist1,width=edges1[1:]-edges1[:-1])

#dispersão da quantidade de seguidores pela quantidade de retweets
plt.figure()
plt.scatter(twitter_data.followers,twitter_data.friends)

x = twitter_data.friends
y = twitter_data.followers

x = sm.add_constant(x)

lr_model = sm.OLS(y,x).fit()



x_prime = np.linspace(x.friends.min(),x.friends.max(),100)
x_prime = sm.add_constant(x_prime)

y_hat = lr_model.predict(x_prime)

plt.scatter(x.friends,y)
plt.xlabel("Friends")
plt.ylabel("Followers")
plt.plot(x_prime[:,1],y_hat)

plt.savefig('Friends x Followers.jpg')