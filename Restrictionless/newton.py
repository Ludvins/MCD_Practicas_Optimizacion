#!/usr/bin/env python3

import numpy as np

def newton(
        grad,
        hessian,
        x0,
        epsilon,
        max_iter
):
    '''Approximate minimum solution by Newton's method.

    Parameters
    ----------
    grad     : function
        Gradient of the objective function.
    hessian  : function
        Hessian of the objective function
    x0       : number
        Initial guess for a solution.
    epsilon  : number
        Stopping criteria is abs(f(x)) < epsilon.
    max_iter : integer
        Maximum number of iterations of Newton's method.

    Returns
    -------
    xn : number
        Implement Newton's method: compute the linear approximation
        of f(x) at xn and find x intercept by the formula
            x = x - Df(x)/Hf(x)
        Continue until abs(f(xn)) < epsilon and return xn.
        If Df(xn) == 0, return None. If the number of iterations
        exceeds max_iter, then return None.

    Examples
    --------
    >>> f = lambda x: x[0]**2 + x[1]**2
    >>> Df = lambda x: np.array([2*x[0], 2*x[1]])
    >>> Hf = lambda x: np.array([[2, 0], [0, 2]])
    >>> newton(Df,Hf,np.array([1,3]),1e-8,10)
    Found solution after 1 iterations.
    array([0., 0.])
    '''

    for n in range(max_iter):
        H = hessian(x0)
        try:
            H = np.linalg.inv(H)
        except:
            print('Hessian has no inverse. No solution found.')
            return None

        x = x0 - grad(x0)@H

        if (np.linalg.norm(x - x0) < epsilon):
            print('Found solution after',n,'iterations.')
            return x
            break

        x0 = x

    print('Exceeded maximum iterations. No solution found.')
    return None
