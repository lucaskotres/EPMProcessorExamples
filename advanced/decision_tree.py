import numpy as np
import matplotlib.pyplot as plt
import epmprocessor as epr
import epmwebapi as epm
import datetime
import requests
import mimetypes
import io
from collections import OrderedDict

from sklearn.tree import DecisionTreeRegressor
import pandas as pd


@epr.applicationMethod('PredictVariable')
def predict_variable(session, epmdataobject1, epmdataobject2, starttime, endtime, connection, pathname):


    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID={1c8911a86601fec454d7f103939e5191}')
    print(r.json())

    try:

        queryperiod = epm.QueryPeriod(starttime, endtime)
        processInterval = datetime.timedelta(seconds=600)
        aggregationdetails = epm.AggregateDetails(processInterval, epm.AggregateType.Interpolative)

        data1 = epmdataobject1.historyReadAggregate(aggregationdetails, queryperiod)
        data2 = epmdataobject2.historyReadAggregate(aggregationdetails, queryperiod)
    except Exception:
        print('Erro ao consultar dataobjects')

    df1 = pd.DataFrame(
        {'Value': data1['Value'].tolist()})

    df2 = pd.DataFrame(
        {'Value': data2['Value'].tolist()})

    y = df1.iloc[:, 0:1].values

    X = df2.iloc[:, 0:1].values

    X_test = np.array([0, 3, 6, 9, 12, 15, 18])
    X_test = X_test.reshape(-1, 1)

    # Fit regression model
    regr_1 = DecisionTreeRegressor(max_depth=2)
    regr_2 = DecisionTreeRegressor(max_depth=5)
    regr_1.fit(X, y)
    regr_2.fit(X, y)

    # Predict

    y_1 = regr_1.predict(X_test)
    print(y_1)
    print(X_test)
    y_2 = regr_2.predict(X_test)

    print(y_2)
    print(X_test)

    # Plot the results
    plt.figure()
    plt.scatter(X, y, color='red', label="data")
    plt.plot(X_test, regr_1.predict(X_test), color="blue", label="max_depth=2", linewidth=2)
    plt.plot(X_test, regr_2.predict(X_test), color="yellow", label="max_depth=5", linewidth=2)
    plt.xlabel("data")
    plt.ylabel("target")
    plt.title("Decision Tree Regression")
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    epmConn = getFirstItemFromODict(session.connections)
    epResourceManager = epmConn.getPortalResourcesManager()
    imgFolder = epResourceManager.getResource(pathname)

    resource = imgFolder.upload('predict_Decision_tree_regression.png', buf, 'Scatterplot gerado pelo Processor',
                                mimetypes.types_map['.png'],
                                overrideFile=True)




def getFirstItemFromODict(oDict):
    return next(iter(oDict.values())) if isinstance(oDict, OrderedDict) or isinstance(oDict, dict) else None
