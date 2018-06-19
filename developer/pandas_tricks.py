
import epmprocessor as epr
import epmwebapi as epm

import datetime
import pandas as pd
from pandas.tseries.offsets import *

#pandas is the most powerfull Python library to work with tables

@epr.applicationMethod('MondaysAvg')
def mondays_avg(session, epmdataobject, starttime, endtime):
    '''Calculates the average of every Monday of the last month'''



    #endtime = datetime.datetime.now()
    #starttime = endtime - datetime.timedelta(days=30)

    try:
        queryperiod = epm.QueryPeriod(starttime,endtime)
        processInterval = datetime.timedelta(seconds=300)
        aggregationdetails = epm.AggregateDetails(processInterval, epm.AggregateType.Interpolative)
        data = epmdataobject.historyReadAggregate(aggregationdetails,queryperiod)

    except:
        raise Exception('Error in read aggregation')

    print(data)
    #EPM return ndarray, we need to transform in pandas dataframe

    df = pd.DataFrame(
        {'Value':data['Value'],
         'Timestamp':data['Timestamp']}
    )
    print(df)

    #TODO: more elegant method
    #mondays = df.loc(df['Timestamp'].dt.dayofweek == 0)
    #mondays = [item for item in df if df['Timestamp'].dt.dayofweek == 0]  # monday=0, sunday=6
    mondays_idx = [item for item in df['Timestamp'].dt.dayofweek == 0]

    for item in len(mondays_idx):
        if item == True:






    print(mondays)

    return epr.ScopeResult(True)

@epr.applicationMethod('DaytimeWorkConsumption')
def daytime_work_comsumption(session, epmdataobject, starttime, endtime):
    '''calculates the energy consumption in working day from Monday to Friday'''


    data = df.asfreq(BDay())
    data = df.between_time('08:00', '18:00')

    print(data)

    return epr.sessionResult(True)

@epr.applicationMethod('TimeBelow')
def timebelow(session, epmdataobject, lowerlimit, starttime, endtime):

    '''calculates the total time that the variable was below a limit value'''

    df = df.reset_index()

    below_lower_line = df.Data < lowerlimit
    upper_line_crossed = above_upper_line != above_upper_line.shift()
    clusters = upper_line_crossed.cumsum()
    below_lower_line = df.Data < lower_limit

    times = df[below_lower_line].groupby(clusters)["DateTime"].first().tolist()