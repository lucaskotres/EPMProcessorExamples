
***REMOVED***
***REMOVED***
import numpy as np
import scipy.linalg as la  # linear algebra Scipy module

@epr.applicationMethod('DeployPerformance')
def scope_context(session):
    '''work with some linear algebra to test performance'''

    if session.scopeContext == session.scopeContext.Test:
        # do it in test
        print("Deploy and execute this method in an Production or Simulation to compare performance.")
        matrix1 = np.random.rand(5000 ,5000)

        result1 = la.lu(a=matrix1 ,overwrite_a=True  )  # set overwrite_a=True to avoid overhead



        print(result1)

        return epr.ScopeResult(True)

    else:

        matrix1 = np.random.rand(5000 ,5000)

        result1 = la.lu(a=matrix1 ,overwrite_a=True  )  # set overwrite_a=True to avoid overhead

        print(result1)

        return epr.ScopeResult(True)













