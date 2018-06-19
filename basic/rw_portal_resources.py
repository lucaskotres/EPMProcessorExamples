import epmprocessor as epr
import epmwebapi as epm

@epr.applicationMethod('GetPortalResource')
def get_portal_resource(session, filename, connection):
    '''We can get resources from EPM WebServer, first create the connection in Workbench/Settings/Connections'''
    #TODO: verificar como usar um parametro do tipo epmconnection

    print(session.connections)

    epResourceManager = epmConn.getProcessorResourcesManager()
    resource = epResourceManager.getResource(fileModel)

