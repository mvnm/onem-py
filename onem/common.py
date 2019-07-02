ALLOWED_METHODS = ['GET', 'POST', 'PUT', 'DELETE']


def sanitize_method(method, default='GET'):
    if method is None:
        return default

    if method.upper() not in ALLOWED_METHODS:
        raise Exception(f'Invalid method. Allowed: {ALLOWED_METHODS}')

    return method.upper()


def sanitize_url(url):
    if not url.startswith('/'):
        raise Exception('Invalid url path.')
    return url