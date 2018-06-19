
#we can program different actions depending on the execution context: test, simulation or production

***REMOVED***
***REMOVED***

@epr.applicationMethod('ScopeContext')
def scope_context(session):

    if session.scopeContext == session.scopeContext.Test:
        #do it in test
        print('Test Context')

    if session.scopeContext == session.scopeContext.Simulation:
        #do it in simulation
        print('Simulation Context')

    if session.scopeContext == session.scopeContext.Production:
        #do it in production
        print('Production Context')


