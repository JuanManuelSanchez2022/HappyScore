import pandas as pd

data = pd.read_csv('happyscore_income.csv')

country = data['country']
avgInc = data['avg_income']
incIneq = data['income_inequality']
happy = data['happyScore']


happy.max()

import matplotlib.pyplot as plt
plt.xlabel('Average Income')
plt.ylabel('Income Inequality')
plt.scatter(avgInc, incIneq, s = happy*100, alpha = 0.25)

from sklearn.cluster import KMeans
import numpy as np
avgInc_inqIneq = np.column_stack((avgInc, incIneq))
km_res = KMeans(n_clusters=2).fit(avgInc_inqIneq)
clusters = km_res.cluster_centers_
plt.scatter(avgInc, incIneq)
plt.xlabel('Average Income')
plt.ylabel('Income Inequality')
plt.scatter(clusters[:,0], clusters[:,1], s=1000, alpha = 0.5)

km_res.cluster_centers_

data.sort_values('avg_income', inplace = True)
happiest = data[data['income_inequality']>=55]
plt.scatter(happiest['avg_income'], happiest['income_inequality'],s = happy*100, alpha = 0.25)
for k, row in happiest.iterrows():
    plt.text(row['avg_income'],
            row['income_inequality'],
            row['country'])
    
    avgInc_inqIneq = np.column_stack((avgInc, incIneq))
    km_res = KMeans(n_clusters=2).fit(avgInc_inqIneq)
    clusters = km_res.cluster_centers_
    plt.scatter(clusters[:,0], clusters[:,1], s=1000, alpha = 0.25)
    
    plt.xlabel('Average Income')
    plt.ylabel('Income Inequality')
    
    #print(row['country'])
    
