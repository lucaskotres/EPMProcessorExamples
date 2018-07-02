***REMOVED***
***REMOVED***

***REMOVED***
import scipy as sp
import numpy as np


@epr.applicationMethod('PredictVariable')
def predict_variable(epmdataobject, starttime, endtime, interval_seconds):

    try:
        queryperiod = epm.QueryPeriod(starttime,endtime)
        processInterval = datetime.timedelta(seconds=interval_seconds)
        aggregationdetails = epm.AggregateDetails(processInterval, epm.AggregateType.Interpolative)
        data = epmdataobject.historyReadAggregate(aggregationdetails,queryperiod)

    except:
        raise Exception('Error in read aggregation')


    #preprocessing and clening data
    #creating array with dataobject values and index

    x = data['Value']
    y = np.array(np.arange(len(x)))

    x = x[~sp.isnan(y)]
    y = y[~sp.isnan(y)]

    import matplotlib.pyplot as plt
    plt.scatter(x, y)
    plt.title("Web traffic over the last month")
    plt.xlabel("Time")
    plt.ylabel("Hits/hour")
    plt.xticks([w * 7 * 24 for w in range(10)], ['week %i' % w for w in range(10)])
    plt.autoscale(tight=True)
    plt.grid()
    plt.show()


def error(f, x, y):
    return sp.sum((f(x)-y)**2)