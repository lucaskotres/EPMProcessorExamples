***REMOVED***
***REMOVED***


@epr.applicationMethod('GetPortalResource')
def get_portal_resource(session, filename, connection):
    '''We can get resources from EPM WebServer, first create the connection in Workbench/Settings/Connections'''
    # TODO: verificar como usar um parametro do tipo epmconnection

    print(session.connections)
    epmConn = getFirstItemFromODict(session.connections)
    epResourceManager = epmConn.getPortalResourcesManager()
    img = epResourceManager.getResource(filename)

    print(img)


@epr.applicationMethod('GetProcessorResource')
def get_processor_resource(session, filename, connection):
    '''We can get resources from EPM WebServer, first create the connection in Workbench/Settings/Connections'''
    # TODO: verificar como usar um parametro do tipo epmconnection

    print(session.connections)

    epResourceManager = epmConn.getProcessorResourcesManager()
    resource = epResourceManager.getResource(fileModel)


def getFirstItemFromODict(oDict):
    return next(iter(oDict.values())) if isinstance(oDict, OrderedDict) or isinstance(oDict, dict) else None
