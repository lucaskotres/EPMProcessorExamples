
***REMOVED***
***REMOVED***
***REMOVED***
import requests

from sklearn.tree import DecisionTreeRegressor
***REMOVED***


@epr.applicationMethod('WritePredictVariable')
def predict_variable(session, epmdataobject1, epmdataobject2, starttime, endtime, write_dataobject):
    url = 'http://servicos.cptec.inpe.br/XML/estacao/SBGR/condicoesAtuais.xml'

    from xml.etree import ElementTree
    response = requests.get(url)
    tree = ElementTree.fromstring(response.content)
    wind = tree.find('vento_int').text

    wind = float(wind)
    print('Previsão de vento para a próxima hora: {}'.format(wind))
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

    # Fit regression model

    regr_1 = DecisionTreeRegressor(max_depth=5)
    regr_1.fit(X, y)

    # Predict
    y_predicted = regr_1.predict(wind)

    print('Previsão de potência baseado no modelo gerado em árvore de decisão: {}'.format(float(y_predicted[0])))

    date = datetime.datetime.now()
    value = float(y_predicted[0])
    quality = 0  # zero is Good in OPC UA

    write_dataobject.write(value, date, quality)


