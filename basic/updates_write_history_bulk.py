#EPM Processor modules
***REMOVED***
***REMOVED***

***REMOVED***
import numpy as np
***REMOVED***


@epr.applicationMethod('HistoryUpdate')
def history_update(session, epmdataobject):
    '''Update tag with 5 new values'''

    #pandas generate a range of dates
    newdates = pd.date_range('1/1/2018', periods=5,freq='H' )

    #just a five itens list
    newvalues = [50,60,30,40,10]

    # epm data format
    desc = np.dtype([('Value', '>f8'), ('Timestamp', 'object'), ('Quality', '>i4')])
    datatemp = np.empty(len(newvalues), dtype=desc)

    #loop to populate the object before send to EPM
    i=0
    while i < len(newvalues):
        datatemp['Value'][i] = newvalues[i]
        datatemp['Timestamp'][i] = newdates[i]
        datatemp['Quality'][i] = 0
        i = i+1
    try:
        if session.scopeContext == epr.ScopeContext.Test:
            print('Resultado: {valor} - {timestamp}'.format(valor=str(datatemp['Value'][-1]),
                                                                timestamp=datatemp['Timestamp'][-1].isoformat()))
        else:  # Production ou Simulation
            epmdataobject.historyUpdate(datatemp)

    except:
        raise Exception('Error in historyUpdate')
