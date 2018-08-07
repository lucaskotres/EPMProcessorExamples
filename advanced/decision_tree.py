***REMOVED***
***REMOVED***
import numpy as np
import matplotlib.pyplot as plt
***REMOVED***

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeRegressor


@epr.applicationMethod('PredictVariable')
def predict_variable(epmdataobject1,epmdataobject2, starttime, endtime, connection, pathname):

    queryperiod = epm.QueryPeriod(starttime,endtime)
    processInterval = datetime.timedelta(seconds=60)
    aggregationdetails = epm.AggregateDetails(processInterval, epm.AggregateType.Interpolative)

    data1 = epmdataobject1.historyReadAggregate(aggregationdetails,queryperiod)
    data2 = epmdataobject2.historyReadAggregate(aggregationdetails,queryperiod)

    # Load data

    X = np.empty(1000)

    for i in range(1000):

        X.append(data1['Value'][i],data2['Value'][i])


    #X = np.array([data1['Value'][0:1000],data2['Value'][0:1000]])
    y = data2['Value'][0:1000]


    X_test = np.empty([data1['Value'][1500],data2['Value'][1500]])


    print(X_test)

    # Fit regression model
    regr_1 = DecisionTreeRegressor(max_depth=2)
    regr_2 = DecisionTreeRegressor(max_depth=5)
    regr_1.fit(X, y)
    regr_2.fit(X, y)

    # Predict
    
    y_1 = regr_1.predict(X_test)
    y_2 = regr_2.predict(X_test)

    # Plot the results
    plt.figure()
    plt.scatter(X, y, s=20, edgecolor="black",
                c="darkorange", label="data")
    plt.plot(X_test, y_1, color="cornflowerblue",
             label="max_depth=2", linewidth=2)
    plt.plot(X_test, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
    plt.xlabel("data")
    plt.ylabel("target")
    plt.title("Decision Tree Regression")
    plt.legend()
    bufBoxplot = io.BytesIO()
    plt.savefig(bufBoxplot, format='png')
    bufBoxplot.seek(0)


    print(session.connections)
    epmConn = getFirstItemFromODict(session.connections)
    epResourceManager = epmConn.getPortalResourcesManager()
    imgFolder = epResourceManager.getResource(pathname)

    resource = imgFolder.upload('scatter.png', bufBoxplot, 'Scatterplot gerado pelo Processor',mimetypes.types_map['.png'], overrideFile=True)
