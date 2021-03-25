#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Dichotomic search algorithm for strictly quasiconvex functions.

Usage: $ python dichotomic_search.py

Authors:  Antonio Coín Castro
          Luis Antonio Ortega Andrés
"""

from typing import Callable, Tuple


def dichotomic_search(
    f: Callable[[float], float],
    lower: float,
    upper: float,
    epsilon: float,
    uncertainty_length: float,
    verbose: bool = False,
) -> Tuple[float, float]:
    """
    Perform dichotomic search over a given function.

    Arguments
    ---------
    f : callable
        Function to minimize. Must be strictly quasiconvex in [lower, upper].
    lower : float
        Lower end of initial interval.
    upper : float
        Upper end of initial interval.
    epsilon: float
        Half length of the intermediate intervals (alpha, mu).
    uncertainty_length : float
        Minimum length of final interval containing the minimum value.
    verbose : bool
        Whether to print information after each iteration.

    Returns
    -------
    lower : float
        Lower end of final interval.
    upper : float
        Upper end of final interval.
    it : integer
        Number of iterations until convergence.

    Example
    -------
    >>> def f(x): return x**2 - 2
    >>> a1, b1 = -5, 5
    >>> length = 0.001
    >>> eps = length/10.
    >>> lower, upper, _ = dichotomic_search(f, a1, b1, eps, length)
    >>> print(f"[{lower:.4f}, {upper:.4f}]")
    [-0.0001, 0.0007]
    """
    i = 0

    # Loop until stopping condition is reached
    while(upper - lower >= uncertainty_length):
        # Define intermediate interval
        alpha = (lower + upper)/2. - epsilon
        mu = (lower + upper)/2. + epsilon

        # Update current interval
        if f(alpha) < f(mu):
            upper = mu
        else:
            lower = alpha

        i += 1

        if verbose:
            print(
                f"Iteration {i}, uncertainty interval [{lower:.4f}, {upper:.4f}]")

    return lower, upper, i


def main():
    """Run a simple example of dichotomic search."""
    def f(x):
        return (x-1)**2 - 1  # Strictly quasiconvex

    a1, b1 = -5, 5
    length = 0.001
    eps = length/10.

    print("Minimizing f(x)=(x-1)^2 - 1 in [0,1] ...")
    lower, upper, it = dichotomic_search(f, a1, b1, eps, length)
    print(f"[dichotomic_search] Convergence reached after {it} iterations.")
    print(f"The minimum is contained in [{lower:.5f}, {upper:.5f}].")


if __name__ == "__main__":
    import doctest
    doctest.testmod()  # Test cases
    main()  # Run example
