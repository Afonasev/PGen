import hashlib


def gen_pass(password, login, site=None, length=10):
    string = ''.join(x for x in [password, login, site] if x)
    str_hash = hashlib.sha224(string.encode()).hexdigest()

    if length > len(str_hash):
        raise ValueError('length (%r) > MAX_LENGTH (56)' % length)

    return str_hash[:length]
