import re
import hashlib


def gen_pass(login, password, site=None, secret_key=None, length=10):
    string = ''.join(x for x in [login, password, site, secret_key] if x)

    password = hashlib.sha512(string.encode()).hexdigest()
    password = re.sub('(?<=\d)\d+', '', password, count=0)
    password = ''.join(
        (i.upper() if n % 3 else i) for n, i in enumerate(password)
    )

    max_length = len(password)

    if length > max_length:
        raise ValueError('length(%r) > max_length(%r)' % (length, max_length))

    return password[:length]
