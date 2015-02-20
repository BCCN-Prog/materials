# The decorator below is supposed to log a warning,
# but just once, not to annoy the user too much.

import math
import functools

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
    f._seen = False
    def wrapper(*args, **kwargs):
        if not f._seen:
            print('Function {} is deprecated, please use something else!'
                  .format(f.__name__))
            f._seen = True
        return f(*args, **kwargs)
    return functools.update_wrapper(wrapper, f)

@deprecate
def square_root(x):
    return math.sqrt(x)

# To test this file, use:
#  py.test-3.4 --doctest-modules deprecation.py
# or
#  python3 -m doctest deprecation.py
