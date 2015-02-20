# The decorator below is supposed to log a warning,
# but just once, not to annoy the user too much.

import math

def deprecate(f):
    """Log a warning when the function is called for the first time.

    >>> @deprecate
    ... def f():
    ...     pass
    >>> f()
    Function f is deprecated, please use something else!
    >>> f()
    >>> f()
    """
    ...
    return f

@deprecate
def square_root(x):
    return math.sqrt(x)

# To test this file, use:
#  py.test-3.4 --doctest-modules deprecation.py
# or
#  python3 -m doctest deprecation.py
