"""

Quick data parser for ECG vs PPG analysis and algo benchmarking

Created: 15/09/2019
Author: MBRS

"""


import pandas as pd
import os
import heartpy as hp
import numpy as np

import matplotlib.pyplot as plt
from datetime import datetime



"""

1. READ  & PARSE DATA

"""

## ECG
ECG_data_des = pd.read_csv('readings/Stef1_ECG.txt',nrows=10)
ECG_data = pd.read_csv('readings/Stef1_ECG.txt',sep="\t",skiprows=11)
ECG_data = ECG_data[0:-1] #remove last row with 'end of exported RAW data' notification
ECG_data.loc[:,'TIME'] =  pd.to_datetime(ECG_data['TIME'], format='%H:%M:%S') #converting col todatetime
ECG_starttime = datetime.strptime(ECG_data_des.index[3].split("\t")[1], '%H:%M:%S')

ECG_data.loc[3,'TIME']+datetime.timestamp(ECG_starttime)
df_data = data_cleaner(df_data)

##PPG
PPG_data = pd.read_csv('readings/Stef1_PPG.csv')
PPG_data.columns = ['Source','idx','ppg_1','ppg_2','timestamp']
PPG_data_loaded = PPG_data['ppg_2'].str.replace("'"," ").astype(int)



_sampleRate = 800
_subsetLen = 20 # in seconds
_subsetStart = 300000

data_loaded_subset = PPG_data_loaded[_subsetStart:_subsetStart+(_subsetLen*_sampleRate)]

plt.figure(figsize=(22,6))
plt.plot(data_loaded_subset)
plt.show()

bandpass_low = 1
bandpass_high = 3
    
filtered_ppg = hp.filter_signal(data_loaded_subset.fillna(0).astype('int32'),
                                    cutoff = [bandpass_low, bandpass_high],
                                    filtertype = 'bandpass',
                                    sample_rate = _sampleRate,
                                    order = 3,
                                    return_top = False)


plt.figure(figsize=(22,6))
plt.plot(filtered_ppg)
plt.show()

wd, m = hp.process(filtered_ppg, sample_rate=_sampleRate,
                   high_precision = True, clean_rr = True, 
                   clean_rr_method = 'iqr')

plt.figure(figsize=(22,6))
hp.plotter(wd, m)

for dict_value in m:
        for k, v in m.items():
            m[k] = round(v, 1)

m.keys

for key in m.keys():
    print('%s: %f' %(key, m[key]))


