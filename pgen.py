import hashlib


def gen_pass(password, login, site=None, length=10):
    string = ''.join(x for x in [password, login, site] if x)
    str_hash = hashlib.sha224(string.encode()).hexdigest()

    max_length = len(str_hash)

    if length > max_length:
        raise ValueError('length(%r) > max_length(%r)' % (length, max_length))

    return str_hash[:length]
