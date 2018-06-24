
***REMOVED***
***REMOVED***

import numpy as np
***REMOVED***
***REMOVED***
from pandas.tseries.offsets import *


#pandas is the most powerfull Python library to work with tables

@epr.applicationMethod('MondaysDescribe')
def mondays_describe(session, epmdataobject, starttime, endtime):
    '''Shows the statistical describe of every Monday in period'''


    try:
        queryperiod = epm.QueryPeriod(starttime, endtime)
        processInterval = datetime.timedelta(seconds=300)
        aggregationdetails = epm.AggregateDetails(processInterval, epm.AggregateType.Interpolative)
        data = epmdataobject.historyReadAggregate(aggregationdetails, queryperiod)

    except:
        raise Exception('Error in read aggregation')

    # EPM return ndarray, we need to transform in pandas dataframe
    df = pd.DataFrame(
        {'Value': data['Value'].tolist(),
         'Timestamp': data['Timestamp'].tolist()}
    )
    #creating a new column with the weekday name
    df['day_of_week'] = df['Timestamp'].dt.weekday_name

    #fitering by Monday
    filtered_data = df[df.day_of_week == 'Monday']


    print(filtered_data.describe())


@epr.applicationMethod('DaytimeWorkConsumption')
def daytime_work_comsumption(session, epmdataobject, starttime, endtime):
    '''calculates the energy consumption in business time'''

    try:
        queryperiod = epm.QueryPeriod(starttime, endtime)
        processInterval = datetime.timedelta(seconds=300)
        aggregationdetails = epm.AggregateDetails(processInterval, epm.AggregateType.Interpolative)
        data = epmdataobject.historyReadAggregate(aggregationdetails, queryperiod)

    except:
        raise Exception('Error in read aggregation')

    # EPM return ndarray, we need to transform in pandas dataframe
    df = pd.DataFrame(
        {'Value': data['Value'].tolist(),
         'Timestamp': data['Timestamp'].tolist()}
    )

    # set Timestamp as index in dataframe
    df.set_index('Timestamp', inplace=True)

    # filter work hours
    df = df.between_time('08:00', '18:00')

    # filter business days
    df = df.asfreq(BDay())

    total = df['Value'].sum()

    print(total)

    return epr.ScopeResult(True)

@epr.applicationMethod('TimeBelow')
def timebelow(session, epmdataobject, lowerlimit, starttime, endtime):
    '''calculates the total time that the variable was below a limit value'''
    try:
        queryperiod = epm.QueryPeriod(starttime, endtime)
        processInterval = datetime.timedelta(seconds=300)
        aggregationdetails = epm.AggregateDetails(processInterval, epm.AggregateType.Interpolative)
        data = epmdataobject.historyReadAggregate(aggregationdetails, queryperiod)

    except:
        raise Exception('Error in read aggregation')

    # EPM return ndarray, we need to transform in pandas dataframe
    df = pd.DataFrame(
        {'Value': data['Value'].tolist(),
         'Timestamp': data['Timestamp'].tolist()}
    )

    df = df.reset_index()

    below_lower_line = df.Data < lowerlimit
    upper_line_crossed = above_upper_line != above_upper_line.shift()
    clusters = upper_line_crossed.cumsum()
    below_lower_line = df.Data < lower_limit

    times = df[below_lower_line].groupby(clusters)["DateTime"].first().tolist()