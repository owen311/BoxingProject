#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


# In[2]:


#Functions

def file_to_df(file):
    df = pd.read_csv(file, sep = '\t')
    df = df.drop(columns = ['Unnamed: 0.1', 'Unnamed: 0'])
    return df
    
def graph_hits(df, w = [0,15], h = 20, p = 20, t = 2):
    peaks, info = find_peaks(df['total'],
        width = w, height = h, prominence = p, threshold = t)
    plt.plot(df['total'])
    plt.plot(peaks, df['total'][peaks], 'x')
    plt.show()
    
def stats(df, w = [0,15], h = 20, p = 20, t = 2):
    peaks, info = find_peaks(df['total'],
        width = [0,15], height = 20, prominence = 20, threshold = 2)

    num_hits = len(peaks)
    max_hit = np.max(info['peak_heights'])
    min_hit = np.min(info['peak_heights'])
    mean_hit = np.mean(info['peak_heights'])
    std_hit = np.std(info['peak_heights'])
    
    y = info['peak_heights']
    x = np.ones(num_hits)
    plt.boxplot(info['peak_heights'])
    plt.plot(x, y, 'r.', alpha=0.8)
    '''
         Q1-1.5IQR   Q1   median  Q3   Q3+1.5IQR
                      |-----:-----|
      o      |--------|     :     |--------|    o  o
                      |-----:-----|
    flier             <----------->            fliers
                           IQR
    '''  
    plt.show()

    print('num hits: {}'.format(num_hits))
    print('max hit: {}'.format(max_hit))
    print('min hit: {}'.format(min_hit))
    print('mean hit: {}'.format(mean_hit))
    print('standard deviation: {}'.format(std_hit))


# In[3]:


df = file_to_df(file = 'boxing_data4000v1')
graph_hits(df)
stats(df)


# In[ ]:




