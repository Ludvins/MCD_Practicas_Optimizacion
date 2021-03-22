
# Dichotomic Search algorithm

# Authors: Antonio Coín Castro
#          Luis Antonio Ortega Andrés



def dichotomic_search(
    f,
    lower,
    upper,
    epsilon,
    uncertainly_length
):
    """
    Performs dichotomic search over the given function.

    Arguments:
        f: Function to minimize
        lower: Initial lower bound to interval
        upper: Initial upper bound to interval
        epsilon: Half length of (alpha, mu) interval.
        uncertainly_length: Minimum length of returned interval containing the
            minimum value.
    """

    while(upper - lower >= uncertainly_length):

        alpha = (lower + upper)/2 - epsilon
        mu = (lower + upper)/2 + epsilon

        if f(alpha) < f(mu):
            upper = mu
        else:
            lower = alpha
    
    return lower, upper

