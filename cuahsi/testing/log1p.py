import math


def log1p(x, base=math.e):
    ''' 
    Find the log of 1+x. This allows log-transformation of data including 
    zeroes.

    Example:
    
    >>> log1p(0)
    0.0
    >>> log1p(math.e-1)
    1.0
    >>> log1p(99, 10)
    2.0
    '''

    return math.log(x+1, base)


if __name__ == '__main__':
    import doctest
    doctest.testmod()