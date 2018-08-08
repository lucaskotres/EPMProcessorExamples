import numpy as np
import matplotlib.pyplot as plt
***REMOVED***
***REMOVED***
***REMOVED***
import mimetypes
import io
from collections import OrderedDict

from sklearn.tree import DecisionTreeRegressor
***REMOVED***

def getFirstItemFromODict(oDict):
    return next(iter(oDict.values())) if isinstance(oDict, OrderedDict) or isinstance(oDict, dict) else None

try:
    connection = epm.EpmConnection('http://dili:44333', 'http://dili:44332', 'sa', 'Epm2017')

except Exception:
    logger.error("can't connect to epm server")
    exit(1)

try:
    dataobject1 = connection.getDataObjects('SP01_PowerAvg')

except Exception:
    logger.error("can't found {} in the epm Server".format(bvname))
    exit(1)

try:
    dataobject2 = connection.getDataObjects('SP01_WindSpeedAvg')

except Exception:
    logger.error("can't found {} in the epm Server".format(bvname))
    exit(1)

starttime = datetime.datetime(2014, 3, 1, 1, 00, 00)
endtime = datetime.datetime(2014, 3, 30, 1, 00, 00)



queryperiod = epm.QueryPeriod(starttime,endtime)
processInterval = datetime.timedelta(seconds=600)
aggregationdetails = epm.AggregateDetails(processInterval, epm.AggregateType.Interpolative)

data1 = dataobject1['SP01_PowerAvg'].historyReadAggregate(aggregationdetails,queryperiod)
data2 = dataobject2['SP01_WindSpeedAvg'].historyReadAggregate(aggregationdetails,queryperiod)

df1 = pd.DataFrame(
    {'Value': data1['Value'].tolist()})

df2 = pd.DataFrame(
    {'Value': data2['Value'].tolist()})


y = df1.iloc[:,0:1].values

X = df2.iloc[:,0:1].values


#y.reshape(1,-1)
#X.reshape(-1,1)


#y = dataset.iloc[:,0:1].values

#X = dataset.iloc[:, 1:2].values

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
plt.show()





