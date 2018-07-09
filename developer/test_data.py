***REMOVED***
import numpy as np
from pandas.tseries.offsets import *


def get_pandas_data():
    '''Return a pandas dataframe'''
    df = pd.DataFrame(np.random.randint(0, 1000, size=(500, 4)), columns=list('ABCD'))
    df['Timestamp'] = pd.date_range('1/1/2018', periods=500, freq='H')
    return df



