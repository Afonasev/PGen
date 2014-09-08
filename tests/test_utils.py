from pgen import utils


def test_gen_pass():
    """
    >>> utils.gen_pass('k', 'n')
    'b0E6B7f9A5'
    >>> utils.gen_pass('k', 'n') == utils.gen_pass('k', 'n')
    True
    >>> utils.gen_pass('k', 'n', 's') != utils.gen_pass('k', 'm', 's')
    True
    >>> len(utils.gen_pass('k', 'n'))
    10
    >>> assert utils.gen_pass('k', None)
    >>> len(utils.gen_pass('k', 'n', length=15))
    15
    >>> utils.gen_pass('k', 'n', length=666)
    Traceback (most recent call last):
        ...
    ValueError: length(666) > max_length(78)
    """
    pass
