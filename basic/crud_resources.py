import epmprocessor as epr
import epmwebapi as epm
from collections import OrderedDict


@epr.applicationMethod('GetPortalResource')
def get_portal_resource(session, filename, connection, filetype='Binary'):
    """
    Get Portal resource from EPM WebServer
        :param filename: caminho completo do arquivo dentro de resources.
        :param connection: objeto do tipo connection.
        :type filename: string
        :type connection: connection
    """
    epmConn = getFirstItemFromODict(session.connections)
    epResourceManager = epmConn.getPortalResourcesManager()
    file = epResourceManager.getResource(filename)
    if filetype == 'Binary':
        print('binary')
        resource = file.download(epm.DownloadType.Binary)
    elif filetype == 'Text':
        resource = file.download(epm.DownloadType.Text)
    elif filetype == 'Json':
        resource = file.download(epm.DownloadType.Json)


@epr.applicationMethod('GetProcessorResource')
def get_processor_resource(session, filename, connection):
    """ Get Processor resource from EPM WebServer
        :param filename: caminho completo do arquivo dentro de resources.
        :param connection: objeto do tipo connection.
        :type filename: string
        :type connection: connection
    """
    epmConn = getFirstItemFromODict(session.connections)
    epResourceManager = epmConn.getProcessorResourcesManager()
    file = epResourceManager.getResource(filename)


def getFirstItemFromODict(oDict):
    return next(iter(oDict.values())) if isinstance(oDict, OrderedDict) or isinstance(oDict, dict) else None
