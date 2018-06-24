***REMOVED***
import numpy as np
from pandas.tseries.offsets import *


def get_pandas_data():
    '''Return a pandas dataframe'''
    df = pd.DataFrame(np.random.randint(0, 1000, size=(500, 4)), columns=list('ABCD'))
    df['Timestamp'] = pd.date_range('1/1/2018', periods=500, freq='H')
    return df


df = get_pandas_data()
#set Timestamp as index in dataframe
df.set_index('Timestamp', inplace=True)

#total in business hours
#********************************
#filter work hours
df = df.between_time('08:00', '18:00')

#filter busines days
df = df.asfreq(BDay())
Total = df['A'].sum()
#print(Total)
#********************************

#total time A > 500

lower_limit = 500

df2 = get_pandas_data()

df2 = df2.loc[df2['A'] > lower_limit]

df2['newColumn'] = df2['Timestamp'].dt.total_seconds()
print(df2)



