
# Golden Section Search algorithm

# Authors: Antonio Coín Castro
#          Luis Antonio Ortega Andrés



def golden_section_search(
    f,
    lower,
    upper,
    uncertainly_length
):
    """
    Performs Golden section search over the given function.

    Arguments:
        f: Function to minimize
        lower: Initial lower bound to interval
        upper: Initial upper bound to interval
        uncertainly_length: Minimum length of returned interval containing the
            minimum value.
    """

    ratio = 0.618
    alpha = lower + (1-ratio)*(upper - lower)
    mu = lower + ratio*(upper - lower)
    
    while(upper - lower >= uncertainly_length):


        if f(alpha) <= f(mu):
            lower = alpha
            alpha = mu
            mu = lower + ratio*(upper - lower)
        else:
            upper = mu
            mu = alpha
            alpha = lower + (1-ratio)*(upper - lower)
    
    return lower, upper

