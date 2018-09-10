import epmprocessor as epr
import epmwebapi as epm

import numpy as np
import mimetypes
import io
import datetime
from collections import OrderedDict

import matplotlib.pyplot as plt



#pandas is the most powerfull Python library to work with tables

@epr.applicationMethod('ScatterPlot')
def scatter_plot(session, connection, epmdataobject_1, epmdataobject_2, starttime, endtime, pathname):
    """
    **ScatterPlot**

                Este método gera faz a consulta interpolada de dois Dataobjects e gera um arquivo de imagem, contendo
                gráfico do tipo Scatter, salvo nos resources do Portal.

                            :param session: objeto *session* do EPM Processor
                            :parm connection: connection para os Resources
                            :param epmdataobject_1: dataobject.
                            :param epmdataobject_2: dataobject.
                            :param starttime: datetime de início da consulta.
                            :param endtime: datetime de fim da consulta.
                            :param pathname: Diretório dentro de Resources do Portal
                            :type filename: nome do arquivo a ser salvo.


                            .. note::
                                Esta função serve apenas como validação de caso de uso do sistema.


                            .. warning::
                                Não é necessário informar **Process Interval**.

                                No modo de *TEST* o resultado é apenas impresso na tela.

                                Não é feita distinção entre execuções de : *TEST*, *PRODUCTION* e *SIMULATION*, ou seja
                                o resultado sempre será escrita em em arquivo em caso de sucesso na execução.


                            """

    try:
        queryperiod = epm.QueryPeriod(starttime, endtime)
        processInterval = datetime.timedelta(seconds=300)
        aggregationdetails = epm.AggregateDetails(processInterval, epm.AggregateType.Interpolative)
        data1 = epmdataobject_1.historyReadAggregate(aggregationdetails, queryperiod)
        data2 = epmdataobject_2.historyReadAggregate(aggregationdetails, queryperiod)

    except:
        raise Exception('Error in read aggregation')

    #gera o chart e salva em buffer
    plt.scatter(data1['Value'], data2['Value'])
    plt.title('Scatter Plot')
    bufBoxplot = io.BytesIO()
    plt.savefig(bufBoxplot, format='png')
    bufBoxplot.seek(0)


    print(session.connections)
    epmConn = getFirstItemFromODict(session.connections)
    epResourceManager = epmConn.getPortalResourcesManager()
    imgFolder = epResourceManager.getResource(pathname)

    resource = imgFolder.upload('scatter.png', bufBoxplot, 'Scatterplot gerado pelo Processor',mimetypes.types_map['.png'], overrideFile=True)


def getFirstItemFromODict(oDict):
    return next(iter(oDict.values())) if isinstance(oDict, OrderedDict) or isinstance(oDict, dict) else None