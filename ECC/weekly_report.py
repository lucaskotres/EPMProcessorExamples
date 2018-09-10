import epmprocessor as epr
import epmwebapi as epm

import datetime
import pandas as pd

@epr.applicationMethod('WeeklyReport')
def weekly_report(session, dataobject_temperature, dataobject_windspeed,
        write_dataobject_temperature, write_dataobject_windspeed):

    '''Doc '''
    end_date = session.timeEvent
    ini_date = end_date - datetime.timedelta(weeks=1)
    query_period = epm.QueryPeriod(ini_date, end_date)
    process_interval = datetime.timedelta(minutes=10)

    aggregate_details = epm.AggregateDetails(process_interval, 
            epm.AggregateType.Interpolative)
    

    temperature = dataobject_temperature.historyReadAggregate(aggregate_details,
            query_period)
    windspeed = dataobject_windspeed.historyReadAggregate(aggregate_details,
            query_period)


    
    pd_temperature = pd.DataFrame(
            {'Value':temperature['Value'].tolist(),
             'Timestamp':temperature['Timestamp'].tolist()}
            )
    pd_windspeed = pd.DataFrame(
            {'Value':windspeed['Value'].tolist(),
             'Timestamp':windspeed['Timestamp'].tolist()}
            )

    



