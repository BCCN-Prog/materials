# Implement a cache, which will store the values
# returned by the function for specific inputs.

import functools

def memoize(func):
    ...
    return func

@memoize
def fibonacci(n):
    """Returns fibonnaci number n.

    See http://en.wikipedia.org/wiki/Fibonacci_number.

    >>> print(fibonacci.cache)
    {}
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(10)
    55
    >>> fibonacci.cache[10]
    55
    >>> fibonacci(40)
    102334155
    """
    assert n >= 0
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test this with
#   py.test-3.4 -v test_memoize.py
# Once that passes, try
#   py.test-3.4 -v test_memoize_mutable.py
