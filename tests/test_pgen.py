
def test_gen_pass():
    """
    >>> from pgen import gen_pass
    >>> gen_pass('k', 'n')
    'b0E6B7f9A5'
    >>> gen_pass('k', 'n') == gen_pass('k', 'n')
    True
    >>> gen_pass('k', 'n', 's') != gen_pass('k', 'm', 's')
    True
    >>> len(gen_pass('k', 'n'))
    10
    >>> assert gen_pass('k', None)
    >>> len(gen_pass('k', 'n', length=15))
    15
    >>> gen_pass('k', 'n', length=666)
    Traceback (most recent call last):
        ...
    ValueError: length(666) > max_length(78)
    """
    pass
