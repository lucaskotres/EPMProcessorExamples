
***REMOVED***
***REMOVED***

***REMOVED***
from pandas.tseries.offsets import *

#pandas is most powerfull Python library to work with tables

@epr.applicationMethod('MondaysAvg')
def mondays_avg(session, epmdataobject):
    '''Calculates the average of every Monday of the last month'''

    sum_mondays = [item for item in df['Timestamp'].dt.dayofweek == 0] #monday=0, sunday=6



    return epr.sessionResult(True)

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