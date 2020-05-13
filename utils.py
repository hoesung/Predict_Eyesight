
import pandas as pd
import numpy as np
from tqdm.notebook import tqdm 
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
pd.set_option('display.float_format','{:.0f}'.format)



def generate_time_series(train):
    '''
    input= pd.DataFrame
    '''
    train_time_series = []
    for n,data in enumerate(tqdm(train.values)):
        train_time_series.extend(convert_timeseries(list(data)))

    return pd.DataFrame(train_time_series)


def convert_timeseries(data,interval=367):
    time_serise = []
    for n,i in enumerate(data[:-interval+1]):
        time_serise.append(data[n:n+interval])
        
    return time_serise
