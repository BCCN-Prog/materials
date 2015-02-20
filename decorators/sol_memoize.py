import functools

# This is the simpler version that does not works
# for kwargs and mutable arguments.
#
# It only passes test_memoize.py.
def memoize_simple(func):
    func.cache = {}
    def wrapper(n):
        try:
            ans = func.cache[n]
        except KeyError:
            ans = func.cache[n] = func(n)
        return ans
    return functools.update_wrapper(wrapper, func)

# This is the full version that does should work
# for kwargs and mutable arguments.
#
# This one passes test_memoize.py and test_memoize_full.py.
def memoize_full(func):
    """
    >>> @memoize_full
    ... def f(*args, **kwargs):
    ...     ans = len(args) + len(kwargs)
    ...     print(args, kwargs, '->', ans)
    ...     return ans
    >>> f(3)
    (3,) {} -> 1
    1
    >>> f(3)
    1
    >>> f(*[3])
    1
    >>> f(a=1, b=2)
    () {'a': 1, 'b': 2} -> 2
    2
    >>> f(b=2, a=1)
    2
    >>> f([1,2,3])
    ([1, 2, 3],) {} -> 1
    1
    >>> f([1,2,3])
    ([1, 2, 3],) {} -> 1
    1
    """
    func.cache = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        try:
            ans = func.cache[key]
        except TypeError:
            # key is unhashable
            return func(*args, **kwargs)
        except KeyError:
            # value is not present in cache
            ans = func.cache[key] = func(*args, **kwargs)
        return ans
    return functools.update_wrapper(wrapper, func)


memoize = memoize_simple
# memoize = memoize_full

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
